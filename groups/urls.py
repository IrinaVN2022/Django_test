
from django.urls import path
from groups.views import ListGroupView, CreateGroupView, UpdateGroupView, DetailGroupView, DeleteGroupView
app_name = 'groups'

urlpatterns = [
    path('', ListGroupView.as_view(), name='list'),
    path('create/', CreateGroupView.as_view(), name='create'),
    path('update/<int:pk>/', UpdateGroupView.as_view(), name='update'),
    path('detail/<int:pk>/', DetailGroupView.as_view(), name='detail'),
    path('delete/<int:pk>/', DeleteGroupView.as_view(), name='delete'),
    ]