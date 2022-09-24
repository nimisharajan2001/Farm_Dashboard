from tkinter.tix import FileEntry
from unicodedata import name
from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import auth, User
from django.contrib.auth import authenticate
from django. contrib import messages
from datetime import datetime,date
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    return render(request,'index.html')

def Reg(request):
    return render(request,'Registration.html')


#**********Registration**********

def registration(request):
    if request.method == 'POST':
        reg = register()
        reg.name = request.POST['name']
        reg.username = request.POST['username']
        reg.mobile = request.POST['mobile']
        reg.email = request.POST['email']
        reg.address = request.POST['address']
        reg.password = request.POST['password']
        reg.cpassword = request.POST['cpassword']
        reg.pin = request.POST['pin']
        reg.district = request.POST['district']
        reg.save()
        msg_success = "Registered successfully"
        m = "Registered successfully"
        return redirect('log')
        # return render(request, 'Registration.html', {'msg_success': msg_success,'m':m})
    return render(request,'Login.html')

#**********Login**********

def log(request):
    client = designation.objects.get(designation="Client")
    staff = designation.objects.get(designation="Staff")
    Admin = designation.objects.get(designation="Admin")
    if request.method == 'POST':       
        # username  = request.POST['username']
        email  = request.POST['email']
        password = request.POST['password']
        # user = authenticate(username=username,password=password)
        # if user is not None:
        #     request.session['SAdm_id'] = user.id
        #     return redirect( 'Admin_Dashboard')
        if register.objects.filter(email=request.POST['email'], password=request.POST['password'],designation=Admin.id).exists():
                member=register.objects.get(email=request.POST['email'], password=request.POST['password'])
                request.session['SAdm_id'] = member.designation_id
                request.session['usernamets1'] = member.username
                request.session['SAdm_id'] = member.id
                mem=register.objects.filter(id= member.id)
                # return render(request,'user_dashboard.html',{'mem':mem})
                return redirect('Admin_Dashboard')

        elif register.objects.filter(email=request.POST['email'], password=request.POST['password'],designation=client.id).exists():
                member=register.objects.get(email=request.POST['email'], password=request.POST['password'])
                request.session['c_id'] = member.designation_id
                request.session['usernamets1'] = member.username
                request.session['c_id'] = member.id
                mem=register.objects.filter(id= member.id)
                # return render(request,'user_dashboard.html',{'mem':mem})
                return redirect('user_dashboard')

        elif register.objects.filter(email=request.POST['email'], password=request.POST['password'],designation=staff.id).exists():
                member=register.objects.get(email=request.POST['email'], password=request.POST['password'])
                request.session['s_id'] = member.designation_id
                request.session['usernamets1'] = member.username
                request.session['s_id'] = member.id
                mem1=register.objects.filter(id= member.id)
                # return render(request,'committee_viewworkorder.html',{'mem1':mem1})
                return redirect('Staff_dashboard')
        else:
            context = {'msg_error': 'Invalid data'}
            return render(request, 'Login.html', context)
    return render(request,'Login.html')


