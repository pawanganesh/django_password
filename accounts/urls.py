from django.urls import path, reverse_lazy
from django.contrib.auth.views import (PasswordChangeView,
                                       PasswordChangeDoneView,
                                       PasswordResetView,
                                       PasswordResetCompleteView,
                                       PasswordResetConfirmView)

from .views import (home_view, login_view, register_view, logout_view, profile_view)

app_name = "account"
urlpatterns = [
    path('home/', home_view, name="home"),
    path('login/', login_view, name="login"),
    path('register/', register_view, name="register"),
    path('profile/<str:username>/', profile_view, name="profile"),
    path('logout/', logout_view, name="logout"),

    #  password change
    path('password_change/', PasswordChangeView.as_view(
        template_name='accounts/password_change.html',
        success_url=reverse_lazy('account:password_change_done')),
         name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(
        template_name='accounts/password_change_done.html'),
         name='password_change_done'),

    #  password reset
    path('password_reset/', PasswordResetView.as_view(
        template_name='accounts/password_reset_form.html',
        subject_template_name='accounts/password_reset_subject.txt',
        email_template_name='accounts/password_reset_email.html',
        success_url=reverse_lazy('account:password_reset_done')),
         name='password_reset'),
    path('password_reset/done', PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='accounts/password_reset_confirm.html',
        success_url=reverse_lazy('account:password_reset_complete')),
         name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html'),
         name='password_reset_complete'),
]
