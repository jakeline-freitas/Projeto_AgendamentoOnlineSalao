from django.urls import path
from django.contrib.auth import views as auth_views  # reutilizando views do django
from .views import SignUpView
urlpatterns = [
    #path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(
        template_name='accounts/loginForm.html'
        ), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
