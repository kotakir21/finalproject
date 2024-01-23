from django.urls import path
from . import views

urlpatterns = [
    path('create-ictsme/', views.create_ictsme, name='create-ictsme'),  # Updated view and URL
    path('customer-active-ictsmes/', views.customer_active_ictsmes, name='customer-active-ictsmes'),  # Updated view and URL
    path('customer-resolved-ictsmes/', views.customer_resolved_ictsmes, name='customer-resolved-ictsmes'),  # Updated view and URL
    path('assign-ictsme/<str:ictsme_id>/', views.assign_ictsme, name='assign-ictsme'),  # Updated view and URL
    path('ictsme-details/<str:ictsme_id>/', views.ictsme_details, name='ictsme-details'),  # Updated view and URL
    path('ictsme-queue/', views.ictsme_queue, name='ictsme-queue'),  # Updated view and URL
    path('officer-active-ictsmes/', views.officer_active_ictsmes, name='officer-active-ictsmes'),  # Updated view and URL
    path('officer-resolved-ictsmes/', views.officer_resolved_ictsmes, name='officer-resolved-ictsmes'),  # Updated view and URL
    path('resolve-ictsme/<str:ictsme_id>/', views.resolve_ictsme, name='resolve-ictsme'),  # Updated view and URL
]
