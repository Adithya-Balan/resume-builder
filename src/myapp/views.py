from django.conf import settings
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import UserCreationForm, UserInfoForm, EducationForm, WorkingInfoForm, OtherForm, SkillForm
from django.template.loader import render_to_string
from weasyprint import HTML
from django.contrib.staticfiles import finders
from django.contrib.auth.models import User
from .models import userinfo, working_info, skill, others, education


# Create your views here.

def index(request):
    form =  UserInfoForm()
    if request.method == 'POST':
        form = UserInfoForm(request.POST)
        if form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.user = request.user
            form_obj.save()
            return redirect('/education')
    context = {
        'form' : form 
    }
    return render(request, 'myapp/index.html', context)

def sign_up(request):
    form = UserCreationForm()
    context = {
        'form' : form 
    }
    return render(request, 'registration/sign-up.html', context)

def education(request):
    form = EducationForm()
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.user = request.user
            form_obj.save()
            if 'submit' in request.POST:
                return redirect('/work-history')
            if 'add_another' in request.POST:
                return redirect('/education')
    context = {
        'form' : form 
    }
    return render(request, 'myapp/education.html', context)

def work_history(request):
    form = WorkingInfoForm()
    if request.method == 'POST':
        form = WorkingInfoForm(request.POST)
        if form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.user = request.user
            form_obj.save()
            if 'submit' in request.POST:
                return redirect('/skill')
            if 'add_another' in request.POST:
                return redirect('/work-history')
    context = {
        'form' : form 
    }
    return render(request, 'myapp/working.html', context)

def skills(request):
    form = SkillForm()
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.user = request.user
            form_obj.save()
            print(True)
            return redirect('/others')
    context = {
        'form' : form 
    }
    return render(request, 'myapp/skills.html', context)

#other page.
def others(request):
    form = OtherForm()
    if request.method == "POST":
        form = OtherForm(request.POST)
        if form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.user = request.user
            form_obj.save()
            return redirect('/generate-pdf')
    context = {
        'form' : OtherForm() 
    }
    return render(request, 'myapp/others.html', context)

def generate_pdf(request):
    userinfo_obj = userinfo.objects.get(user = request.user)
    workinginfo_obj = request.user.working_info_s.all().order_by('id')
    skill_obj = skill.objects.get(user=request.user)
    others_obj = request.user.other_info
    education_obj = request.user.education_info.all()
    form = UserInfoForm()

# Data dictionary
    data = {
        'form': form,
        'userinfo_obj': userinfo_obj,
        'workinginfo_obj': workinginfo_obj,
        'skill_obj': skill_obj,
        'others_obj': others_obj,
        'education_obj': education_obj,
    }

    html_string = render_to_string('myapp/output.html', data)
    # Create a response object
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="document.pdf"'
    
    # Convert HTML to PDF
    HTML(string=html_string).write_pdf(response)
    return response