
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.views.generic import View
from django.template.loader import get_template

from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

import requests
from . models import u_reg
from . models import p_reg
from . models import cnews
from . models import food
from . models import medicine
from . models import doctor
from . models import FeedBackUser
from django.core.files.storage import FileSystemStorage
# Create your views here.

import json
import math, random
#email
from e_quarantine.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

def mainhome(request):
    pf = cnews.objects.filter()
    return render(request, "index1.html",{'pf':pf})
def statistics(request):
    data=True
    result = None
    states = None
    results = None
    globalSummary = None
    countries = None

    while(data):
        try:
            results =requests.get('https://api.covid19api.com/summary')
            globalSummary=results.json()['Global']
            countries = results.json()['Countries']
            result =requests.get('https://disease.sh/v3/covid-19/gov/India')
            
            states = result.json()['states']
            data=False
        except:
            data=True

    return render(request, "statistics.html",{'globalSummary' : globalSummary, 'countries':countries, 'states':states})    
def indexlogin1(request):
    return render(request, "indexlogin1.html")    
def reguser2(request):
    return render(request, "reguser2.html")  
def regpanchayat2(request):
    return render(request, "regpanchayat2.html") 
def foodorder(request):
    co = food.objects.filter()
    return render(request, "foodorder.html",{'co':co}) 
def medicineorder(request):
    co1 = medicine.objects.filter()
    return render(request, "medicineorder.html",{'co1':co1}) 
def vwdoctor(request):
    do = doctor.objects.filter()
    return render(request, "vwdoctor.html",{'do':do}) 
def userfoodorder(request,id):
    s=food.objects.get(id=id)
    return render(request, "userfoodorder.html",{'s':s}) 
def usermedorder(request,id):
    s2=medicine.objects.get(id=id)
    return render(request, "usermedorder.html", {'s2':s2})
def payment(request,id,uname):
    s1=food.objects.get(id=id,u_name=uname)
    return render(request, "payment.html",{'s1':s1})
def mpayment(request,id,uname):
    s11=medicine.objects.get(id=id,u_name=uname)
    return render(request, "payment1.html",{'s11':s11})
def phnotification(request,pname):
    n=food.objects.filter(status="ordered",pname=pname)
    m=medicine.objects.filter(status="ordered",pname=pname)
    
    post=[]
    com=[]
    com1=[]
    com2=[]
    com3=[]
    post1=[]
    com11=[]
    com12=[]
    com13=[]
    com14=[]
    for e in n:
        jid=e.id
        job=u_reg.objects.get(f_id=jid)
        name=job.fname
        # lname=job.lname
        post.append(name)
        # post.append(lname)
    for e1 in n:
        jid=e1.id    
        job=u_reg.objects.get(f_id=jid)
        hname=job.hname
        com.append(hname)
    for e2 in n:
        jid=e2.id    
        job=u_reg.objects.get(f_id=jid)
        place=job.place
        com1.append(place)
    for e3 in n:
        jid=e3.id    
        job=u_reg.objects.get(f_id=jid)
        mob=job.mob
        com2.append(mob)        
    for e4 in n:
        jid=e4.id    
        job=u_reg.objects.get(f_id=jid)
        id1=job.f_id
        com3.append(id1) 
    for e5 in m:
        jid=e5.id
        job=u_reg.objects.get(m_id=jid)
        name=job.fname
        # lname=job.lname
        post1.append(name)
        # post.append(lname)    
    for e6 in m:
        jid=e6.id    
        job=u_reg.objects.get(m_id=jid)
        hname=job.hname
        com11.append(hname)
    for e7 in m:
        jid=e7.id    
        job=u_reg.objects.get(m_id=jid)
        place=job.place
        com12.append(place)
    for e8 in m:
        jid=e8.id    
        job=u_reg.objects.get(m_id=jid)
        mob=job.mob
        com13.append(mob)        
    for e9 in m:
        jid=e9.id    
        job=u_reg.objects.get(m_id=jid)
        id2=job.m_id
        com14.append(id2)     
    return render(request, "phnotification.html",{'n':n,'post':post,'com':com,'com1':com1,'com2':com2,'com3':com3,'m':m,'post1':post1,'com11':com11,'com12':com12,'com13':com13,'com14':com14})       

    
     