#------------------------ADMIN----------------------------
def Admin_index(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        user = register.objects.filter(id=SAdm_id)
        return render(request,'Admin_index.html',{'user':user})
    else:
        return redirect('/')

def Admin_Dashboard(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        user = register.objects.filter(id=SAdm_id)
        return render(request,'Admin_Dashboard.html',{'user':user})
    else:
        return redirect('/')

def Admin_Settings(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        user = register.objects.filter(id=SAdm_id)
        return render(request,'Admin_Settings.html',{'user':user})
    else:
        return redirect('/')

def Admin_clients(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        user = register.objects.filter(id=SAdm_id)
        desig = designation.objects.get(designation='Client')
        var= register.objects.filter(designation=desig).order_by('-id')
        return render(request,'Admin_clients.html',{'var':var,'user':user})
    else:
        return redirect('/')

def Admin_clientdashboard(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        user = register.objects.filter(id=SAdm_id)
        var= register.objects.filter(id=id)
        labels = []
        data = []
        queryset = farm_expenses.objects.filter(user_id=id)
        for j in queryset:
            labels=[j.price,j.total_cost,j.quantity]
            data=[j.price,j.total_cost,j.quantity]
        return render(request,'Admin_clientdashboard.html',{'var':var,'user':user,'labels':labels,'data':data})
    else:
        return redirect('/')


def Admin_client_chart(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=SAdm_id)
        var = register.objects.filter(id = id)
        labels = []
        data = []
        queryset = farm_revenue.objects.filter(user_id=id)
        for j in queryset:
            labels=[j.quantity,j.revenue]
            data=[j.quantity,j.revenue]
        return render(request,'Admin_clientchart.html',{'mem1':mem1,'var':var,'labels':labels,'data':data})
    else:
        return redirect('/')


def Admin_staffs(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        user = register.objects.filter(id=SAdm_id)
        desig = designation.objects.get(designation='Staff')
        var= register.objects.filter(designation=desig).order_by('-id')
        return render(request,'Admin_staffs.html',{'var':var,'user':user})
    else:
        return redirect('/')

def Admin_staffdashboard(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        user = register.objects.filter(id=SAdm_id)
        var= register.objects.filter(id=id)
        labels = []
        data = []
        queryset = farm_expenses.objects.filter(user_id=id)
        for j in queryset:
            labels=[j.price,j.total_cost,j.quantity]
            data=[j.price,j.total_cost,j.quantity]
        return render(request,'Admin_staffdashboard.html',{'var':var,'user':user,'labels':labels,'data':data})
    else:
        return redirect('/')

def Admin_Staff_chart(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        user = register.objects.filter(id=SAdm_id)
        var = register.objects.filter(id = id)
        labels = []
        data = []
        queryset = farm_revenue.objects.filter(user_id=id)
        for j in queryset:
            labels=[j.quantity,j.revenue]
            data=[j.quantity,j.revenue]
        return render(request,'Admin_Staffchart.html',{'user':user,'var':var,'labels':labels,'data':data})
    else:
        return redirect('/')


def Admin_registration_details(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        user = register.objects.filter(id=SAdm_id)
        des = designation.objects.all()
        var = register.objects.all().order_by('-id')
        desig = designation.objects.get(designation='Staff')
        st= register.objects.filter(designation=desig)
        return render(request,'Admin_registration_details.html',{'var':var,'des':des,'st':st,'user':user})
    else:
        return redirect('/')

def registersave(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = register.objects.filter(id=SAdm_id)
        user = register.objects.get(id=id)
        if request.method == 'POST':
            user.designation_id = request.POST.get('designation')
            user.team = request.POST.get("team")
            user.date = datetime.now()
            user.save()
            msg_success = "Registered successfully"
        return render(request,'Admin_registration_details.html',{'user':user,'msg_success':msg_success,'users':users})
    else:
        return redirect('/')

def Admin_plant_details(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        user = register.objects.filter(id=SAdm_id)
        var = plantdetails.objects.all().order_by('-id')
        return render(request,'Admin_plant_details.html',{'var':var,'user':user})
    else:
        return redirect('/')


def Admin_excel(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        user = register.objects.filter(id=SAdm_id)
        var = farm_expenses.objects.all().order_by('-id')
        return render(request,'Admin_expense_excel.html',{'var':var,'user':user})
    else:
        return redirect('/')

def Admin_farm_weather(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        user = register.objects.filter(id=SAdm_id)
        var = farm_weather.objects.all().order_by('-id')
        return render(request,'Admin_farm_weather.html',{'var':var,'user':user})
    else:
        return redirect('/')

def Admin_find_weather(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        user = register.objects.filter(id=SAdm_id)
        var = farm_weather.objects.values('user').distinct()
        num = register.objects.all()
        return render(request,'Admin_find_weather.html',{'user':user,'var':var,'num':num})
    else:
        return redirect('/')

def Admin_weather(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        user = register.objects.filter(id=SAdm_id)
        if request.method == "POST":
            fromdate = request.POST.get('startdate')
            todate = request.POST.get('enddate')
            p1=request.POST.get('parameter')
            n1=request.POST.get('name')
            var = farm_weather.objects.filter(date__range=[fromdate, todate]).filter(user_id=n1).filter(parameters=p1)
        return render(request,'Admin_weather.html',{'user':user,'var':var})
    else:
        return redirect('/')

def Admin_soil_sample_test(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        user = register.objects.filter(id=SAdm_id)
        var = soil_sample_test.objects.all().order_by('-id')
        return render(request,'Admin_soil_sample_test.html',{'var':var,'user':user})
    else:
        return redirect('/')

def Admin_fertilizer_applications(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        user = register.objects.filter(id=SAdm_id)
        var = fertilizer_applications.objects.all().order_by('-id')
        return render(request,'Admin_fertilizer_applications.html',{'var':var,'user':user})
    else:
        return redirect('/')

def Admin_periodic_tests(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        user = register.objects.filter(id=SAdm_id)
        var = periodic_tests.objects.all().order_by('-id')
        return render(request,'Admin_periodic_tests.html',{'var':var,'user':user})
    else:
        return redirect('/')

def Admin_farm_machineries(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        user = register.objects.filter(id=SAdm_id)
        var = farm_machineries.objects.all().order_by('-id')
        return render(request,'Admin_farm_machineries.html',{'var':var,'user':user})
    else:
        return redirect('/')

def Admin_man_power_usage(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        user = register.objects.filter(id=SAdm_id)
        var = man_power_usage.objects.all().order_by('-id')
        return render(request,'Admin_man_power_usage.html',{'var':var,'user':user})
    else:
        return redirect('/')

def Admin_farm_expenses(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        user = register.objects.filter(id=SAdm_id)
        var = farm_expenses.objects.all().order_by('-id')
        return render(request,'Admin_farm_expenses.html',{'var':var,'user':user})
    else:
        return redirect('/')

def Admin_find_expense(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        user = register.objects.filter(id=SAdm_id)
        var = farm_expenses.objects.values('user').distinct()
        num = register.objects.all()
        return render(request,'Admin_find_expense.html',{'user':user,'var':var,'num':num})
    else:
        return redirect('/')

def Admin_expense(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        user = register.objects.filter(id=SAdm_id)
        if request.method == "POST":
            fromdate = request.POST.get('startdate')
            todate = request.POST.get('enddate')
            n1=request.POST.get('name')
            var = farm_expenses.objects.filter(date__range=[fromdate, todate]).filter(user_id=n1)
        return render(request,'Admin_expense.html',{'user':user,'var':var})
    else:
        return redirect('/')


def Admin_farm_revenue(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        user = register.objects.filter(id=SAdm_id)
        var = farm_revenue.objects.all().order_by('-id')
        return render(request,'Admin_farm_revenue.html',{'var':var,'user':user})
    else:
        return redirect('/')

def Admin_find_revenue(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        user = register.objects.filter(id=SAdm_id)
        var = farm_revenue.objects.values('user').distinct()
        num = register.objects.all()
        return render(request,'Admin_find_revenue.html',{'user':user,'var':var,'num':num})
    else:
        return redirect('/')

def Admin_revenue(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        user = register.objects.filter(id=SAdm_id)
        if request.method == "POST":
            fromdate = request.POST.get('startdate')
            todate = request.POST.get('enddate')
            n1=request.POST.get('name')
            var = farm_revenue.objects.filter(date__range=[fromdate, todate]).filter(user_id=n1)
        return render(request,'Admin_revenue.html',{'user':user,'var':var})
    else:
        return redirect('/')


def logout_admin(request):
    if 'SAdm_id' in request.session:
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/')

#------------------------USER----------------------------

def user_index(request):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=c_id)
        return render(request,'user_index.html',{'mem1':mem1})
    else:
        return redirect('/')

# def user_index(request):
#     if 'c_id' in request.session:
#         if request.session.has_key('c_id'):
#             c_id = request.session['c_id']
#         else:
#             return redirect('/')
#         mem1 = register.objects.filter(id=c_id)
#         return render(request,'user_index.html',{'mem1':mem1})

def user_dashboard(request):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=c_id)
        var = register.objects.filter(id=c_id)
        labels = []
        data = []
        queryset = farm_expenses.objects.filter(user_id=c_id)
        for j in queryset:
            labels=[j.price,j.total_cost,j.quantity]
            data=[j.price,j.total_cost,j.quantity]
        return render(request,'user_dashboard.html',{'mem1':mem1,'var':var,'labels':labels,'data':data})
    else:
        return redirect('/')

@csrf_exempt
def user_chart(request):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=c_id)
        var = register.objects.filter(id = c_id)
        labels = []
        data = []
        queryset = farm_revenue.objects.filter(user_id=c_id)
        for j in queryset:
            labels=[j.quantity,j.revenue]
            data=[j.quantity,j.revenue]
        return render(request,'user_chart.html',{'mem1':mem1,'var':var,'labels':labels,'data':data})
    else:
        return redirect('/')


def user_settings(request):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=c_id)
        mem = register.objects.filter(id = c_id)
        if request.method == 'POST':
            abc = register.objects.get(id=c_id)
            abc.name = request.POST.get('name')
            abc.username= request.POST.get('uname')
            abc.mobile = request.POST.get('mobile')
            abc.email = request.POST.get('email')
            abc.address = request.POST.get('address')
            abc.date = request.POST.get('date')
            abc.pin = request.POST.get('pin')
            abc.district = request.POST.get('district')
            abc.save()
            msg_success = "Details changed successfully"
            return render(request, 'user_settings.html', {'msg_success': msg_success})
        return render(request,'user_settings.html',{'mem':mem,'mem1':mem1})
    else:
        return redirect('/')


def user_Profile_Imagechange(request,id):
    if request.method == 'POST':
        ab = register.objects.get(id=id)
        ab.photo = request.FILES['files']
        ab.save()
        msg_success = "Profile Picture changed successfully"
        return render(request, 'user_settings.html', {'msg_success': msg_success})

def user_change_password(request,id):
    if request.method == 'POST':
        ac = register.objects.get(id=id)
        oldps = request.POST['currentPassword']
        newps = request.POST['newPassword']
        cmps = request.POST.get('confirmPassword')
        if oldps != newps:
            if newps == cmps:
                ac.password = request.POST.get('newPassword')
                ac.cpassword = request.POST.get('confirmPassword')
                ac.save()
                msg_success = "Password changed successfully"
                return render(request, 'user_settings.html', {'msg_success': msg_success})
        elif oldps == newps:
            messages.add_message(request, messages.INFO, 'Current and New password same')
        else:
            messages.info(request, 'Incorrect password same')
        return redirect('user_settings')


def user_plant_details(request):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=c_id)
        var = plantdetails.objects.filter(user_id=c_id).order_by('-id')
        return render(request,'user_plant_details.html',{'mem1':mem1,'var':var})
    else:
        return redirect('/')

def user_plant_details_print(request):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=c_id)
        var = plantdetails.objects.filter(user_id=c_id).order_by('-id')
        return render(request,'Plant_details_print.html',{'mem':mem1,'var':var})
    else:
        return redirect('/')

def user_plant_details_search(request):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=c_id)
        if request.method == "POST":
            p1=request.POST.get('input')
            var = plantdetails.objects.filter(user_id=c_id).filter(plant_name=p1).order_by('-id')
        
        return render(request,'Plant_details_print.html',{'mem':mem1,'var':var})
    else:
        return redirect('/')

def user_add_plant_details(request):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=c_id)
        if request.method == 'POST':
            p1 = request.POST['plant']
            p2 = request.POST['flowering']
            p3 = request.POST['fruiting']
            p4 = request.POST['fertilization']
            p5 = request.POST['harvesting']
            p6 = request.POST['harvesteddata']
            p7 = request.POST['planting']
            p8 = request.POST['pest']
            p9 = request.POST['location']
            p10 = request.POST['number']
            plant = plantdetails( plant_name = p1,flowering_date = p2,fruiting_date = p3,
                fertilization_date = p4,harvesting_date = p5,harvested_data = p6,
                planting_date = p7, pest_control_date = p8, location = p9, number = p10 ,user_id = c_id)
            plant.save()
            msg_success = "Details added successfully, Refresh your page"
            return render(request,'user_add_plant_details.html',{'msg_success':msg_success})
        return render(request,'user_add_plant_details.html',{'mem1':mem1})
    else:
        return redirect('/')

def user_viewedit_plantdetails(request,id):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=c_id)
        var = plantdetails.objects.filter(id=id)
        return render(request,'user_viewedit_plantdetails.html',{'mem1':mem1,'var':var})
    else:
        return redirect('/')

def user_plantdetails_update(request,id):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=c_id)
        if request.method == 'POST':
            abc = plantdetails.objects.get(id=id)
            abc.plant_name = request.POST.get('plant')
            abc.planting_date = request.POST.get('planting')
            abc.flowering_date = request.POST.get('flowering')
            abc.pest_control_date = request.POST.get('pest')
            abc.fruiting_date = request.POST.get('fruiting')
            abc.fertilization_date = request.POST.get('fertilization')
            abc.harvesting_date = request.POST.get('harvesting')
            abc.harvested_data = request.POST.get('harvesteddata')
            abc.location = request.POST.get('location')
            abc.number = request.POST.get('number')
            abc.save()
            print(abc)
            msg_success = "Details updated successfully, Refresh your page"
            return render(request,'user_viewedit_plantdetails.html',{'msg_success': msg_success})
        return render(request,'user_viewedit_plantdetails.html',{'mem1':mem1})
    else:
        return redirect('/')

def user_farm_weather(request):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=c_id)
        var = farm_weather.objects.filter(user_id=c_id).order_by('-id')
        return render(request,'user_farm_weather.html',{'mem1':mem1,'var':var})
    else:
        return redirect('/')

def user_weather_print(request):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=c_id)
        var = farm_weather.objects.filter(user_id=c_id).order_by('-id')
        return render(request,'weather_print.html',{'mem1':mem1,'var':var})
    else:
        return redirect('/')

def user_add_farm_weather(request):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=c_id)
        if request.method == 'POST':
            f1 = request.POST['parameter']
            f2 = request.POST['date']
            f3 = request.POST['morning']
            f4 = request.POST['evening']
            f5 = request.POST['average']
            f6 = request.POST['noon']
            farm = farm_weather( parameters = f1,date = f2,morning = f3,
                evening = f4,average = f5, noon = f6,user_id = c_id)
            farm.save()
            print(f5)
            msg_success = "Details added successfully, Refresh your page"
            return render(request,'user_add_farm_weather.html',{'msg_success':msg_success})
        return render(request,'user_add_farm_weather.html',{'mem1':mem1})
    else:
        return redirect('/')

def user_viewedit_farmweather(request,id):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=c_id)
        ab = farm_weather.objects.get(id=id)
        var = farm_weather.objects.filter(id=id)
        return render(request,'user_viewedit_farmweather.html',{'mem1':mem1,'var':var,'ab':ab})
    else:
        return redirect('/')

def user_farmweather_update(request,id):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=c_id)
        if request.method == 'POST':
            abc = farm_weather.objects.get(id=id)
            abc.parameters = request.POST.get('parameter')
            abc.date = request.POST.get('date')
            abc.morning = request.POST.get('morning')
            abc.noon = request.POST.get('noon')
            abc.evening = request.POST.get('evening')
            abc.average = request.POST.get('average')
            abc.save()
            print('average')
            msg_success = "Details updated successfully, Refresh your page"
            return render(request,'user_viewedit_farmweather.html',{'msg_success': msg_success})
        return render(request,'user_viewedit_farmweather.html')
    else:
        return redirect('/')

def user_find_weather(request):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=c_id)
        return render(request,'user_find_weather.html',{'mem1':mem1})
    else:
        return redirect('/')

def user_weather(request):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=c_id)
        if request.method == "POST":
            fromdate = request.POST.get('startdate')
            todate = request.POST.get('enddate')
            p1=request.POST.get('parameter')
            var = farm_weather.objects.filter(date__range=[fromdate, todate]).filter(user_id=c_id).filter(parameters=p1)
        return render(request,'user_weather.html',{'mem1':mem1,'var':var})
    else:
        return redirect('/')


def user_soil_sample_test(request):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=c_id)
        var = soil_sample_test.objects.filter(user_id=c_id).order_by('-id')
        return render(request,'user_soil_sample_test.html',{'mem1':mem1,'var':var})
    else:
        return redirect('/')

def user_soil_sample_print(request):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=c_id)
        var = soil_sample_test.objects.filter(user_id=c_id).order_by('-id')
        return render(request,'Soil_sample_print.html',{'mem':mem1,'var':var})
    else:
        return redirect('/')

def user_viewedit_soilsampletest(request,id):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=c_id)
        var = soil_sample_test.objects.filter(id=id)
        return render(request,'user_viewedit_soilsampletest.html',{'mem1':mem1,'var':var})
    else:
        return redirect('/')

def user_soilsampletest_update(request,id):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=c_id)
        if request.method == 'POST':
            abc = soil_sample_test.objects.get(id=id)
            abc.tests = request.POST.get('tests')
            abc.date = request.POST.get('date')
            abc.result = request.POST.get('result')
            abc.unit = request.POST.get('unit')
            abc.method = request.POST.get('method')
            abc.level = request.POST.get('level')
            abc.place = request.POST.get('place')
            abc.save()
            print(abc)
            msg_success = "Details updated successfully, Refresh your page"
            return render(request,'user_viewedit_soilsampletest.html',{'msg_success': msg_success})
        return render(request,'user_viewedit_soilsampletest.html',{'mem1':mem1})
    else:
        return redirect('/')


def user_add_soil_sample_test(request):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=c_id)
        if request.method == 'POST':
            # s1 = request.POST['tests']
            s2 = request.POST['date']
            # s3 = request.POST['result']
            # s4 = request.POST['unit']
            # s5 = request.POST['method']
            # s6 = request.POST['level']
            # s7 = request.POST['place']
            s8 = request.FILES['files']
            soil = soil_sample_test( date = s2, file = s8,user_id = c_id)
            soil.save()
            # soil = soil_sample_test( tests = s1,date = s2,result = s3,
            #     unit = s4,method= s5,level = s6, place = s7, file = s8,user_id = c_id)
            # soil.save()
            msg_success = "Details added successfully, Refresh your page"
            return render(request,'user_add_soil_sample_test.html',{'msg_success':msg_success})
        return render(request,'user_add_soil_sample_test.html',{'mem1':mem1})
    else:
        return redirect('/')

def user_fertilizer_applications(request):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=c_id)
        var = fertilizer_applications.objects.filter(user_id=c_id).order_by('-id')
        return render(request,'user_fertilizer_applications.html',{'mem1':mem1,'var':var})
    else:
        return redirect('/')

def user_fertilizer_print(request):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=c_id)
        var = fertilizer_applications.objects.filter(user_id=c_id).order_by('-id')
        return render(request,'Fertilizer_print.html',{'mem':mem1,'var':var})
    else:
        return redirect('/')

def user_fertilizer(request):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=c_id)
        var = fertilizer_applications.objects.values('fertilizer').distinct().filter(user_id=c_id)
        return render(request,'user_fertilizer.html',{'mem1':mem1,'var':var})
    else:
        return redirect('/')

def user_fertilizer_list(request):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=c_id)
        if request.method == "POST":
            p1=request.POST.get('fertilizer')
            var = fertilizer_applications.objects.filter(user_id=c_id).filter(fertilizer=p1).order_by('-id')
        return render(request,'user_fertilizer_list.html',{'mem1':mem1,'var':var})
    else:
        return redirect('/')

