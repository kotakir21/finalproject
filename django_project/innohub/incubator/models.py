from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Incubator(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='incubators_customer')
    engineer = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='incubators_engineer', null=True, blank=True)
    incubator_id = models.CharField(max_length=15, unique=True)
    incubator_title = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=(('Active', 'Active'), ('Pending', 'Pending'), ('Resolved', 'Resolved')), default='Pending')
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    is_resolved = models.BooleanField(default=False)
    severity = models.CharField(max_length=5, choices=(('A', 'A'), ('B', 'B')), default='B')
    is_assigned_to_engineer = models.BooleanField(default=False)
    resolution_steps = models.TextField(blank=True, null=True)
    #incubator specific fields
    position_in_company = models.CharField(
        max_length=20,
        choices=[
            ('Co-founder', 'Co-founder'),
            ('Founder', 'Founder'),
        ]
    )
    applicant_name = models.CharField(max_length=255)
    applicant_phone = models.CharField(max_length=15)
    product_name = models.CharField(max_length=255, blank=True, null=True)
    problem_description = models.TextField(blank=True, null=True)
    solution_description = models.TextField(blank=True, null=True)
    serving_sectors = models.CharField(max_length=255)
    competitors_description = models.TextField()
    market_potential = models.TextField()
    have_technical_documentation = models.BooleanField(default=False)
    technical_documentation = models.TextField()
    have_ursb_registration_number = models.BooleanField(default=False)
    ursb_registration_number = models.CharField(max_length=50)
    have_documented_processes = models.BooleanField(default=False)
    documented_processes = models.TextField()
    have_documented_processes = models.BooleanField(default=False)
    have_ura_registration_number = models.BooleanField(default=False)    
    ura_registration_number = models.CharField(max_length=50)
    have_pdpo_registration_number = models.BooleanField(default=False)
    pdpo_registration_number = models.CharField(max_length=50, blank=True, null=True)
    funding_amount = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    hub_requirements = models.TextField()


