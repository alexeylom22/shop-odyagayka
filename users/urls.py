from django.urls import path
from . import views
from django.contrib.auth import views as authViews
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('reg', views.register, name='register'),
    path('user/', authViews.LoginView.as_view(template_name='users/user.html'), name='user'),
    path('exit/', authViews.LogoutView.as_view(template_name='users/exit.html'), name='exit'),
    path('profile', views.profile, name='profile'),
]


# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
