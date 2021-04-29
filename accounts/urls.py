from django.urls import path, include
from .views import SignUpView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('change-password/', auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html', success_url = '/'), name='change_password'),
]