def usetpwd(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        pass1 = request.POST['pswd1']
        pass2 = request.POST['pswd2']
        pass3 = request.POST['pswd3']
        user = auth.authenticate(username = uname, password = pass1)
        if user is not None:
            u = User.objects.get(username = uname)
            
        
            if pass2 == pass3:
                u.set_password(pass3)
                u.save()
                messages.info(request,'Your Password Changed ,Please Login')
                return render(request,'indexlogin1.html')
            else:
                messages.info(request,'Password Missmatch...')
                return redirect('usetpwd')
           
        else:
            messages.info(request,'Invalid Password...')
            return redirect('change_password')

    else:
        return render(request,'usetpwd.html')    
def phpwd(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        pass1 = request.POST['pswd1']
        pass2 = request.POST['pswd2']
        pass3 = request.POST['pswd3']
        user = auth.authenticate(username = uname, password = pass1)
        if user is not None:
            u = User.objects.get(username = uname)
            
        
            if pass2 == pass3:
                u.set_password(pass3)
                u.save()
                messages.info(request,'Your Password Changed ,Please Login')
                return render(request,'indexlogin1.html')
            else:
                messages.info(request,'Password Missmatch...')
                return redirect('usetpwd')
           
        else:
            messages.info(request,'Invalid Password...')
            return redirect('change_password')

    else:
        return render(request,'phpwd.html')    
        
def payment1(request,id,uname):
    if request.method == 'POST':
        unam= request.POST['unam']
        stat = request.POST['stat']
         
        pa1=food.objects.get(id=id)
        pa1.u_name=unam
        pa1.save()
        pa1.status=stat
        pa1.save()
        pa2=u_reg.objects.get(uname=uname)
        pa2.f_status=stat
        pa2.f_id=id
        pa2.save()
    return redirect('payment',id,uname) 
def payment2(request,id,uname):
    if request.method == 'POST':
        unam1= request.POST['unam1']
        stat1 = request.POST['stat1']
         
        pa2=medicine.objects.get(id=id)
        pa2.u_name=unam1
        pa2.save()
        pa2.status=stat1
        pa2.save()
        pa2=u_reg.objects.get(uname=uname)
        pa2.m_status=stat1
        pa2.m_id=id
        pa2.save()
       
    return redirect('mpayment',id,uname)     


def addfood1(request):   
    # sp = User.objects.filter(last_name="ph")
    return render (request,'addfood.html')
def addfood(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        sp = request.POST['sp']
        fitem = request.POST['fitem']
        
        fprice = request.POST['fprice']  
        fod=food(uname=uname,pname=sp,fitem=fitem,fprice=fprice,status="not ordered")
        fod.save()
        sp= User.objects.filter(last_name="ph")
    return render(request, "addfood.html") 
def addmedicine(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        sp = request.POST['sp']
        mname = request.POST['mname']
        quan=request.POST['quantity']
        mprice = request.POST['mprice']  
        med=medicine(uname=uname,pname=sp,mname=mname,mprice=mprice,status="not ordered",quantity=quan)
        med.save()
    return render(request, "addmedicine.html") 
def care(request):
    
    return render(request, "care.html")     
def care1(request):
    if request.method == 'POST':
        res=request.FILES.get('pi1',True)
        if res==False:
            pass
        else:
            fs=FileSystemStorage()
            fs.save(res.name, res)
        sp = request.POST['sp']
        dname = request.POST['dname']
        ddep= request.POST['ddep']
        dmob = request.POST['dmob']  
        dep=doctor(pname=sp,dname=dname,ddep=ddep,dmob=dmob,img=res)
        dep.save()
    return render(request, "care.html") 
def phome(request):
    pf1 = cnews.objects.filter()
    # h = u_reg.objects.filter()
    
    return render(request, "phome.html",{'pf1':pf1})    
def confirmuser(request,pname):
    h = u_reg.objects.filter(status="1",pname=pname)
    return render(request, "confirmuser.html",{'h':h})
def deleteuser(request,uname):
    d=u_reg.objects.get(uname=uname)
    d.status = 0
    d.save()
    u=User.objects.get(username=uname)
    u.is_active = False
    u.save()
    messages.success(request,'Rejected one user ')
    return redirect('phome')           
def uhome(request):
    pf11 = cnews.objects.filter()
    return render(request, "uhome.html", {'pf11':pf11})   
def viewnotification(request):
    fcount = u_reg.objects.filter(f_status="ordered").count()
    mcount = u_reg.objects.filter(f_status="ordered").count()
    tcount=fcount+mcount
   

    return render(request, "phome.html" ,{'tcount':tcount})      
def indexadmin(request):
    ucount = u_reg.objects.filter().count()
    spcount = p_reg.objects.filter().count()
    dcount = food.objects.filter().count()
    mcount = medicine.objects.filter().count()

    return render(request, "indexadmin.html" ,{'ucount':ucount,'spcount':spcount,'dcount':dcount,'mcount':mcount})  
def news(request):
    pp = cnews.objects.filter()
    return render(request, "news.html" ,{'pp':pp})  
def logout(request):
    return redirect('mainhome')     
def adminco1(request):
     if request.method == 'POST':
        ctotal1 = request.POST['ctotal']
        cactive1 = request.POST['cactive']
        cured1 = request.POST['cured']  
        death1 = request.POST['death']

        ind = request.POST['ind']
        inda = request.POST['inda']
        indr = request.POST['indr']
        indt = request.POST['indt']
        wl = request.POST['wl']
        wla = request.POST['wla']
        wlr = request.POST['wlr'] 
        wld = request.POST['wld'] 
        # cov=cnews(ctotal=ctotal,cactive=cactive,cured=cured,death=death)
        # cov.save()
        # return render(request,'news.html')

       
        pp=cnews.objects.get()
        pp.ctotal=ctotal1
        pp.save()
        pp.cactive=cactive1
        pp.save()
        pp.cured=cured1
        pp.save()
        pp.death=death1
        pp.save()

        pp.india=ind
        pp.save()
        pp.i_active=inda
        pp.i_recoverd=indr
        pp.save()
        pp.i_death=indt
        pp.save()
        pp.world=wl
        pp.save()
        pp.w_active=wla
        pp.save()
        pp.w_recoverd=wlr
        pp.save()
        pp.w_death=wld
        pp.save()
        
        return redirect( '/news')
     else:
        return render(request,'news.html')       
def admvwfood2(request):
    a = food.objects.filter() 
    return render(request, "admvwfood2.html",{'a':a}) 
def admvwmedicine(request):
    m = medicine.objects.filter() 
    return render(request, "admvwmedicine.html",{'m':m})           
def admvwuser(request):
    # i = u_reg.objects.filter(status="1")
    s = u_reg.objects.filter()
    return render(request, "admvwuser.html" ,{'s':s})   
def admvwph(request):
    i = p_reg.objects.filter(status="1")
    return render(request, "admvwph.html",{'i':i})
def deleteph(request,uname):
    d=p_reg.objects.get(uname=uname)
    d.status = 0
    d.save()
    u=User.objects.get(username=uname)
    u.is_active = False
    u.save()
    return redirect('admvwph')  
def deletefood(request,uname,pname):
    
    j = food.objects.filter(uname=uname,pname=pname)
    
    return render(request,'deletefood.html',{'j':j})   
def deletefood1(request,id):
    cc=food.objects.get(id=id)
    
    cc.delete()
    messages.success(request,'One item deleted ')
    return redirect( 'addfood')
def deletemedicine(request,uname,pname):
    j1 = medicine.objects.filter(uname=uname,pname=pname)
    return render(request,'deletemedicine.html',{'j1':j1})
def deletemedicine1(request,id):
    cc1=medicine.objects.get(id=id)
    
    cc1.delete()
    messages.success(request,'One item deleted ')
    return redirect( 'addmedicine')                   
def signupp(request):
   if request.method == 'POST':
        fname = request.POST['fname']
        lname=request.POST['lname']
        mob=request.POST['mob']
        hname = request.POST['hname']
        place = request.POST['place']
        district = request.POST['district']
        state = request.POST['state']
        pin = request.POST['pin']
        pname = request.POST['pname']
        uname = request.POST['uname']
        pwd= request.POST['pwd']
        pwd1 = request.POST['pwd1']
        if(pwd == pwd1):
            if User.objects.filter(username=uname).exists():                                                                 
                messages.info(request,'Username already exist')
                return render(request, 'reguser2.html') 
            user = User.objects.create_user(username=uname, password=pwd, email=uname, first_name=fname, last_name=lname)
            user.save()
            usr=u_reg(fname=fname,lname=lname,mob=mob,hname=hname,place=place,district=district,state=state,pin=pin,pname=pname.lower(),uname=uname,status='1',f_status="null",m_status="null",f_id='0',m_id='0')
            usr.save()
            return render(request, 'indexlogin1.html') 
        else: 
            messages.info(request,'Password Missmatch')
            return render(request, 'reguser2.html')
         
   else:
        return render(request, 'reguser2.html') 

def signupph(request):
   if request.method == 'POST':
        state = request.POST['state']
        district=request.POST['district']
        pname = request.POST['pname']
        cperson = request.POST['cperson']
        mob=request.POST['mob']
        uname=request.POST['uname']
        pwdd= request.POST['pwdd']
        pwdd1 = request.POST['pwdd1']
        if(pwdd == pwdd1):
            if User.objects.filter(username=uname).exists():                                                                 
                messages.info(request,'Username already exist')
                return render(request, 'regpanchayat2.html') 
            user = User.objects.create_user(username=uname, password=pwdd, email=uname, first_name=pname.lower(), last_name="ph")
            user.save()    
            phr=p_reg(state=state,district=district,pname=pname.lower(),cperson=cperson,mob=mob,uname=uname,status='1')
            phr.save()
            
            return render(request, 'indexlogin1.html') 
        else: 
            messages.info(request,'Password Missmatch')
            return render(request, 'regpanchayat2.html')
         
   else:
        return render(request, 'regpanchayat2.html')          


def logincheck(request):
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['pswd']
        if u_reg.objects.filter(uname=username).exists():
            usr=u_reg.objects.get(uname=username)
            if usr.status == 1:
                  user = auth.authenticate(username=username, password=password)
                  if user is not None:
                     auth.login(request, user) 
                     if User.objects.filter(last_name="ph",username=username).exists():
                        
                        return redirect('phome') 
                     else:    
                         return redirect('uhome')
                          
                  else:
                      
                      messages.info(request, 'Invalid username/password')
                      return render(request, 'indexlogin1.html')
            else:
                messages.info(request,'Your account is deactivated')    
                return render(request, 'indexlogin1.html')
        elif p_reg.objects.filter(uname=username).exists():
             phr=p_reg.objects.get(uname=username)
             if phr.status == 1:
                 user = auth.authenticate(username=username, password=password)
                 if user is not None:
                     auth.login(request, user) 
                     if User.objects.filter(last_name="ph",username=username).exists():
                        return redirect('phome')
                     else:
                         return redirect('uhome')
                 else:
                     messages.info(request, 'Invalid username/password')
                     return render(request, 'indexlogin1.html')
             else:
                 messages.info(request,'Your account is deactivated')    
                 return render(request, 'indexlogin1.html')
        else: 
             user = auth.authenticate(username=username, password=password)
             if user is not None:
                auth.login(request, user)
                return redirect('indexadmin')
             else:
                 messages.info(request, 'Invalid username/password')
                 return render(request, 'indexlogin1.html')
    else:             
        return render(request, 'indexlogin1.html')
                        
def forgotpass(request):
    if request.method=="POST":
        p=OTPgenerator()
        global otp
        global omail
        
        otp=p
        # request.session['otp']=p
        mailAddr=request.POST.get('email')
        
        if u_reg.objects.filter(uname=mailAddr).exists():
            # request.session['omail']=mailAddr
            omail=mailAddr
            sendOtpToMAil(mailAddr, p)
            return redirect("http://localhost:8000/cpass")
        else:
            messages.error(request,"Not a Registered User")
        
    return render(request, "forget-pass.html")

def otp_pass(request):
   
    if request.method=="POST":
        j=request.POST.get('cpass')
        o=request.POST.get('onetp')
        print(j,o)
        if(o==otp):
            # print("\n\nNADAKKOOOLLAAAAa")
            u=User.objects.get(username =omail)
            # print(u)
            u.set_password(j)
            u.save()

            return redirect("http://localhost:8000/indexlogin1/")
        else:
            messages.error(request,"Please Enter a Valid OTP")
        
    return render(request, "cpass.html")

def OTPgenerator():
    digits_in_otp = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    OTP = ""
    length = len(digits_in_otp)
    for i in range(6):
        OTP += digits_in_otp[math.floor(random.random() * length)]

    print("\nOTP: ",OTP)

    return OTP

def sendOtpToMAil(mailAddr, otp):
    subject = 'EQS - OTP for Changing Password'
    message = 'Hello,\n The One Time Password(OTP) for changing the Password of your account is : '+ str(otp)
    
    mailAddr = str(mailAddr)
    recepient = str(mailAddr)
    send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently=False)


def userfeedback(request):
    
    feedback_data=FeedBackUser.objects.all()
    return render(request,"user_feedback_template.html",{"feedback_data":feedback_data})

def user_feedback_save(request):
    if request.method!="POST":
        return HttpResponseRedirect(reverse("userfeedback"))
    else:
        feedback_msg=request.POST.get("feedback_msg")

        # user_obj=u_reg.objects.get(id=request.user.id)
        try:
            feedback=FeedBackUser( feedback=feedback_msg,feedback_reply="")
            feedback.save()
            messages.success(request, "Successfully Sent Feedback")
            return HttpResponseRedirect(reverse("userfeedback"))
        except:
            messages.error(request, "Failed To Send Feedback")
            return HttpResponseRedirect(reverse("userfeedback"))

def user_feedback_message(request):
    feedbacks=FeedBackUser.objects.all()
    return render(request,"phuser_feedback_template.html",{"feedbacks":feedbacks})

@csrf_exempt
def user_feedback_message_replied(request):
    feedback_id=request.POST.get("id")
    feedback_message=request.POST.get("message")

    try:
        feedback=FeedBackUser.objects.get(id=feedback_id)
        feedback.feedback_reply=feedback_message
        feedback.save()
        return HttpResponse("True")
    except:
        return HttpResponse("False")

                        