from django.shortcuts import render, redirect
from .models import ImageHistory
from django.utils import timezone
from django.contrib.auth.decorators import login_required
# Create your views here.
# Image paths and names
image_paths = [
    {'path': '/static/1.png', 'name': 'One'},
    {'path': '/static/2.png', 'name': 'Two'},
    {'path': '/static/3.png', 'name': 'Three'},
    {'path': '/static/4.png', 'name': 'Four'},
    {'path': '/static/5.png', 'name': 'Five'},
]



@login_required(login_url='users:login')

def dashboard(request):
    image_index = request.session.get('image_index', 0)
    last_interaction = request.session.get('last_interaction', str(timezone.now()))

    # Handle button clicks
    if request.method == 'POST':
        # image_index = request.session.get('image_index', 0)
        # last_interaction = request.session.get('last_interaction', str(timezone.now()))
        action = request.POST.get('action')
        current_image = image_paths[image_index]

        if action == 'left':
            # Reject the image
            ImageHistory.objects.create(image_path=current_image['path'], action='reject', user=request.user)
            request.session['last_interaction'] = str(timezone.now())
            message = f"{request.user.first_name}, you have rejected image {current_image['name']}"
            return render(request, 'dashboard.html', {'message': message})
        elif action == 'right':
            # Accept the image
            ImageHistory.objects.create(image_path=current_image['path'], action='accept', user=request.user)
            request.session['last_interaction'] = str(timezone.now())
            message = f"{request.user.first_name}, you have selected image {current_image['name']}"
            return render(request, 'dashboard.html', {'message': message})

    # Check if 5 seconds have elapsed since the last interaction
    time_elapsed = timezone.now() - timezone.datetime.fromisoformat(last_interaction)
    if time_elapsed.total_seconds() >= 5:
        image_index = (image_index + 1) % len(image_paths)
        request.session['image_index'] = image_index
        request.session['last_interaction'] = str(timezone.now())

    # Get the current image path and name
    current_image = image_paths[image_index]

    if image_index == 0 and len(image_paths) == len(ImageHistory.objects.filter(user=request.user).all()):
        message = f"{request.user.first_name}, you have rated all the images. Thank you!"
        return render(request, 'dashboard.html', {'message': message})
   
    context = {
        'image_path': current_image['path'],
        'image_name': current_image['name'],
        'image_index': image_index,
        'total_images': len(image_paths),
        'welcome_message':f'Welcome {request.user.first_name}'
    }
    return render(request, 'dashboard.html', context)

def history(request):
    history = ImageHistory.objects.filter(user=request.user).order_by('-timestamp')
    context = {'history': history}
    return render(request, 'history.html', context)