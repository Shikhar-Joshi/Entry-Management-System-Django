from django.shortcuts import render, redirect
from .models import Information
import datetime


from django.shortcuts import get_object_or_404


def index(request):
    details = Information.objects.all()
    return render(request, 'home/index.html',
                  {'details': details})


def add_data_db(request):
    visitor_name = request.POST["visitor_name"]
    visitor_email = request.POST["visitor_email"]
    visitor_number = request.POST["visitor_number"]

    host_name = request.POST["host_name"]
    host_email = request.POST["host_email"]
    host_number = request.POST["host_number"]

    check_in = datetime.datetime.now().strftime('%H:%M:%S')

    meeting_data = Information(
                        visitor_name=visitor_name, visitor_email=visitor_email,
                        visitor_number=visitor_number, host_name=host_name,
                        host_email=host_email, host_number=host_number, check_in=check_in
                    )

    meeting_data.save()
    return redirect('home_page')
