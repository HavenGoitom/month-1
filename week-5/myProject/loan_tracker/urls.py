from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('loans/', views.loans, name='loans'),
    path('update/<int:loan_id>/', views.update_loan, name='update_loan'),
    path('delete/<int:loan_id>/', views.delete_loan, name='delete_loan'),  # New delete path

]