def list(request,id):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=c_id)
        var = fertilizer_applications.objects.filter(user_id=c_id).filter(id=id).order_by('-id')
        return render(request,'Fertilizer_print.html',{'mem':mem1,'var':var})
    else:
        return redirect('/')

def user_viewedit_fertilizer(request,id):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=c_id)
        var = fertilizer_applications.objects.filter(id=id)
        return render(request,'user_viewedit_fertilizer.html',{'mem1':mem1,'var':var})
    else:
        return redirect('/')

def user_fertilizer_update(request,id):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=c_id)
        if request.method == 'POST':
            abc = fertilizer_applications.objects.get(id=id)
            abc.fertilizer = request.POST.get('fertilizer')
            abc.applied_quantity = request.POST.get('Applied')
            abc.applied_date = request.POST.get('date')
            abc.brand_name = request.POST.get('brand_name')
            abc.place = request.POST.get('place')
            abc.plant_name = request.POST.get('plant_name')
            abc.unit = request.POST.get('unit')
            abc.save()
            msg_success = "Details updated successfully, Refresh your page"
            return render(request,'user_viewedit_fertilizer.html',{'msg_success': msg_success})
        return render(request,'user_viewedit_fertilizer.html',{'mem1':mem1})
    else:
        return redirect('/')

def user_add_fertilizer_applications(request):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=c_id)
        if request.method == 'POST':
            f1 = request.POST['fertilizer']
            f2 = request.POST['Applied']
            f3 = request.POST['date']
            f4 = request.POST['brand_name']
            f5 = request.POST['place']
            f6 = request.POST['plant_name']
            f7 = request.POST['unit']
            fert = fertilizer_applications( fertilizer = f1,applied_quantity = f2,applied_date = f3,
                brand_name = f4,place = f5,plant_name = f6, unit = f7, user_id = c_id)
            fert.save()
            msg_success = "Details added successfully, Refresh your page"
            return render(request,'user_add_fertilizer_applications.html',{'msg_success':msg_success})
        return render(request,'user_add_fertilizer_applications.html',{'mem1':mem1})
    else:
        return redirect('/')

def user_periodic_tests(request):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=c_id)
        var = periodic_tests.objects.filter(user_id=c_id).order_by('-id')
        return render(request,'user_periodic_tests.html',{'mem1':mem1,'var':var})
    else:
        return redirect('/')

