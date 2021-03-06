"""myblog URL Configuration

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
from django.urls import path,include

from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('index/', views.index),    # 在网页很多的情况下，这种配置网页路径的方法不太理想
    path('blog/', include('blog.urls', namespace='blog')),  # 这里的index是总路径（方法1）
    # path('blog/', include(('blog.urls', 'blog'), namespace=None)),  # 方法2
    path('blog2/', include('blog2.urls'))
]
