from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import UserProfile
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout

class UserProfileView(View):
    def get(self, request, user_id):
        try:
            user_profile = UserProfile.objects.get(id=user_id)
            data = {
                'username': user_profile.username,
                'bio': user_profile.bio,
                'profile_picture': user_profile.profile_picture.url if user_profile.profile_picture else None,
            }
            return JsonResponse(data)
        except UserProfile.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)

    def post(self, request):
        # Logic for creating a new user profile
        pass

    def put(self, request, user_id):
        # Logic for updating an existing user profile
        pass

    def delete(self, request, user_id):
        # Logic for deleting a user profile
        pass

def profile(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    user_profile = get_object_or_404(UserProfile, user=user)
    return render(request, 'users/profile.html', {'user_profile': user_profile})

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        bio = request.POST.get('bio', '')
        profile_picture = request.FILES.get('profile_picture')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return render(request, 'users/register.html')

        user = User.objects.create_user(username=username, email=email, password=password)
        user_profile = UserProfile.objects.create(user=user, bio=bio, profile_picture=profile_picture)
        messages.success(request, 'Registration successful! Please log in.')
        return redirect('login')
    return render(request, 'users/register.html')

def login_view(request):
    return render(request, 'users/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')