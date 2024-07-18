from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.contrib.auth.models import User

def contact_view(request):
    success_message = None
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        message = request.POST.get('message')

        if not request.user.is_authenticated:
            messages.error(request, "You didn't sign up yet, so sign up first.")
            return redirect('signup')
        
        Contact.objects.create(
            full_name=full_name,
            email=email,
            phone_number=phone_number,
            message=message,
            submitted_by=request.user  # Set the authenticated user as the submitter
        )
        success_message = "Your message has been sent successfully!"
        messages.success(request, success_message)
        return redirect('contact_view')  # Redirect to clear the form after submission

    return render(request, "contact/index.html", {'success_message': success_message})

def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists!')
            else:
                user = User.objects.create_user(
                    username=email,  # Assuming username is email
                    email=email,
                    password=password  # The password will be hashed automatically
                )
                messages.success(request, 'Your account has been created successfully!')
                return redirect('contact_view')  # Redirect to the contact page
        else:
            messages.error(request, 'Passwords do not match!')

    return render(request, 'contact/signup.html')
