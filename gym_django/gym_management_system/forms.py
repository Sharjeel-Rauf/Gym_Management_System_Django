from .models import Membership, Attendance
from django import forms

class MembershipForm(forms.ModelForm):
    class Meta:
        model=Membership
        fields= "__all__"

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['member', 'date', 'present']