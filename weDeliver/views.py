
from django.shortcuts import render,redirect
from django.http import  HttpResponse
from django.contrib import messages
from .models import Products,User
import random
from ecom.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.db.utils import IntegrityError
from django.core.paginator import Paginator
nm = ''
con = ''
ml = ''
ps = ''
st= ''
otp = 0

def home(request):
    # pr =  Products.objects.all()
    # return render(request,'home.html',{'prods':pr})
    v= request.COOKIES
    m = len(v)-1
    pr = Products.objects.all()
    pg = Paginator(pr,3)
    page_no = request.GET.get('page_no',1)
    page = pg.page(page_no)
    return render(request,'home.html',{'data':page, 'mycart':m})

def adlog(request):
    return render(request, 'admin_login.html')

def adchk(request):
    un = request.POST.get('user')
    pw = request.POST.get('pass')

    if un == 'manthan' and pw == 'manthan':
        return redirect('admin')
    else:
        messages.error(request, 'Invalid Credentials')
        return redirect('adlog')

def adminhome(request):
    return render(request,'admin_home.html')

def addprod(request):
    res=Products.objects.all()
    return render(request,'addproducts.html',{'prods':res})

def prods(request):
    md = request.POST.get('model')
    br = request.POST.get('brnd')
    dsc = request.POST.get('desc')
    pr = request.POST.get('price')
    qty = request.POST.get('qtty')
    ph = request.FILES['photo']
    st = 'active'

    messages.success(request,'Your product added Successfully.')
    Products(modelNo=md,brand=br,desc=dsc,price=pr,quatity=qty,photo=ph,status=st).save()
    return redirect('add_prod')

def reg(request):
    return render(request,'register.html')

def regis(request):
    global nm,con,ml,ps,st
    nm = request.POST.get('name')
    con = request.POST.get('no')
    ml = request.POST.get('email')
    ps = request.POST.get('pass')
    st = 'Pending'
    crt = request.COOKIES
    m = len(crt) - 1
    if User.objects.filter(email__exact=ml).count()==0 and User.objects.filter(number__exact=con).count()==0:
        rnd = random.randint(100000,999999)
        global otp
        otp = rnd
        recipient = ml
        subject = 'We\Deliver New Account, Your Verification Code for Registering New Account'
        message = '''
        Hi,


        Greetings!


        You are just a step away from Registering your We\Deliver account
        
        
        We are sharing a verification code to create your account. The code is valid for 10 minutes and usable only once.
        
        
        Once you have verified the code, you'll be able to login to your account, after your request is approved by Admin.
        
        
        This is to ensure that only you have access to your account.
        
        
        Your OTP: ''' + str(otp)

        '''Expires in: 10 minutes
        
        Best Regards,
        Team We\Deliver'''

        send_mail(subject,message,EMAIL_HOST_USER,[recipient],fail_silently=False)
        return redirect('otppage')
    else:
        messages.error(request, 'Email or Number is Already Registered')
        return redirect('userreg')

    # try:
    #     User(name=nm, number=con, email=ml, password=ps, status=st).save()
    #     return redirect('uslog')
    # except IntegrityError:
    #     messages.error(request, 'Email or Number is Already Registered')
    #     return redirect('userreg')
    # qs =  User.objects.filter(email__exact=ml)
    # print(qs)
    # if qs != '<QuerySet []>':
    #     messages.error(request, 'Email or Number is Already Registered')
    #     return redirect('userreg')
    # else:
    #     rand = random.randint(100000,999999)
    #     global otp
    #     otp = rand
    #     subject = 'Welcome to we\Deliver Shopping'
    #     message = 'Your one time password for Registration in We\Deliver is : ' + str(otp)
    #     print(message)
    #     recepient = ml
    #     send_mail(subject,
    #               message, EMAIL_HOST_USER, [recepient], fail_silently=False)
    #     return render(request, 'otpvalidate.html', {'recepient': recepient})


def showpndng(request):
    # res = User.objects.filter(status__in=['Pending']).order_by('-id')
    # return render(request, 'pending.html', {'user': res})
    var = User.objects.filter(status__in=['Pending']).order_by('-id')
    res = Paginator(var,6)
    pn = request.GET.get('page',1)
    page = res.page(pn)
    return render(request,'pending.html',{'pages':page})


def uslog(request):
    v = request.COOKIES
    m = len(v)-1
    return render(request, 'userlog.html',{'mycart':m})

def userchk(request):
    un = request.POST.get('user')
    pw = request.POST.get('pass')
    v = User.objects.filter(number__in=[un])
    for x in v:
        if pw == x.password:
            if x.status=='Approved':
                return redirect('userhome')
            elif x.status=='Declined':
                messages.error(request,'Your Registration Request Is Declined By Admin. Please Register Again.')
                return redirect('uslog')
            else:
                messages.error(request, 'Your Registration Request Not Yet Approved. Please Come Back Later.')
                return redirect('uslog')

    messages.error(request, 'Invalid Login Details')
    return redirect('uslog')

def userhome(request):
    data = Products.objects.all()
    v = request.COOKIES
    m = len(v)-1
    return render(request,'userhome.html',{'prods':data,'mycart':m})


