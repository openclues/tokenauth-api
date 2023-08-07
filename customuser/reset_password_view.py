from django.contrib.auth.views import PasswordResetView
from django.shortcuts import render, redirect
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_decode
from django.utils.timezone import now, timedelta
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_view, extend_schema

User = get_user_model()


def custom_password_reset_confirm(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        if request.method == 'POST':
            # Process the password reset form data and set the new password
            new_password = request.POST.get('new_password')
            user.set_password(new_password)
            user.save()
            return redirect('password_reset_complete')  # Redirect to a success page

        # Check if the token has expired        # The token is valid and not expired, render the reset password form
        return render(request, 'customuser/custom_password_reset_confirm.html')

    else:
        # Invalid link or token
        return render(request, 'customuser/custom_password_reset_invalid.html')


