# DEFINE IMPORTS
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.models import User


# START OF FILE: [users]: 'views.py'

# [GET] > userLogin
def login_view(request):
    """
    Display the login page and handle user authentication.

    This view renders the login page for the Eskak application. It also checks
    if the user is already authenticated. If the user is authenticated, they are
    redirected to the profile view. If not, the login page is displayed.

    :param request: HttpRequest object
    :type request: HttpRequest

    :return: Rendered HTML login page or HttpResponseRedirect to profile view
    :rtype: HttpResponse or HttpResponseRedirect
    """
    # Extract the message(if any)
    message = request.GET.get('message', '')
    # Check if user is authenticated
    if request.user.is_authenticated:
        # Redirect to profile using 'reverse'
        return HttpResponseRedirect(reverse('users:profile_view'))
    # Else function will returned login webpage(render)
    return render(request, 'userLogin.html', {'message': message})

# [POST] < userLogin
def login_user(request):
    """
    Authenticate and log in a user.

    This view handles user authentication by checking the provided username
    and password. If the user is successfully authenticated, they are logged
    in, and they are redirected to the profile view. If authentication fails,
    an error message is displayed on the login page.

    :param request: HttpRequest object containing user input
    :type request: HttpRequest

    :return: Rendered HTML login page with an error message or HttpResponseRedirect to profile view
    :rtype: HttpResponse or HttpResponseRedirect
    """
    # Extract the username and password from the POST request
    username = request.POST['username']
    password = request.POST['password']

    # Attempt to authenticate the user
    user = authenticate(username=username, password=password)

    # User is NOT authenticated
    if user is None:
        # Update the error_message parameter to pass to the view
        error_message = "Invalid Username or Password!"

        # Render the login page with the error message
        return render(request, 'userLogin.html', {'error_message': error_message})
    else:
        # Log in the user
        login(request, user)

        # Redirect to the profile view
        return HttpResponseRedirect(reverse('users:profile_view'))


# [GET] > userRegister 
def register_view(request):
    """
    Display the user registration page.

    This view renders the user registration page for the Eskak application.
    It checks whether the user is already authenticated; if authenticated,
    the user is redirected to the logout view with an error message. If not
    authenticated, the registration page is displayed.

    :param request: HttpRequest object
    :type request: HttpRequest

    :return: Rendered HTML registration page or HttpResponseRedirect to logout view with an error message
    :rtype: HttpResponse or HttpResponseRedirect
    """
    # Check if the user is already authenticated
    if request.user.is_authenticated:
        # Redirect to the logout view with an error message
        return HttpResponseRedirect(reverse('users:logout_view') + '?error_message=You must be logged out in to register a new user.')

    # If the user is not authenticated, render the registration page
    return render(request, 'userRegister.html')


# [POST] > userRegister 
def register_user(request):
    """
    Register a new user.

    This view handles user registration by processing the provided registration
    form data. It checks if the passwords match and creates a new user account
    with the given username, email, and password. If successful, the user is
    redirected to the login view. If there is an error, an error message is
    displayed on the registration page.

    :param request: HttpRequest object containing user input
    :type request: HttpRequest

    :return: HttpResponseRedirect to login view on successful registration or
             HttpResponseRedirect to registration view with an error message on
             failure
    :rtype: HttpResponseRedirect
    """
    raiseFlag = False

    while raiseFlag == False:
        if request.method == 'POST':
            # Fetch data from the form
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')

        # Check if both passwords match
        if password != confirm_password:
            return HttpResponseRedirect(reverse('users:register_view') + f'?error_message=Make sure your password match!')

        try:
            # Create a new User instance and set attributes
            new_user = User.objects.create_user(username=username, password=password)
            # Set email
            new_user.email = email
            # Set is_staff
            new_user.is_staff = False
            # Set is_superuser
            new_user.is_superuser = False
            # Save user to the database
            new_user.save()
            print("Successfully Added New User to Database")
            print(f"USERNAME - {username}\nPassword(op-sec) - {password}\nEmail - {email}")
            # Redirect user to the login view
            return HttpResponseRedirect(reverse('users:login_view'))
        except Exception as ex:
            # Get the error message
            error_message = str(ex)
            # Redirect back to the registration view with the error message
            return HttpResponseRedirect(reverse('users:register_view') + f'?error_message={error_message}')

        
# [GET] > userProfile
def profile_view(request):
    """
    Display the user's profile page.

    This view renders the user's profile page for the Eskak application.

    :param request: HttpRequest object
    :type request: HttpRequest

    :return: Rendered HTML profile page
    :rtype: HttpResponse
    """
    return render(request, 'userProfile.html')


# [GET] > userLogout & [POST] < userLogout
def logout_view(request):
    """
    Log out the user and redirect to the login page.

    This view logs out the currently authenticated user and redirects them
    to the login page of the Eskak application.

    :param request: HttpRequest object
    :type request: HttpRequest

    :return: HttpResponseRedirect to the login view
    :rtype: HttpResponseRedirect
    """
    logout(request)
    return redirect(reverse('users:login_view'))

 

'''CODE IMPLEMENTED & CONTRIBUTED BY: BRANDEN VAN STADEN'''
