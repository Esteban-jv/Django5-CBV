from django.shortcuts import render

from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordResetView

class UserLoginView(LoginView):
    template_name="login.html"
    next_page="/management/"
    redirect_authenticated_user=True
    # extra_context={
    #     'key1':"valor 1",
    #     'key2':"valor 2",
    # }

class UserLogoutView(LogoutView):
    next_page="/auth/login"


class UserPasswordChangeView(PasswordChangeView):
    template_name="password-change.html"
    next_page="/auth/login"


class UserPasswordResetView(PasswordResetView):
    template_name="reset-password.html"