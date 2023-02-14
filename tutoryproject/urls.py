"""tutoryproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path ('signup', views.signup),
    path ('signin', views.signin),
    path ('logout', views.logout),
    path('accounts/', include('django.contrib.auth.urls')),
    path('setting', views.setting),
    path('<str:pk>/deleteaccount', views.deleteaccount),
    path('student-profile/<str:pk>', views.profile1),
    path('business-profile/<str:pk>', views.profile2),
    path('create', views.create),
    path('add', views.add),
    path('project/<str:pk>', views.project, name='project'),
    path('project/<str:pk>/download', views.download),
    path('project/<str:pk>/change', views.change),
    path('project/<str:pk>/delete', views.delete),
    path('search', views.search),
    path('courses', views.courses),
    path('courses/webdev', views.webdev),
    path('courses/design', views.design),
    path('courses/project-management', views.projectmanagement),
    path('allprojects', views.allprojects),
]

urlpatterns = urlpatterns+static(settings.MEDIA_URL,
document_root=settings.MEDIA_ROOT)