def user_periodic_print(request):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=c_id)
        var = periodic_tests.objects.filter(user_id=c_id).order_by('-id')
        return render(request,'Periodic_test_print.html',{'mem':mem1,'var':var})
    else:
        return redirect('/')

def user_viewedit_periodictest(request,id):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=c_id)
        var = periodic_tests.objects.filter(id=id)
        return render(request,'user_viewedit_periodictest.html',{'mem1':mem1,'var':var})
    else:
        return redirect('/')

def user_periodictest_update(request,id):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=c_id)
        if request.method == 'POST':
            abc = periodic_tests.objects.get(id=id)
            abc.tests = request.POST.get('tests')
            abc.date = request.POST.get('date')
            abc.measurement = request.POST.get('measurement')
            abc.place = request.POST.get('place')
            abc.save()
            msg_success = "Details updated successfully, Refresh your page"
            return render(request,'user_viewedit_periodictest.html',{'msg_success': msg_success})
        return render(request,'user_viewedit_periodictest.html',{'mem1':mem1})
    else:
        return redirect('/')

def user_add_periodic_tests(request):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=c_id)
        if request.method == 'POST':
            p1 = request.POST['tests']
            p2 = request.POST['date']
            p3 = request.POST['measurement']
            p4 = request.POST['place']
            test = periodic_tests( tests = p1,date = p2,measurement = p3,
                place = p4 ,user_id = c_id)
            test.save()
            msg_success = "Details added successfully, Refresh your page"
            return render(request,'user_add_periodic_tests.html',{'msg_success':msg_success})
        return render(request,'user_add_periodic_tests.html',{'mem1':mem1})
    else:
        return redirect('/')

def user_farm_machineries(request):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=c_id)
        var = farm_machineries.objects.filter(user_id=c_id).order_by('-id')
        return render(request,'user_farm_machineries.html',{'mem1':mem1,'var':var})
    else:
        return redirect('/')

def user_machineries_print(request):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=c_id)
        var = farm_machineries.objects.filter(user_id=c_id).order_by('-id')
        return render(request,'Farm_machineries_print.html',{'mem':mem1,'var':var})
    else:
        return redirect('/')

def user_viewedit_farmmachineries(request,id):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=c_id)
        var = farm_machineries.objects.filter(id=id)
        return render(request,'user_viewedit_farmmachineries.html',{'mem1':mem1,'var':var})
    else:
        return redirect('/')

def user_farmmachineries_update(request,id):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=c_id)
        if request.method == 'POST':
            abc = farm_machineries.objects.get(id=id)
            abc.machine_name = request.POST.get('machines')
            abc.number_of_machines = request.POST.get('number')
            abc.working_hours = request.POST.get('hours')
            abc.machine_id = request.POST.get('machine_id')
            abc.place = request.POST.get('place')
            abc.date = request.POST.get('date')
            abc.total = request.POST.get('total')
            abc.save()
            msg_success = "Details updated successfully, Refresh your page"
            return render(request,'user_viewedit_farmmachineries.html',{'msg_success': msg_success})
        return render(request,'user_viewedit_farmmachineries.html',{'mem1':mem1})
    else:
        return redirect('/')


def user_add_farm_machineries(request):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=c_id)
        if request.method == 'POST':
            f1 = request.POST['machines']
            f2 = request.POST['number']
            f3 = request.POST['hours']
            f4 = request.POST['machine_id']
            f5 = request.POST['place']
            f6 = request.POST['date']
            f7 = request.POST['total']
            test = farm_machineries( machine_name = f1,number_of_machines = f2,working_hours = f3,
                machine_id = f4, place = f5, date =f6, total = f7,user_id = c_id)
            test.save()
            msg_success = "Details added successfully, Refresh your page"
            return render(request,'user_add_farm_machineries.html',{'msg_success':msg_success})
        return render(request,'user_add_farm_machineries.html',{'mem1':mem1})
    else:
        return redirect('/')

def user_man_power_usage(request):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=c_id)
        var = man_power_usage.objects.filter(user_id=c_id).order_by('-id')
        return render(request,'user_man_power_usage.html',{'mem1':mem1,'var':var})
    else:
        return redirect('/')

def user_manpower_print(request):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=c_id)
        var = man_power_usage.objects.filter(user_id=c_id).order_by('-id')
        return render(request,'Man_power_print.html',{'mem':mem1,'var':var})
    else:
        return redirect('/')

def user_viewedit_manpower(request,id):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=c_id)
        var = man_power_usage.objects.filter(id=id)
        return render(request,'user_viewedit_manpower.html',{'mem1':mem1,'var':var})
    else:
        return redirect('/')

def user_manpower_update(request,id):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=c_id)
        if request.method == 'POST':
            abc = man_power_usage.objects.get(id=id)
            abc.job = request.POST.get('job')
            abc.number_of_peoples = request.POST.get('number')
            abc.working_hours = request.POST.get('hours')
            abc.place = request.POST.get('place')
            abc.date = request.POST.get('date')
            abc.total = request.POST.get('total')
            abc.save()
            msg_success = "Details updated successfully, Refresh your page"
            return render(request,'user_viewedit_manpower.html',{'msg_success': msg_success})
        return render(request,'user_viewedit_manpower.html',{'mem1':mem1})
    else:
        return redirect('/')


def user_add_man_power_usage(request):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=c_id)
        if request.method == 'POST':
            m1 = request.POST['job']
            m2 = request.POST['number']
            m3 = request.POST['hours']
            m4 = request.POST['place']
            m5 = request.POST['date']

            test = man_power_usage( job = m1,number_of_peoples = m2,working_hours = m3, place = m4,
                date = m5, user_id = c_id)
            test.save()
            
            msg_success = "Details added successfully, Refresh your page"
            return render(request,'user_add_man_power_usage.html',{'msg_success':msg_success})
        return render(request,'user_add_man_power_usage.html',{'mem1':mem1})
    else:
        return redirect('/')

def user_farm_expenses(request):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=c_id)
        var = farm_expenses.objects.filter(user_id=c_id).order_by('-id')
        return render(request,'user_farm_expenses.html',{'mem1':mem1,'var':var})
    else:
        return redirect('/')

def user_expense_print(request):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=c_id)
        var = farm_expenses.objects.filter(user_id=c_id).order_by('-id')
        return render(request,'Expense_print.html',{'mem':mem1,'var':var})
    else:
        return redirect('/')

def user_viewedit_farmexpenses(request,id):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=c_id)
        var = farm_expenses.objects.filter(id=id)
        return render(request,'user_viewedit_farmexpense.html',{'mem1':mem1,'var':var})
    else:
        return redirect('/')

def user_farmexpense_update(request,id):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=c_id)
        if request.method == 'POST':
            abc = farm_expenses.objects.get(id=id)
            abc.expenditure = request.POST.get('expenditure')
            abc.expense = request.POST.get('expense')
            abc.type_description = request.POST.get('description')
            abc.item = request.POST.get('item')
            abc.quantity = request.POST.get('quantity')
            abc.price = request.POST.get('price')
            abc.total_cost = request.POST.get('total')
            abc.date = request.POST.get('date')
            abc.save()
            msg_success = "Details updated successfully, Refresh your page"
            return render(request,'user_viewedit_farmexpense.html',{'msg_success': msg_success})
        return render(request,'user_viewedit_farmexpense.html',{'mem1':mem1})
    else:
        return redirect('/')

def user_add_farm_expenses(request):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=c_id)
        if request.method == 'POST':
            e1 = request.POST['expenditure']
            e2 = request.POST['expense']
            e3 = request.POST['description']
            e4 = request.POST['quantity']
            e5 = request.POST['price']
            e6 = request.POST['total']
            e7 = request.POST['date']
            test = farm_expenses( expenditure = e1,expense = e2,type_description = e3,
                quantity = e4,price = e5,total_cost = e6, date = e7,user_id = c_id)
            test.save()
            msg_success = "Details added successfully, Refresh your page"
            return render(request,'user_add_farm_expenses.html',{'msg_success':msg_success})
        return render(request,'user_add_farm_expenses.html',{'mem1':mem1})
    else:
        return redirect('/')


def user_find_expense(request):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=c_id)
        return render(request,'user_find_expense.html',{'mem1':mem1})
    else:
        return redirect('/')

def user_expense(request):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=c_id)
        if request.method == "POST":
            fromdate = request.POST.get('startdate')
            todate = request.POST.get('enddate')
            var = farm_expenses.objects.filter(date__range=[fromdate, todate]).filter(user_id=c_id)
        return render(request,'user_expense.html',{'mem1':mem1,'var':var})
    else:
        return redirect('/')

