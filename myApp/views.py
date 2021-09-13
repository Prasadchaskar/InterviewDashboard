from django.shortcuts import render,redirect
from . models import Candidate
from . forms import ScheduleForm

# Create your views here.


def home(request):
    records = Candidate.objects.all()
    return render(request,'home.html',{'records':records})
def Interviewschedul(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ScheduleForm()
    return render(request,'scheduleform.html',{'form':form})

