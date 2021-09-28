from django.shortcuts import render,redirect,get_object_or_404
from . models import Candidate
from . forms import ScheduleForm,UpdateStatus
from django.core.mail import send_mail
from django.core.mail import EmailMessage
# Create your views here.


def home(request):
    records = Candidate.objects.all().order_by('-scheduled_date')
    return render(request,'home.html',{'records':records})
def Interviewschedul(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            can_name = form.cleaned_data['name']
            can_email = form.cleaned_data['candidate_mail']
            intv_email = form.cleaned_data['interviewr_mail']
            intv_name = form.cleaned_data['interviewr_name']
            job_post = form.cleaned_data['post']
            inv_date = form.cleaned_data['scheduled_date']
            inv_time = form.cleaned_data['scheduled_time']
            comp = form.cleaned_data['company']
            tech = form.cleaned_data['technology']
            cv = form.cleaned_data['candidate_cv']
            
            email = EmailMessage(
                        f'{comp}: Invitation to Interview',
                        f'Dear {intv_name} \nWe would like to invite you to interview for the role with {can_name},{job_post} in {tech} \nPlease reply to this email directly with your availability during the following date and time options:\n{inv_date}-{inv_time}\n Sincerely {comp}',
                        'Your Mail',
                        [intv_email]
                    )
            email.send(fail_silently=False)
            return redirect('home')
    else:
        form = ScheduleForm()
    return render(request,'scheduleform.html',{'form':form})

def update(request,id):
    obj= get_object_or_404(Candidate, id=id)
    can_details = Candidate.objects.get(id=id)
    form = UpdateStatus(request.POST or None, instance= obj)
    context= {'form': form}

    if form.is_valid():
        obj= form.save(commit= False)
        obj.save()  
        return redirect('home')
        
    else:
        context= {'form': form,'can_details':can_details}
    return render(request,'Updateform.html' , context)
