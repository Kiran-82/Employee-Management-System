from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('login/', views.admin_login, name='admin_login'),
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('employees/', views.employee_list, name='employee_list'),
    path('employees/add/', views.add_employee, name='add_employee'),
    path('employees/edit/<int:id>/', views.edit_employee, name='edit_employee'),
      path('employees/delete/<int:id>/', views.delete_employee, name='delete_employee'),  # Delete Employee URL
      path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
