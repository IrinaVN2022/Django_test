"""LMS URL Configuration

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
from django.urls import path, re_path, include
from django.views.generic import RedirectView

from core.views import index
# from teachers.views import get_render_list, get_render_create, get_render_update, get_render_detail


# from core.views import view_with_param
# from core.views import view_without_param

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path('', index, name='home'),
    path('students/', include('students.urls')),
    path('teachers/', include('teachers.urls')),
    # path('teachers/', get_render_list),
    # path('teachers/create/', get_render_create),
    # path('teachers/update/<int:pk>/', get_render_update),
    # path('teachers/detail/<int:pk>/', get_render_detail),
    path('groups/', include('groups.urls')),
    path('courses/', include('courses.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

]
