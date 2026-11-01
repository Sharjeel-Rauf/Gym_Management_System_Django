from django.db import models

from django.urls import reverse

from django.contrib.auth.models import User

from django.utils import timezone

# Create your models here.
class Membership(models.Model):
    member_name = models.CharField(max_length = 255)
    parent_name = models.CharField(max_length = 255)
    cnic_no = models.CharField(max_length = 15, unique = True)
    DOB = models.DateTimeField()
    email = models.EmailField(max_length=255, null=True, blank=True)
    mobile_number = models.CharField(max_length=15)
    occupation_choices = [
        ('Services', 'Services'),
        ('Engineering', 'Engineering'),
        ('Medical', 'Medical'),
        ('Other', 'Other'),
    ]
    occupation = models.CharField(max_length=255, choices=occupation_choices, default='Other')
    address = models.TextField(null=True, blank=True)
    reference_choices = [
        ('Ahmed', 'Ahmed'),
        ('Ali', 'Ali'),
        ('Ashar', 'Ashar'),
        ('Other', 'Other'),
    ]
    reference = models.CharField(max_length=255, choices=reference_choices, default='Other')
    gender_choices = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    gender = models.CharField(max_length=10, choices=gender_choices, default='Male')
    blood_group_choices = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('Unknown', 'Unknown'),
    ]
    blood_group = models.CharField(max_length=10, choices=blood_group_choices, default='Unknown')
    member_timing_choices = [
        ('Gents Morning', 'Gents Morning'),
        ('Ladies Evening', 'Ladies Evening'),
        ('Other', 'Other'),
    ]
    member_timings = models.CharField(max_length=255, choices=member_timing_choices, default='Other')
    height_cm = models.IntegerField(verbose_name='Height (cm)', null=True, blank=True)
    weight_kg = models.FloatField(verbose_name='Weight (KG)', null=True, blank=True)

    admission_fee = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Admission Fee', default=0.00)
    monthly_fee = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Monthly Fee', default=0.00)

    trainer_choices = [
        ('Big Show', 'Big Show'),
        ('Under Taker', 'Under Taker'),
        ('Other', 'Other'),
    ]
    trainer_name = models.CharField(max_length=255, verbose_name='Trainer Name', choices = trainer_choices, default = 'Not required')
    trainer_fee = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Trainer Fee', default=0.00)

    starting_date = models.DateTimeField(verbose_name='Starting Date', null=True, blank=True)
    admission_date = models.DateTimeField(verbose_name='Admission Date', null=True, blank=True)


    def __str__(self):
        return f'{self.member_name}'
    
    class Meta:
        verbose_name_plural = "Gym admin"

    def get_absolute_url(self):
        return reverse("home")
    
class Attendance(models.Model):
    member = models.ForeignKey(Membership, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    present = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.member.member_name} - {self.date}"
    
