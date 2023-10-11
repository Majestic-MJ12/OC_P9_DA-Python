# Importing necessary modules and functions from Django
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Importing views and custom view for the users app
from users import views as views
from users.views import UnsubscribeView

# URL patterns for the Django project
urlpatterns = [
    # Admin site URL
    path('admin/', admin.site.urls),

    # URL for user registration
    path('register/', views.register, name='register'),

    # URL for user profile page
    path('profile/', views.profile, name='profile'),

    # URL for user login page using Django's built-in auth_views
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),

    # URL for user logout page using Django's built-in auth_views
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

    # URL for user subscriptions page
    path('subscriptions/', views.subscriptions, name='subscriptions'),

    # URL for confirming unsubscribe action using custom view UnsubscribeView
    path('subscriptions/confirm_unsub/<int:pk>/', UnsubscribeView.as_view(), name='confirm-unsub'),

    # Including URLs from the reviews app
    path('', include('reviews.urls')),
]

# Adding static and media URL patterns if in DEBUG mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