def allprods(request):
    res = Products.objects.all().order_by('-prodId')
    return render(request,'allproducts.html',{'all':res})

def update(request):
    idn = request.GET.get('id')
    res = Products.objects.get(prodId=idn)
    return render(request,'update.html',{'data':res})

def upprod(request):
    pi = request.POST.get('id')
    mdl = request.POST.get('model')
    br = request.POST.get('brnd')
    pr = request.POST.get('price')
    qt = request.POST.get('qtty')
    ds =request.POST.get('desc')
    pc =request.FILES['pic']
    Products.objects.filter(prodId=pi).update(modelNo=mdl,brand=br,price=pr,quatity=qt,desc=ds,photo=pc)
    return redirect('allprods')

def uslogem(request):
    v = request.COOKIES
    m = len(v)-1
    return render(request,'userlogem.html',{'mycart':m})


def userchkem(request):
    un = request.POST.get('user')
    pw = request.POST.get('pass')
    v = User.objects.filter(email__in=[un]).all()
    for x in v:
        if pw == x.password:
            if x.status=='Approved':
                return redirect('userhome')
            elif x.status=='Declined':
                messages.error(request,'Your Registration Request Is Declined By Admin. Please Register Again.')
                return redirect('uslogem')
            else:
                messages.error(request, 'Your Registration Request Not Yet Approved. Please login after some time.')
                return redirect('uslogem')
    messages.error(request, 'Invalid Username and Password.')
    return redirect('uslogem')


def delprod(request):
    pi = request.GET.get('id')
    Products.objects.filter(prodId=pi).delete()
    return redirect('allprods')


def picupdate(request):
    pi = request.GET.get('id')
    print(pi)
    res = Products.objects.get(prodId__exact=pi)
    Products.objects.filter(prodId=pi).update(photo=None)
    return render(request,'photo_update.html',{'data':res})


def upphoto(request):
    pi = request.POST.get('id')
    pc = request.FILES['photo']
    Products.objects.filter(prodId=pi).update(photo=pc)
    return None

def appruser(request):
    ui = request.GET.get('id')
    User.objects.filter(id=ui).update(status='Approved')
    return redirect('showpndg')

def declineuser(request):
    ui = request.GET.get('id')
    User.objects.filter(id=ui).update(status='Declined')
    return redirect('showpndg')

def showapprd(request):
    # res = User.objects.filter(status__in=['Approved']).order_by('-id')
    # return render(request,'approved_users.html',{'app':res})
    res = User.objects.filter(status__in=['Approved']).order_by('-id')
    objs = Paginator(res,6)
    pa = request.GET.get('page',1)
    page = objs.page(pa)
    return render(request,'approved_users.html',{'app':page})

def dclndusers(request):
    res = User.objects.filter(status__in=['Declined']).order_by('-id')
    # if res:
    return render(request,'declined_users.html',{'dec':res})
    # else:
    #     return render(request,'declined_users.html',{'dec':'You have no declined users'})

def deletedecuser(request):
    req = request.GET.get('id')
    User.objects.filter(id=req).delete()
    return redirect('showdclnd')

def delpdnguser(request):
    ui = request.GET.get('id')
    User.objects.filter(id=ui).delete()
    return redirect('showpndg')

def delappuser(request):
    ui= request.GET.get('id')
    User.objects.filter(id=ui).delete()
    return redirect('showapprd')

def apprdlcnd(request):
    ui = request.GET.get('id')
    User.objects.filter(id=ui).update(status='Approved')
    return redirect('showdclnd')


def cart(request):
    k = request.GET.get('id')
    v = request.GET.get('model')
    pr = request.GET.get('price')
    response= redirect('home')
    response.set_cookie(k,v)
    return response

def cartitems(request):
    v = request.COOKIES
    if len(v)==1:
        messages.error(request,'Your cart is Empty. ')
    m = len(v)-1
    return render(request,'cartitems.html',{'cart':request.COOKIES, 'mycart':m})


def delcart(request):
    mc = request.GET.get('id')
    response = redirect('cartitems')
    response.set_cookie(mc,max_age=0)
    return response


def usercart(request):
    v = request.COOKIES
    m = len(v)-1
    if len(v)==1:
        messages.error(request, 'Your cart is Empty. ')
    return render(request,'usercart.html',{'cart':request.COOKIES, 'mycart':m})


def useritems(request):
    itn = request.GET.get('id')
    mdl =  request.GET.get('model')
    pr = request.GET.get('price')
    response = redirect('usercart')
    response.set_cookie(itn,mdl)
    # response.set_cookie(itn,pr)
    return response

def delusercart(request):
    mc = request.GET.get('id')
    response = redirect('usercart')
    response.set_cookie(mc, max_age=0)
    return response


def forgotpass(request):
    return render(request,'forgotpass.html')


def otppage(request):
    return render(request,'otpvalidate.html')


def otpvalidate(request):
    usrotp = eval(request.POST.get('otp'))
    if usrotp==otp:
        User(name=nm,number=con,email=ml,password=ps,status=st).save()
        return redirect('uslog')
    else:
        messages.error(request,'Invalid OTP. Try Again')
        return redirect('otppage')