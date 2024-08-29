from django.shortcuts import render ,redirect
from tudu_app.models import *
from django.contrib.auth import logout 
from allauth.socialaccount.models import SocialAccount
from django.http import JsonResponse
from tudu_app.models import *

# Create your views here.
    
def home(request):

    uid = uname = lists = tasks = uname = None
    isg = 0

    if 'uid' not in request.session:
        if request.user.is_authenticated == False:
            return redirect('/login')
        if request.user.id == None:
            return redirect('/login')
    
    # Get uid of manully signed users
    if 'uid' in request.session:
        uid = request.session['uid']
        user_det = user_data.objects.filter(id=uid).get()
        uname = user_det.username
        isg = 0

    # Get uid of user that Signed up with google
    if request.user.id:
        google_user = str(request.user.id)
        user_obj = SocialAccount.objects.get(id=google_user,provider='google')
        request.session['guid'] = user_obj.id
        isg = 1

    if 'guid' in request.session:
        uid = request.session['guid']
        print(uid)
        uname = SocialAccount.objects.filter(uid=uid)

    form = task_form()
    if request.method == 'POST':
        form = task_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        uid = request.session['uid']
        


    tasks = tasks_data.objects.filter(added_by=uid,is_google=isg)
    lists = task_type_lists.objects.filter(added_by=uid,is_google=isg)
    user_tasks = tasks_data.objects.filter(added_by=uid,is_google=isg).count()
    # print("User total task : ",user_tasks)
    
    return render(request,'index.html',{'task_data':tasks,'list_data':lists,'uname_m':uname,'total_tasks':user_tasks,'form':form,'uid':uid})


# Login page
def login_page(request):

    alert = 0

    if 'uid' in request.session or 'guid' in request.session:
        return redirect('/')
    
    if 'login' in request.POST:
        f_em = request.POST['em']
        f_pass = request.POST['pss']
        if user_data.objects.filter(email=f_em,password=f_pass).exists():
            print('success')
            uid = user_data.objects.filter(email=f_em,password=f_pass).get()
            print(uid.id)
            request.session['uid'] = uid.id
            return redirect('/')
        else:
            alert=1

    return render(request,'login_page.html',{'email_pass_alert':alert})

# Register page
def register_page(request):

    uname_msg = email_msg = 0

    # Manually registration
    if 'register' in request.POST:

        uname = request.POST['un']
        f_email = request.POST['em']
        f_password = request.POST['pss']

        if user_data.objects.filter(username=uname,email=f_email).exists():
            uname_msg = 1
            email_msg = 1
        elif user_data.objects.filter(username=uname).exists():
            uname_msg = 1
        elif user_data.objects.filter(email=f_email).exists():
            email_msg = 1
        else:
            user_obj = user_data(username=uname,email=f_email,password=f_password)
            user_obj.save()
            
            # For session UID
            uid = user_data.objects.filter(username=uname)
            print(uid.id)
            request.session['uid'] = uid.id
            return redirect('/',{ 'uname_m':uname })

    return render(request,'register_page.html',{'uname_msg':uname_msg,'email_msg':email_msg})

# Logout
def logout_view(request):
    logout(request)
    del request.session
    return redirect('/login')