"""ryanthtrablog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.urls import include, re_path
from django.conf.urls.static import static
from django.conf import settings
import posts.views
import sitepages.views

urlpatterns = [
    path('aod894hnfskoui3iokd38bi3iuvnki/', admin.site.urls),
    path('', posts.views.home, name="home_page"),
    # path('posts/<int:post_id>/', views.post_details),
    re_path(r'^posts/(?P<post_id>[0-9]+)/$', posts.views.post_details, name="post_details"),
    path('about', sitepages.views.about, name="about_page")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
