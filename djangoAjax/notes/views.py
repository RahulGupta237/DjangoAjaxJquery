from turtle import title
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import ContactForm,LoginForm,NoteForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Note
from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse

# Create your views here.
@csrf_protect
def Index(request):
    #return HttpResponse("Hellow Kelltontech")
    #form=NoteForm()
    
    if request.user.is_authenticated:
        form=NoteForm()
        data_retrieve_from_noteform=Note.objects.filter(user=request.user)
        data={
            "form":form,
            "data_retrieve_frm_database":data_retrieve_from_noteform
        }
        
        if request.method=="POST":
           
            title=request.POST.get('title')
            description=request.POST.get('description')
            
            print(type(title),title,description)
            note=Note()
            note.title=title
            note.description=description
            note.user=request.user
            note.save()
            print("Successfully save in database")
        return render(request,"notes/index.html",context=data)
    else:
        return redirect('Login')
        #return render(request,"notes/index.html",context=data)
        pass

@csrf_protect
def Signup(request):
    #return HttpResponse("Hellow Kelltontech")
    form=ContactForm()
    if request.method=="POST":
        form=ContactForm(request.POST)
        name=request.POST.get("name")
        email=request.POST.get("email")
        username=request.POST.get("user_name")
        password=request.POST.get("password")
        repassword=request.POST.get("repassword")
        print("--->",name,username,email,password,repassword)
        if password!=repassword:
             messages.error(request, 'Password do not match.')

        else:
            user=User.objects.create_user(username=username,email=email,password=password,last_name=name)
            if user.is_active:
                print("Rahul successfully register")
                messages.success(request, 'User Sucessfully Created.')
                return redirect("Login")
            else:
                print("error")
    return render(request,"notes/signup.html",context={"form":form})

@csrf_protect
def LoginUser(request):
    loginform=LoginForm()
    data={
        "loginForm":loginform
    }
    if request.method=="POST":
        #form=loginform(request.POST)
        username=request.POST.get("username")
        password=request.POST.get("password")
        try:
            user=authenticate(request,username=username,password=password)
        except:
            messages.error(request, f'invalide credential for {username} or {password}')

        if user is not None:
            login(request,user)
            print("heloow iam working authenticate username",user)
            #messages.success(request, f'Successfully login {user}')
            #return render(request,"notes/index.html")
            return redirect('Home')
        else:
              messages.error(request, f'invalide credential for {username} or {password}')
            
        
        print("--->",username,password)
    return render(request,"notes/login.html",context=data)

def Logoutuser(request):
    logout(request)
    return redirect("Login")


def delete_note(request):
    del_note=request.GET.get(id)
    print(delete_note)

