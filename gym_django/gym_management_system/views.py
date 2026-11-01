from django.shortcuts import render, redirect

from datetime import timedelta

from django.utils import timezone

from django.db.models import Count

from .models import Membership, Attendance

from .forms import MembershipForm, AttendanceForm


# import paginatipon stuff
from django.core.paginator import Paginator

# home & pagination view
def home_view(request):

    # Explicitly order the queryset
    # members = Membership.objects.all().order_by('id')
    members = Membership.objects.all()
  

    # set up pagination with the same ordered queryset
    p = Paginator(Membership.objects.all(), 2)
    page = request.GET.get('page')
    memberships = p.get_page(page)
    attendance_list = Attendance.objects.all()

    return render(request, "gym_management_system/home.html", {'members' : members , 'memberships': memberships, 'attendance_list': attendance_list} )

# search member view
def search_member(request):
    if request.method == "POST":
        searched = request.POST['searched']
        members = Membership.objects.filter(member_name__icontains = searched)
        return render(request, "gym_management_system/search.html", {'searched': searched, 'members': members})
    else:
        return render(request, "gym_management_system/search.html", {})
 

# record attendence view
def record_attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form = AttendanceForm()

    return render(request, 'gym_management_system/record_attendance.html', {'form': form})

# member detail view
def member_detail(request, member_id):
    member = Membership.objects.get(id=member_id)
    return render(request, "gym_management_system/member_detail.html", {'member': member})

# delete member view
def delete_member_view(request, member_id):
    membership = Membership.objects.get(id = member_id)

    if request.method == 'POST':
        membership.delete()
        return redirect('home')

    return render(request, 'gym_management_system/delete_member.html', {'membership': membership})

# create member view
def create_member_view(request):
    if request.method == 'POST':
        form = MembershipForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form = MembershipForm()

    return render(request, 'gym_management_system/create_member.html', {'form': form})

# update member view
def update_member_view(request, member_id):
    membership = Membership.objects.get(id=member_id)

    if request.method == 'POST':
        form = MembershipForm(request.POST, instance=membership)
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form = MembershipForm(instance=membership)

    return render(request, 'gym_management_system/update_member.html', {'form': form, 'membership': membership})

# monthly attendence view
def monthly_attendance(request, member_id):
    member = Membership.objects.get(pk=member_id)
    today = timezone.now()
    first_day_of_month = today.replace(day=1)
    print('first_day:', first_day_of_month)
    last_day_of_month = (first_day_of_month + timedelta(days=32)).replace(day=1) - timedelta(days=1)
    attendance_data = Attendance.objects.filter(
        member=member,
        date__range=[first_day_of_month, last_day_of_month]
    ).values('date', 'present').annotate(total=Count('date')).order_by('date')

    context = {
        'member': member,
        'attendance_data': attendance_data,
        'first_day_of_month': first_day_of_month,
        'last_day_of_month': last_day_of_month,
    }

    return render(request, 'gym_management_system/monthly_attendance.html', context)