def user_farm_revenue(request):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=c_id)
        var = farm_revenue.objects.filter(user_id=c_id).order_by('-id')
        return render(request,'user_farm_revenue.html',{'mem1':mem1,'var':var})
    else:
        return redirect('/')

def user_revenue_print(request):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=c_id)
        var = farm_revenue.objects.filter(user_id=c_id).order_by('-id')
        return render(request,'Revenue_print.html',{'mem':mem1,'var':var})
    else:
        return redirect('/')

def user_viewedit_farmrevenue(request,id):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=c_id)
        var = farm_revenue.objects.filter(id=id)
        return render(request,'user_viewedit_farmrevenue.html',{'mem1':mem1,'var':var})
    else:
        return redirect('/')

def user_farmrevenue_update(request,id):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=c_id)
        if request.method == 'POST':
            abc = farm_revenue.objects.get(id=id)
            abc.revenue_type = request.POST.get('revenue_type')
            abc.type_description = request.POST.get('type_description')
            abc.quantity = request.POST.get('quantity')
            abc.revenue = request.POST.get('revenue')
            abc.date = request.POST.get('date')
            abc.save()
            msg_success = "Details updated successfully, Refresh your page"
            return render(request,'user_viewedit_farmrevenue.html',{'msg_success': msg_success})
        return render(request,'user_viewedit_farmrevenue.html',{'mem1':mem1})
    else:
        return redirect('/')

def user_add_farm_revenue(request):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=c_id)
        if request.method == 'POST':
            r1 = request.POST['revenue_type']
            r2 = request.POST['type_description']
            r3 = request.POST['quantity']
            r4 = request.POST['revenue']
            r5 = request.POST['date']
            test = farm_revenue(revenue_type = r1,type_description = r2,quantity = r3,
                revenue = r4,date=r5, user_id = c_id)
            test.save()
            msg_success = "Details added successfully, Refresh your page"
            return render(request,'user_add_farm_revenue.html',{'msg_success':msg_success})
        return render(request,'user_add_farm_revenue.html',{'mem1':mem1})
    else:
        return redirect('/')

def user_find_revenue(request):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=c_id)
        return render(request,'user_find_revenue.html',{'mem1':mem1})
    else:
        return redirect('/')

def user_revenue(request):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=c_id)
        if request.method == "POST":
            fromdate = request.POST.get('startdate')
            todate = request.POST.get('enddate')
            var = farm_revenue.objects.filter(date__range=[fromdate, todate]).filter(user_id=c_id)
        return render(request,'user_revenue.html',{'mem1':mem1,'var':var})
    else:
        return redirect('/')

def logout_user(request):
    if 'c_id' in request.session:
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/')

