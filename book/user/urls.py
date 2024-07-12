from django.urls import path
from .views import UserLoginView, UserLogoutView, UserPasswordChangeView, UserPasswordResetView

# app_name = 'user'
urlpatterns = [
    path('/login', UserLoginView.as_view(), name='login'),
    path('/logout', UserLogoutView.as_view(), name='logout'),
    path('/change-password', UserPasswordChangeView.as_view(), name='change_password'),
    path('/password-reset', UserPasswordResetView.as_view(), name='password_reset'),
    # path('/save/', BookSaveFormView.as_view(), name='save'),
    # path('update/<int:id>', views.update, name='update'),
    # path('delete/<int:id>', views.delete, name='delete'),
]