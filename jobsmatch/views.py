from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import LoginForm, JobForm, CriteriaForm, UserForm, ProfileForm
from .models import Profile, Career, Job, Criteria



def index(request):
    login_form = LoginForm()
    context = {'form' : login_form}
    return render(request, 'jobsmatch/index.html', context)


'''
view single full applicant profile
'''
def applicant(request, user_id):
    profile = Profile.objects.raw('SELECT id, (SELECT email FROM auth_user WHERE id = user_id LIMIT 1) AS email, (SELECT first_name FROM auth_user WHERE id = user_id LIMIT 1) AS fname, (SELECT last_name FROM auth_user WHERE id = user_id LIMIT 1) AS lname FROM jobsmatch_profile WHERE user_id = %s', [user_id])
    career = Career.objects.raw('SELECT * FROM jobsmatch_career WHERE user_id = %s', [user_id]);
    context = { 'profile' : profile, 'career' : career}
    return render(request, 'jobsmatch/applicant.html', context)


def register(request):
    if request.method == 'POST':       
        form = UserForm(request.POST or None)       
        if form.is_valid():
            User.objects.create_user(username=form.cleaned_data['username'], first_name=form.cleaned_data['first_name'], last_name=form.cleaned_data['last_name'], email = form.cleaned_data['email'], password = form.cleaned_data['password'])
            user_form = UserForm()
            context = {'save_user_message' : 'You have been successfully registered. Please login', 'form' : user_form}
            return render(request, 'jobsmatch/register.html', context)
    else:
        user_form = UserForm()
        context = {'form' : user_form}
        return render(request, 'jobsmatch/register.html', context)



def criteria(request):
    if request.method == 'POST':       
        form = CriteriaForm(request.POST or None)       
        if form.is_valid():
            Criteria.objects.create(certifications=form.cleaned_data['certifications'], skills=form.cleaned_data['skills'], name=form.cleaned_data['name'])
            criteria_form = CriteriaForm()
            context = {'save_citeria_message' : 'Criteria has been created', 'form' : criteria_form}
            return render(request, 'jobsmatch/criteria.html', context)
    else:
        criteria_form = CriteriaForm()
        context = {'form' : criteria_form}
        return render(request, 'jobsmatch/criteria.html', context)



def add_job(request):
    if request.method == 'POST':       
        form = JobForm(request.POST or None)       
        if form.is_valid():
            Job.objects.create(title=form.cleaned_data['title'], description=form.cleaned_data['description'], certificates=form.cleaned_data['certificates'], skills=form.cleaned_data['skills'])
            job_form = JobForm()
            context = {'save_job_message' : 'Job has been saved successfully', 'form' : job_form}
            return render(request, 'jobsmatch/add_job.html', context)
    else:
        job_form = JobForm()
        context = {'form' : job_form}
        return render(request, 'jobsmatch/add_job.html', context)



def filter_job(request):
        
    criteria = Criteria.objects.all()
    
    if request.method == 'POST':      
        
        # Get comparison criteria items from the criteria selected    
        criteria_selected = Criteria.objects.get(id__exact=request.POST['criteria_id'])       
        skills = criteria_selected.skills.split(", ")
        certification = criteria_selected.certifications.split(", ")
        
        # Total criteria items
        total_criteria_params = len(certification) + len(skills)
          
        applicants = []

        # Collect applicants as per their occurance in the skillset and certifications 
        # available in the criteria chosen 
        
        for i, val in enumerate(certification):
            resume = Profile.objects.filter(certifications__contains=val)
            for r in resume:
                applicants.append(r.user_id)
                
     
        for i, val in enumerate(skills):
            resume = Profile.objects.filter(skills__contains=val)
            for r in resume:
                applicants.append(r.user_id)
        
        
        # To hold candidates score as per the criteia total items in percentage
        performance_dic = {}    
        unique_applicants_list = set(applicants)
        
    
        #compute a percentage qualification for each occuring applicant as per the criteria ocurrance
        for i, val in enumerate(unique_applicants_list):
            count = applicants.count(val)
            q = count / float(total_criteria_params) * 100
            performance_dic.update({val: float("{0:.2f}".format(q))})
                
        
        candidates = Profile.objects.filter(user_id__in=applicants).select_related()
        form = CriteriaForm()
        context = {'form' : CriteriaForm, 'performance_dic': performance_dic, 'candidates' : candidates, 'applicants': applicants, 'total_criteria_params': total_criteria_params,'criteria' : criteria}
        return render(request, 'jobsmatch/filter.html', context)
    
    else:
        form = CriteriaForm()
        context = {'form' : CriteriaForm, 'criteria' : criteria}
        return render(request, 'jobsmatch/filter.html', context)

    

def admin(request):
    context = {}
    return render(request, 'jobsmatch/admin.html', context)
    
    
    
def log_in(request):
    return HttpResponseRedirect('/jobsmatch/profile')



def verify(request):  
    if request.method == 'POST':       
        form = LoginForm(request.POST or None)       
        if form.is_valid():
            username = form.cleaned_data['username']
            password=form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            
            if user is not None:
                if user.is_active:
                    login(request, user)
                    request.session['username'] = username
                    return HttpResponseRedirect('/jobsmatch/profile');
                else:
                    return HttpResponse('The user is deactivated')
            else:
                return HttpResponse('Login failed. Wrong username or password combination!')
    else:
        return HttpResponse('This is not a post call')

    

def log_out(request):
    logout(request) 
    return HttpResponseRedirect('/jobsmatch');



@login_required()
def profile(request):
    
    current_user = request.user
    profile_exist = True
    
    if request.method == 'POST':       
        form = ProfileForm(request.POST or None)       
        if form.is_valid():
            Profile.objects.create(user_id = current_user.id, summary = form.cleaned_data['summary'], skills = form.cleaned_data['skills'], certifications = form.cleaned_data['certifications'])
            return HttpResponseRedirect('/jobsmatch/profile');
    else:
        try:
            profile_exists = Profile.objects.get(user_id__exact=current_user.id)
        except Profile.DoesNotExist:
            profile_exist = False

        if profile_exist == True:     
            profile = Profile.objects.raw('SELECT * FROM jobsmatch_profile WHERE user_id = %s', [current_user.id])
            career = Career.objects.raw('SELECT * FROM jobsmatch_career WHERE user_id = %s', [current_user.id]);
            context = { 'profile' : profile, 'career' : career, 'current_user' : current_user}
            return render(request, 'jobsmatch/profile.html', context)
        else:      
            profile_form = ProfileForm()
            context = {'current_user' : current_user, 'form' : profile_form }
            return render(request, 'jobsmatch/create_profile.html', context) 