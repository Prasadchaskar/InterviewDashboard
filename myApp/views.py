from django.shortcuts import render, redirect, get_object_or_404
from . models import Candidate
from . forms import ScheduleForm, UpdateStatus
from django.core.mail import send_mail
from django.core.mail import EmailMessage
# Create your views here.


def home(request):
    records = Candidate.objects.all().order_by('-scheduled_date')
    return render(request, 'home.html', {'records': records})


def Interviewschedul(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST, request.FILES)
        if form.is_valid():
            can_con = form.cleaned_data['candidate_contact']    
            if Candidate.objects.filter(candidate_contact__contains=can_con).exists():
                var = Candidate.objects.filter(candidate_contact__contains=can_con)
                print("****",var)
                request.session['name'] = request.POST['name']
                request.session['candidate_contact'] = request.POST['candidate_contact']
                request.session['candidate_mail'] = request.POST['candidate_mail']
                request.session['avialable_for'] = request.POST['avialable_for']
                request.session['company'] = request.POST['company']
                request.session['candidate_cv'] = '/media/' + \
                    str(request.FILES.get('candidate_cv'))
                request.session['technology'] = request.POST['technology']
                request.session['post'] = request.POST['post']
                request.session['scheduled_date'] = request.POST['scheduled_date']
                request.session['scheduled_time'] = request.POST['scheduled_time']
                request.session['scheduled_by'] = request.POST['scheduled_by']
                request.session['interviewr_name'] = request.POST['interviewr_name']
                request.session['interviewr_mail'] = request.POST['interviewr_mail']
                request.session['status'] = request.POST['status']
                request.session['remark'] = request.POST['remark']
                return render(request, 'error.html')
            else:
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
    return render(request, 'scheduleform.html', {'form': form})


def update(request, id):
    obj = get_object_or_404(Candidate, id=id)
    can_details = Candidate.objects.get(id=id)
    form = UpdateStatus(request.POST or None, instance=obj)
    context = {'form': form}

    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        return redirect('home')

    else:
        context = {'form': form, 'can_details': can_details}
    return render(request, 'Updateform.html', context)


def Search(request):
    if request.method == 'POST':
        search = request.POST['s']
        records = Candidate.objects.filter(
            name__contains=search)  # serach by name
        records = Candidate.objects.filter(
            candidate_contact__contains=search)  # search by contact
        return render(request, 'search.html', {'search': search, 'records': records})
    else:
        return render(request, 'search.html')


def Schedul_anyway(request):
    name = request.session.get('name')
    candidate_contact = request.session.get('candidate_contact')
    candidate_mail = request.session.get('candidate_mail')
    candidate_cv = request.session.get('candidate_cv')
    print("***", candidate_cv)
    avialable_for = request.session.get('avialable_for')
    company = request.session.get('company')
    technology = request.session.get('technology')
    post = request.session.get('post')
    scheduled_date = request.session.get('scheduled_date')
    scheduled_time = request.session.get('scheduled_time')
    scheduled_by = request.session.get('scheduled_by')
    interviewr_name = request.session.get('interviewr_name')
    interviewr_mail = request.session.get('interviewr_mail')
    status = request.session.get('status')
    remark = request.session.get('remark')

    candidate = Candidate(name=name, candidate_contact=candidate_contact,
                          candidate_mail=candidate_mail, candidate_cv=candidate_cv, avialable_for=avialable_for, company=company,
                          technology=technology, post=post, scheduled_date=scheduled_date, scheduled_time=scheduled_time,
                          scheduled_by=scheduled_by, interviewr_mail=interviewr_mail, interviewr_name=interviewr_name,
                          status=status, remark=remark)
    candidate.save()

    email = EmailMessage(
                    f'{company}: Invitation to Interview',
                    f'Dear {interviewr_name} \nWe would like to invite you to interview for the role with {name},{post} in {technology} \nPlease reply to this email directly with your availability during the following date and time options:\n{scheduled_date}-{scheduled_time}\n Sincerely {company}',
                    'Your Email',
                    [interviewr_mail]
                )
    email.send(fail_silently=False)
    return redirect('home')
    return render(request, 'error.html')