#------------------------STAFF----------------------------
def Staff_index(request):
    if 's_id' in request.session:
        if request.session.has_key('s_id'):
            s_id = request.session['s_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=s_id)
        return render(request,'Staff_index.html',{'mem':mem})
    else:
        return redirect('/')

def Staff_dashboard(request):
    if 's_id' in request.session:
        if request.session.has_key('s_id'):
            s_id = request.session['s_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=s_id)
        labels = []
        data = []
        queryset = farm_expenses.objects.filter(user_id=s_id)
        for j in queryset:
            labels=[j.price,j.total_cost,j.quantity]
            data=[j.price,j.total_cost,j.quantity]
        return render(request,'Staff_dashboard.html',{'mem':mem,'labels':labels,'data':data})
    else:
        return redirect('/')

def Staff_chart(request):
    if 's_id' in request.session:
        if request.session.has_key('s_id'):
            s_id = request.session['s_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=s_id)
        var = register.objects.filter(id = s_id)
        labels = []
        data = []
        queryset = farm_revenue.objects.filter(user_id=s_id)
        for j in queryset:
            labels=[j.quantity,j.revenue]
            data=[j.quantity,j.revenue]
        return render(request,'Staff_chart.html',{'mem1':mem1,'var':var,'labels':labels,'data':data})
    else:
        return redirect('/')


def Staff_settings(request):
    if 's_id' in request.session:
        if request.session.has_key('s_id'):
            s_id = request.session['s_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=s_id)
        mem = register.objects.filter(id = s_id)
        if request.method == 'POST':
            abc = register.objects.get(id=s_id)
            abc.name = request.POST.get('name')
            abc.username= request.POST.get('uname')
            abc.mobile = request.POST.get('mobile')
            abc.email = request.POST.get('email')
            abc.address = request.POST.get('address')
            abc.date = request.POST.get('date')
            abc.pin = request.POST.get('pin')
            abc.district = request.POST.get('district')
            abc.save()
            msg_success = "Details changed successfully"
            return render(request, 'Staff_settings.html', {'msg_success': msg_success})
        return render(request,'Staff_settings.html',{'mem':mem,'mem1':mem1})
    else:
        return redirect('/')


def Staff_Profile_Imagechange(request,id):
    if request.method == 'POST':
        ab = register.objects.get(id=id)
        ab.photo = request.FILES['files']
        ab.save()
        msg_success = "Profile Picture changed successfully"
        return render(request, 'Staff_settings.html', {'msg_success': msg_success})


def Staff_change_password(request,id):
    if request.method == 'POST':
        ac = register.objects.get(id=id)
        oldps = request.POST['currentPassword']
        newps = request.POST['newPassword']
        cmps = request.POST.get('confirmPassword')
        if oldps != newps:
            if newps == cmps:
                ac.password = request.POST.get('newPassword')
                ac.cpassword = request.POST.get('confirmPassword')
                ac.save()
                msg_success = "Password changed successfully"
                return render(request, 'Staff_settings.html', {'msg_success': msg_success})
        elif oldps == newps:
            messages.add_message(request, messages.INFO, 'Current and New password same')
        else:
            messages.info(request, 'Incorrect password same')
        return redirect('Staff_settings')


def Staff_clients(request):
    if 's_id' in request.session:
        if request.session.has_key('s_id'):
            s_id = request.session['s_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=s_id)
        var = register.objects.all()
        return render(request,'Staff_clients.html',{'mem':mem,'var':var})
    else:
        return redirect('/')

def Staff_clientdashboard(request,id):
    if 's_id' in request.session:
        if request.session.has_key('s_id'):
            s_id = request.session['s_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=s_id)
        var= register.objects.filter(id=id)
        labels = []
        data = []
        queryset = farm_expenses.objects.filter(user_id=id)
        for j in queryset:
            labels=[j.price,j.total_cost,j.quantity]
            data=[j.price,j.total_cost,j.quantity]
        return render(request,'Staff_clientdashboard.html',{'mem':mem,'var':var,'labels':labels,'data':data})
    else:
        return redirect('/')

def Staff_client_chart(request,id):
    if 's_id' in request.session:
        if request.session.has_key('s_id'):
            s_id = request.session['s_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=s_id)
        var = register.objects.filter(id =id)
        labels = []
        data = []
        queryset = farm_revenue.objects.filter(user_id=id)
        for j in queryset:
            labels=[j.quantity,j.revenue]
            data=[j.quantity,j.revenue]
        return render(request,'Staff_client_chart.html',{'mem1':mem1,'var':var,'labels':labels,'data':data})
    else:
        return redirect('/')

def Staff_plant_details(request):
    if 's_id' in request.session:
        if request.session.has_key('s_id'):
            s_id = request.session['s_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=s_id)
        var = plantdetails.objects.filter(user_id=s_id).order_by('-id')
        return render(request,'Staff_plant_details.html',{'mem':mem,'var':var})
    else:
        return redirect('/')

def Staff_plant_details_print(request):
    if 's_id' in request.session:
        if request.session.has_key('s_id'):
            s_id = request.session['s_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=s_id)
        var = plantdetails.objects.filter(user_id=s_id).order_by('-id')
        return render(request,'Plant_details_print.html',{'mem':mem,'var':var})
    else:
        return redirect('/')


def Staff_add_plant_details(request):
    if 's_id' in request.session:
        if request.session.has_key('s_id'):
            s_id = request.session['s_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=s_id)
        if request.method == 'POST':
            p1 = request.POST['plant']
            p2 = request.POST['flowering']
            p3 = request.POST['fruiting']
            p4 = request.POST['fertilization']
            p5 = request.POST['harvesting']
            p6 = request.POST['harvesteddata']
            p7 = request.POST['planting']
            p8 = request.POST['pest']
            p9 = request.POST['location']
            p10 = request.POST['number']
            plant = plantdetails( plant_name = p1,flowering_date = p2,fruiting_date = p3,
                fertilization_date = p4,harvesting_date = p5,harvested_data = p6,
                planting_date = p7, pest_control_date = p8, location = p9, number =p10,user_id = s_id)
            plant.save()
            msg_success = "Details added successfully, Refresh your page"
            return render(request,'Staff_add_plant_details.html',{'msg_success':msg_success})
        return render(request,'Staff_add_plant_details.html',{'mem':mem})
    else:
        return redirect('/')

def Staff_viewedit_plantdetails(request,id):
    if 's_id' in request.session:
        if request.session.has_key('s_id'):
            s_id = request.session['s_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=s_id)
        var = plantdetails.objects.filter(id=id)
        return render(request,'Staff_viewedit_plantdetails.html',{'mem':mem,'var':var})
    else:
        return redirect('/')

def Staff_plantdetails_update(request,id):
    if 's_id' in request.session:
        if request.session.has_key('s_id'):
            s_id = request.session['s_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=s_id)
        if request.method == 'POST':
            abc = plantdetails.objects.get(id=id)
            abc.plant_name = request.POST.get('plant')
            abc.planting_date = request.POST.get('planting')
            abc.flowering_date = request.POST.get('flowering')
            abc.pest_control_date = request.POST.get('pest')
            abc.fruiting_date = request.POST.get('fruiting')
            abc.fertilization_date = request.POST.get('fertilization')
            abc.harvesting_date = request.POST.get('harvesting')
            abc.harvested_data = request.POST.get('harvesteddata')
            abc.location = request.POST.get('location')
            abc.number = request.POST.get('number')
            abc.save()
            print(abc)
            msg_success = "Details updated successfully, Refresh your page"
            return render(request,'Staff_viewedit_plantdetails.html',{'msg_success': msg_success})
        return render(request,'Staff_viewedit_plantdetails.html')
    else:
        return redirect('/')


def Staff_farm_weather(request):
    if 's_id' in request.session:
        if request.session.has_key('s_id'):
            s_id = request.session['s_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=s_id)
        var = farm_weather.objects.filter(user_id = s_id).order_by('-id')
        return render(request,'Staff_farm_weather.html',{'mem':mem,'var':var})
    else:
        return redirect('/')

def Staff_weather_print(request):
    if 's_id' in request.session:
        if request.session.has_key('s_id'):
            s_id = request.session['s_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=s_id)
        var = farm_weather.objects.filter(user_id=s_id).order_by('-id')
        return render(request,'weather_print.html',{'mem':mem,'var':var})
    else:
        return redirect('/')

def Staff_add_farm_weather(request):
    if 's_id' in request.session:
        if request.session.has_key('s_id'):
            s_id = request.session['s_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=s_id)
        if request.method == 'POST':
            f1 = request.POST['parameter']
            f2 = request.POST['date']
            f3 = request.POST['morning']
            f4 = request.POST['evening']
            f5 = request.POST['average']
            farm = farm_weather( parameters = f1,date = f2,morning = f3,
                evening = f4,average = f5,user_id = s_id)
            farm.save()
            msg_success = "Details added successfully, Refresh your page"
            return render(request,'Staff_add_farm_weather.html',{'msg_success':msg_success})
        return render(request,'Staff_add_farm_weather.html',{'mem':mem})
    else:
        return redirect('/')

def Staff_viewedit_farmweather(request,id):
    if 's_id' in request.session:
        if request.session.has_key('s_id'):
            s_id = request.session['s_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=s_id)
        ab = farm_weather.objects.get(id=id)
        var = farm_weather.objects.filter(id=id)
        return render(request,'Staff_viewedit_farmweather.html',{'mem':mem,'var':var,'ab':ab})
    else:
        return redirect('/')

def Staff_farmweather_update(request,id):
    if 's_id' in request.session:
        if request.session.has_key('s_id'):
            s_id = request.session['s_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=s_id)
        if request.method == 'POST':
            abc = farm_weather.objects.get(id=id)
            abc.parameters = request.POST.get('parameter')
            abc.date = request.POST.get('date')
            abc.morning = request.POST.get('morning')
            abc.noon = request.POST.get('noon')
            abc.evening = request.POST.get('evening')
            abc.average = request.POST.get('average')
            abc.save()
            print(abc)
            msg_success = "Details updated successfully, Refresh your page"
            return render(request,'Staff_viewedit_farmweather.html',{'msg_success': msg_success})
        return render(request,'Staff_viewedit_farmweather.html')
    else:
        return redirect('/')

def Staff_find_weather(request):
    if 's_id' in request.session:
        if request.session.has_key('s_id'):
            s_id = request.session['s_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=s_id)
        return render(request,'Staff_find_weather.html',{'mem':mem})
    else:
        return redirect('/')

def Staff_weather(request):
    if 's_id' in request.session:
        if request.session.has_key('s_id'):
            s_id = request.session['s_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=s_id)
        if request.method == "POST":
            fromdate = request.POST.get('startdate')
            todate = request.POST.get('enddate')
            p1=request.POST.get('parameter')
            var = farm_weather.objects.filter(date__range=[fromdate, todate]).filter(user_id=s_id).filter(parameters=p1)
        return render(request,'Staff_weather.html',{'mem':mem,'var':var})
    else:
        return redirect('/')

def Staff_soil_sample_test(request):
    if 's_id' in request.session:
        if request.session.has_key('s_id'):
            s_id = request.session['s_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=s_id)
        var = soil_sample_test.objects.filter(user_id= s_id).order_by('-id')
        return render(request,'Staff_soil_sample_test.html',{'mem':mem,'var':var})
    else:
        return redirect('/')


def Staff_soil_sample_print(request):
    if 's_id' in request.session:
        if request.session.has_key('s_id'):
            s_id = request.session['s_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=s_id)
        var = soil_sample_test.objects.filter(user_id=s_id).order_by('-id')
        return render(request,'Soil_sample_print.html',{'mem':mem,'var':var})
    else:
        return redirect('/')

def Staff_viewedit_soilsampletest(request,id):
    if 's_id' in request.session:
        if request.session.has_key('s_id'):
            s_id = request.session['s_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=s_id)
        var = soil_sample_test.objects.filter(id=id)
        return render(request,'Staff_viewedit_soilsampletest.html',{'mem':mem,'var':var})
    else:
        return redirect('/')

def Staff_soilsampletest_update(request,id):
    if 's_id' in request.session:
        if request.session.has_key('s_id'):
            s_id = request.session['s_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=s_id)
        if request.method == 'POST':
            abc = soil_sample_test.objects.get(id=id)
            abc.tests = request.POST.get('tests')
            abc.date = request.POST.get('date')
            abc.result = request.POST.get('result')
            abc.unit = request.POST.get('unit')
            abc.method = request.POST.get('method')
            abc.level = request.POST.get('level')
            abc.place = request.POST.get('place')
            abc.save()
            print(abc)
            msg_success = "Details updated successfully, Refresh your page"
            return render(request,'Staff_viewedit_soilsampletest.html',{'msg_success': msg_success})
        return render(request,'Staff_viewedit_soilsampletest.html')
    else:
        return redirect('/')


def Staff_add_soil_sample_test(request):
    if 's_id' in request.session:
        if request.session.has_key('s_id'):
            s_id = request.session['s_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=s_id)
        if request.method == 'POST':
            s1 = request.POST['tests']
            s2 = request.POST['date']
            s3 = request.POST['result']
            s4 = request.POST['unit']
            s5 = request.POST['method']
            s6 = request.POST['level']
            s7 = request.POST['place']
            soil = soil_sample_test( tests = s1,date = s2,result = s3,
                unit = s4,method= s5,level = s6, place = s7,user_id = s_id)
            soil.save()
            msg_success = "Details added successfully, Refresh your page"
            return render(request,'Staff_add_soil_sample_test.html',{'msg_success':msg_success})
        return render(request,'Staff_add_soil_sample_test.html',{'mem':mem})
    else:
        return redirect('/')

def Staff_fertilizer_applications(request):
    if 's_id' in request.session:
        if request.session.has_key('s_id'):
            s_id = request.session['s_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=s_id)
        var = fertilizer_applications.objects.filter(user_id=s_id).order_by('-id')
        return render(request,'Staff_fertilizer_applications.html',{'mem':mem,'var':var})
    else:
        return redirect('/')

def Staff_fertilizer(request):
    if 's_id' in request.session:
        if request.session.has_key('s_id'):
            s_id = request.session['s_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=s_id)
        var = fertilizer_applications.objects.values('fertilizer').distinct().filter(user_id=s_id)
        return render(request,'Staff_fertilizer.html',{'mem':mem,'var':var})
    else:
        return redirect('/')

def Staff_fertilizer_print(request):
    if 's_id' in request.session:
        if request.session.has_key('s_id'):
            s_id = request.session['s_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=s_id)
        var = fertilizer_applications.objects.filter(user_id=s_id).order_by('-id')
        return render(request,'Fertilizer_print.html',{'mem':mem,'var':var})
    else:
        return redirect('/')

def Staff_fertilizer_list(request):
    if 's_id' in request.session:
        if request.session.has_key('s_id'):
            s_id = request.session['s_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=s_id)
        if request.method == "POST":
            p1=request.POST.get('fertilizer')
            var = fertilizer_applications.objects.filter(user_id=s_id).filter(fertilizer=p1)
        return render(request,'Staff_fertilizer_list.html',{'mem':mem,'var':var})
    else:
        return redirect('/')

def Staff_viewedit_fertilizer(request,id):
    if 's_id' in request.session:
        if request.session.has_key('s_id'):
            s_id = request.session['s_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=s_id)
        var = fertilizer_applications.objects.filter(id=id)
        return render(request,'Staff_viewedit_fertilizer.html',{'mem':mem,'var':var})
    else:
        return redirect('/')

def Staff_fertilizer_update(request,id):
    if 's_id' in request.session:
        if request.session.has_key('s_id'):
            s_id = request.session['s_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=s_id)
        if request.method == 'POST':
            abc = fertilizer_applications.objects.get(id=id)
            abc.fertilizer = request.POST.get('fertilizer')
            abc.applied_quantity = request.POST.get('Applied')
            abc.applied_date = request.POST.get('date')
            abc.brand_name = request.POST.get('brand_name')
            abc.place = request.POST.get('place')
            abc.plant_name = request.POST.get('plant_name')
            abc.unit = request.POST.get('unit')
            abc.save()
            msg_success = "Details updated successfully, Refresh your page"
            return render(request,'Staff_viewedit_fertilizer.html',{'msg_success': msg_success})
        return render(request,'Staff_viewedit_fertilizer.html')
    else:
        return redirect('/')

def Staff_add_fertilizer_applications(request):
    if 's_id' in request.session:
        if request.session.has_key('s_id'):
            s_id = request.session['s_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=s_id)
        if request.method == 'POST':
            f1 = request.POST['fertilizer']
            f2 = request.POST['Applied']
            f3 = request.POST['date']
            f4 = request.POST['brand_name']
            f5 = request.POST['place']
            f6 = request.POST['plant_name']
            f7 = request.POST['unit']
            fert = fertilizer_applications( fertilizer = f1,applied_quantity = f2,applied_date = f3,
                brand_name = f4,place = f5, plant_name = f6, unit = f7, user_id = s_id)
            fert.save()
            msg_success = "Details added successfully, Refresh your page"
            return render(request,'Staff_add_fertilizer_applications.html',{'msg_success':msg_success})
        return render(request,'Staff_add_fertilizer_applications.html',{'mem':mem})
    else:
        return redirect('/')

def Staff_periodic_tests(request):
    if 's_id' in request.session:
        if request.session.has_key('s_id'):
            s_id = request.session['s_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=s_id)
        var = periodic_tests.objects.filter(user_id = s_id).order_by('-id')
        return render(request,'Staff_periodic_tests.html',{'mem':mem,'var':var})
    else:
        return redirect('/')

def Staff_periodic_print(request):
    if 's_id' in request.session:
        if request.session.has_key('s_id'):
            s_id = request.session['s_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=s_id)
        var = periodic_tests.objects.filter(user_id=s_id).order_by('-id')
        return render(request,'Periodic_test_print.html',{'mem':mem,'var':var})
    else:
        return redirect('/')

def Staff_viewedit_periodictest(request,id):
    if 's_id' in request.session:
        if request.session.has_key('s_id'):
            s_id = request.session['s_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=s_id)
        var = periodic_tests.objects.filter(id=id)
        return render(request,'Staff_viewedit_periodictest.html',{'mem':mem,'var':var})
    else:
        return redirect('/')

def Staff_periodictest_update(request,id):
    if 's_id' in request.session:
        if request.session.has_key('s_id'):
            s_id = request.session['s_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=s_id)
        if request.method == 'POST':
            abc = periodic_tests.objects.get(id=id)
            abc.tests = request.POST.get('tests')
            abc.date = request.POST.get('date')
            abc.measurement = request.POST.get('measurement')
            abc.place = request.POST.get('place')
            abc.save()
            msg_success = "Details updated successfully, Refresh your page"
            return render(request,'Staff_viewedit_periodictest.html',{'msg_success': msg_success})
        return render(request,'Staff_viewedit_periodictest.html')
    else:
        return redirect('/')

def Staff_add_periodic_tests(request):
    if 's_id' in request.session:
        if request.session.has_key('s_id'):
            s_id = request.session['s_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=s_id)
        if request.method == 'POST':
            p1 = request.POST['tests']
            p2 = request.POST['date']
            p3 = request.POST['measurement']
            p4 = request.POST['place']
            test = periodic_tests( tests = p1,date = p2,measurement = p3,
                place = p4 ,user_id = s_id)
            test.save()
            msg_success = "Details added successfully, Refresh your page"
            return render(request,'Staff_add_periodic_tests.html',{'msg_success':msg_success})
        return render(request,'Staff_add_periodic_tests.html',{'mem':mem})
    else:
        return redirect('/')

def Staff_farm_machineries(request):
    if 's_id' in request.session:
        if request.session.has_key('s_id'):
            s_id = request.session['s_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=s_id)
        var = farm_machineries.objects.filter(user_id = s_id).order_by('-id')
        return render(request,'Staff_farm_machineries.html',{'mem':mem,'var':var})
    else:
        return redirect('/')

def Staff_machineries_print(request):
    if 's_id' in request.session:
        if request.session.has_key('s_id'):
            s_id = request.session['s_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=s_id)
        var = farm_machineries.objects.filter(user_id=s_id).order_by('-id')
        return render(request,'Farm_machineries_print.html',{'mem':mem,'var':var})
    else:
        return redirect('/')

def Staff_viewedit_farmmachineries(request,id):
    if 's_id' in request.session:
        if request.session.has_key('s_id'):
            s_id = request.session['s_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=s_id)
        var = farm_machineries.objects.filter(id=id)
        return render(request,'Staff_viewedit_farmmachineries.html',{'mem':mem,'var':var})
    else:
        return redirect('/')

def Staff_farmmachineries_update(request,id):
    if 's_id' in request.session:
        if request.session.has_key('s_id'):
            s_id = request.session['s_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=s_id)
        if request.method == 'POST':
            abc = farm_machineries.objects.get(id=id)
            abc.machine_name = request.POST.get('machines')
            abc.number_of_machines = request.POST.get('number')
            abc.working_hours = request.POST.get('hours')
            abc.machine_id = request.POST.get('machine_id')
            abc.place = request.POST.get('place')
            abc.date = request.POST.get('date')
            abc.total = request.POST.get('total')
            abc.save()
            msg_success = "Details updated successfully, Refresh your page"
            return render(request,'Staff_viewedit_farmmachineries.html',{'msg_success': msg_success})
        return render(request,'Staff_viewedit_farmmachineries.html')
    else:
        return redirect('/')


def Staff_add_farm_machineries(request):
    if 's_id' in request.session:
        if request.session.has_key('s_id'):
            s_id = request.session['s_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=s_id)
        if request.method == 'POST':
            f1 = request.POST['machines']
            f2 = request.POST['number']
            f3 = request.POST['hours']
            f4 = request.POST['machine_id']
            f5 = request.POST['place']
            f6 = request.POST['date']
            f7 = request.POST['total']
            test = farm_machineries( machine_name = f1,number_of_machines = f2,working_hours = f3,
                machine_id = f4, place = f5, date =f6, total = f7,user_id = s_id)
            test.save()
            msg_success = "Details added successfully, Refresh your page"
            return render(request,'Staff_add_farm_machineries.html',{'msg_success':msg_success})
        return render(request,'Staff_add_farm_machineries.html',{'mem':mem})
    else:
        return redirect('/')

def Staff_man_power_usage(request):
    if 's_id' in request.session:
        if request.session.has_key('s_id'):
            s_id = request.session['s_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=s_id)
        var = man_power_usage.objects.filter(user_id = s_id).order_by('-date')
        return render(request,'Staff_man_power_usage.html',{'mem':mem,'var':var})
    else:
        return redirect('/')

def Staff_manpower_print(request):
    if 's_id' in request.session:
        if request.session.has_key('s_id'):
            s_id = request.session['s_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=s_id)
        var = man_power_usage.objects.filter(user_id=s_id).order_by('-id')
        return render(request,'Man_power_print.html',{'mem':mem,'var':var})
    else:
        return redirect('/')

def Staff_viewedit_manpower(request,id):
    if 's_id' in request.session:
        if request.session.has_key('s_id'):
            s_id = request.session['s_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=s_id)
        var = man_power_usage.objects.filter(id=id)
        return render(request,'Staff_viewedit_manpower.html',{'mem':mem,'var':var})
    else:
        return redirect('/')

def Staff_manpower_update(request,id):
    if 's_id' in request.session:
        if request.session.has_key('s_id'):
            s_id = request.session['s_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=s_id)
        if request.method == 'POST':
            abc = man_power_usage.objects.get(id=id)
            abc.job = request.POST.get('job')
            abc.number_of_peoples = request.POST.get('number')
            abc.working_hours = request.POST.get('hours')
            abc.place = request.POST.get('place')
            abc.date = request.POST.get('date')
            abc.total = request.POST.get('total')
            abc.save()
            msg_success = "Details updated successfully, Refresh your page"
            return render(request,'Staff_viewedit_manpower.html',{'msg_success': msg_success})
        return render(request,'Staff_viewedit_manpower.html')
    else:
        return redirect('/')

def Staff_add_man_power_usage(request):
    if 's_id' in request.session:
        if request.session.has_key('s_id'):
            s_id = request.session['s_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=s_id)
        if request.method == 'POST':
            m1 = request.POST['job']
            m2 = request.POST['number']
            m3 = request.POST['hours']
            m4 = request.POST['place']
            m5 = request.POST['date']
            m6= request.POST['total']
            test = man_power_usage( job = m1,number_of_peoples = m2,working_hours = m3, place = m4,
                date = m5,total = m6, user_id = s_id)
            test.save()

            msg_success = "Details added successfully, Refresh your page"
            return render(request,'Staff_add_man_power_usage.html',{'msg_success':msg_success})
        return render(request,'Staff_add_man_power_usage.html',{'mem':mem})
    else:
        return redirect('/')

def Staff_farm_expenses(request):
    if 's_id' in request.session:
        if request.session.has_key('s_id'):
            s_id = request.session['s_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=s_id)
        var = farm_expenses.objects.filter(user_id=s_id).order_by('-id')
        return render(request,'Staff_farm_expenses.html',{'mem':mem,'var':var})
    else:
        return redirect('/')

def Staff_expense_print(request):
    if 's_id' in request.session:
        if request.session.has_key('s_id'):
            s_id = request.session['s_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=s_id)
        var = farm_expenses.objects.filter(user_id=s_id).order_by('-id')
        return render(request,'Expense_print.html',{'mem':mem,'var':var})
    else:
        return redirect('/')

def Staff_viewedit_farmexpenses(request,id):
    if 's_id' in request.session:
        if request.session.has_key('s_id'):
            s_id = request.session['s_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=s_id)
        var = farm_expenses.objects.filter(id=id)
        return render(request,'Staff_viewedit_farmexpense.html',{'mem':mem,'var':var})
    else:
        return redirect('/')

def Staff_farmexpense_update(request,id):
    if 's_id' in request.session:
        if request.session.has_key('s_id'):
            s_id = request.session['s_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=s_id)
        if request.method == 'POST':
            abc = farm_expenses.objects.get(id=id)
            abc.expenditure = request.POST.get('expenditure')
            abc.expense = request.POST.get('expense')
            abc.type_description = request.POST.get('description')
            abc.item = request.POST.get('item')
            abc.quantity = request.POST.get('quantity')
            abc.price = request.POST.get('price')
            abc.total_cost = request.POST.get('total')
            abc.date = request.POST.get('date')
            abc.save()
            msg_success = "Details updated successfully, Refresh your page"
            return render(request,'Staff_viewedit_farmexpense.html',{'msg_success': msg_success})
        return render(request,'Staff_viewedit_farmexpense.html',{'mem':mem})
    else:
        return redirect('/')

def Staff_add_farm_expenses(request):
    if 's_id' in request.session:
        if request.session.has_key('s_id'):
            s_id = request.session['s_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=s_id)
        if request.method == 'POST':
            e1 = request.POST['expenditure']
            e2 = request.POST['expense']
            e3 = request.POST['description']
            e4 = request.POST['quantity']
            e5 = request.POST['price']
            e6 = request.POST['total']
            e7 = request.POST['date']
            test = farm_expenses( expenditure = e1,expense = e2,type_description = e3,
                quantity = e4,price = e5,total_cost = e6, date = e7,user_id = s_id)
            test.save()
            msg_success = "Details added successfully, Refresh your page"
            return render(request,'Staff_add_farm_expenses.html',{'msg_success':msg_success})
        return render(request,'Staff_add_farm_expenses.html',{'mem':mem})
    else:
        return redirect('/')

def Staff_find_expense(request):
    if 's_id' in request.session:
        if request.session.has_key('s_id'):
            s_id = request.session['s_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=s_id)
        return render(request,'Staff_find_expense.html',{'mem':mem})
    else:
        return redirect('/')

def Staff_expense(request):
    if 's_id' in request.session:
        if request.session.has_key('s_id'):
            s_id = request.session['s_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=s_id)
        if request.method == "POST":
            fromdate = request.POST.get('startdate')
            todate = request.POST.get('enddate')
            var = farm_expenses.objects.filter(date__range=[fromdate, todate]).filter(user_id=s_id)
        return render(request,'Staff_expense.html',{'mem':mem,'var':var})
    else:
        return redirect('/')


def Staff_farm_revenue(request):
    if 's_id' in request.session:
        if request.session.has_key('s_id'):
            s_id = request.session['s_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=s_id)
        var = farm_revenue.objects.filter(user_id=s_id).order_by('-id')
        return render(request,'Staff_farm_revenue.html',{'mem':mem,'var':var})
    else:
        return redirect('/')

def Staff_revenue_print(request):
    if 's_id' in request.session:
        if request.session.has_key('s_id'):
            s_id = request.session['s_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=s_id)
        var = farm_revenue.objects.filter(user_id=s_id).order_by('-id')
        return render(request,'Revenue_print.html',{'mem':mem,'var':var})
    else:
        return redirect('/')


def Staff_viewedit_farmrevenue(request,id):
    if 's_id' in request.session:
        if request.session.has_key('s_id'):
            s_id = request.session['s_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=s_id)
        var = farm_revenue.objects.filter(id=id)
        return render(request,'Staff_viewedit_farmrevenue.html',{'mem':mem,'var':var})
    else:
        return redirect('/')

def Staff_farmrevenue_update(request,id):
    if 's_id' in request.session:
        if request.session.has_key('s_id'):
            s_id = request.session['s_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=s_id)
        if request.method == 'POST':
            abc = farm_revenue.objects.get(id=id)
            abc.revenue_type = request.POST.get('revenue_type')
            abc.type_description = request.POST.get('type_description')
            abc.quantity = request.POST.get('quantity')
            abc.revenue = request.POST.get('revenue')
            abc.date = request.POST.get('date')
            abc.save()
            msg_success = "Details updated successfully, Refresh your page"
            return render(request,'Staff_viewedit_farmrevenue.html',{'msg_success': msg_success})
        return render(request,'Staff_viewedit_farmrevenue.html')
    else:
        return redirect('/')

def Staff_add_farm_revenue(request):
    if 's_id' in request.session:
        if request.session.has_key('s_id'):
            s_id = request.session['s_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=s_id)
        if request.method == 'POST':
            r1 = request.POST['revenue_type']
            r2 = request.POST['type_description']
            r3 = request.POST['quantity']
            r4 = request.POST['revenue']
            r5 = request.POST['date']
            test = farm_revenue(revenue_type = r1,type_description = r2,quantity = r3,
                revenue = r4,date = r5, user_id = s_id)
            test.save()
            msg_success = "Details added successfully, Refresh your page"
            return render(request,'Staff_add_farm_revenue.html',{'msg_success':msg_success})
        return render(request,'Staff_add_farm_revenue.html',{'mem':mem})
    else:
        return redirect('/')

def Staff_find_revenue(request):
    if 's_id' in request.session:
        if request.session.has_key('s_id'):
            s_id = request.session['s_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=s_id)
        return render(request,'Staff_find_revenue.html',{'mem':mem})
    else:
        return redirect('/')

def Staff_revenue(request):
    if 's_id' in request.session:
        if request.session.has_key('s_id'):
            s_id = request.session['s_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=s_id)
        if request.method == "POST":
            fromdate = request.POST.get('startdate')
            todate = request.POST.get('enddate')
            var = farm_revenue.objects.filter(date__range=[fromdate, todate]).filter(user_id=s_id)
        return render(request,'Staff_revenue.html',{'mem':mem,'var':var})
    else:
        return redirect('/')


def logout_staff(request):
    if 's_id' in request.session:
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/')