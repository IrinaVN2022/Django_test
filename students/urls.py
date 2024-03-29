"""lms URL Configuration

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

from django.urls import path


from .views import create_student_view
from .views import detail_student
from .views import delete_student
from .views import CustomUpdateStudentView
from .views import UpdateStudentView
from .views import ListStudentView

# from students.views import view_with_param
# from students.views import view_without_param

app_name = 'students'

urlpatterns = [
    path('', ListStudentView.as_view(), name='list'),                            # students: list
    path('create/', create_student_view, name='create'),            # students/create/
    path('update/<int:pk>/', UpdateStudentView.as_view(), name='update'),
    path('detail/<int:pk>/', detail_student, name='detail'),
    path('delete/<int:pk>/', delete_student, name='delete'),
]

