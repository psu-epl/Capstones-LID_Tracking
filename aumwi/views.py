from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.forms import modelform_factory, modelformset_factory
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages as message
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.urlresolvers import reverse
from .models import *
from django.template import RequestContext
import datetime

# Create your views here.


#******************************************************************************
# Basic Website administration pages

# None currently, a generic user profile view would go here later

#******************************************************************************
# Class for Manager level pages
class ManagerView(LoginRequiredMixin, PermissionRequiredMixin):
    permission_required = 'aumwi.is_manager'

    def addauthuser(request): # AddAuthUser.html
        # POST request means we received from data
        if request.method == 'POST':
            rfid = request.POST.get("rfid","")
            smid = request.POST.get("smid","")
            AuthForm = modelform_factory(AuthUser, fields='__all__')
            AuthForm = AuthForm(request.POST)
            if AuthForm.is_valid():
                AuthForm.save()
                message.success(request, '%s was successfully added!' % uname)
            else:
                message.error(request, 'Something went wrong!')
            #Strip request and return to "Add Auth User"
            return redirect('addauthuser')
        else:
            # GET request means we need to render form
            form = modelform_factory(AuthUser, fields='__all__')
            return render(request, 'AddAuthUser.html', {'form':form})


  # User Manipulation *************************************************

    def adduser(request): # AddUser.html
        # POST request means we received form data
        if request.method == 'POST':
            uname = request.POST.get("username","")
            UserForm = modelform_factory(User, fields='__all__')
            UserForm = UserForm(request.POST)
            if UserForm.is_valid():
                UserForm.save()
                message.success(request, '%s was successfully added!' % uname)
            else:
                message.error(request, 'Something went wrong!')
            #Strip request and return to "Add User"
            return redirect('adduser')
        else:
            # GET request means we need to render form
            form = modelform_factory(User, fields='__all__')
            return render(request, 'AddUser.html', {'form':form})


    def edituser(request): # EditUser.html
        # POST request required to show user data was passed
        if request.method == 'POST':
            uname = request.POST.get("username","")
            UserForm = modelform_factory(User, fields='__all__')
            UserForm = UserForm(request.POST)
            if UserForm.is_valid():
                # User data received and form created. Render page.
                return render(request, 'EditUser.html', {'form':UserForm})
            else:
                message.error(request, 'Invalid User data!')
        else:
            message.error(request, 'Something went wrong!')
        # An error has occured, redirect back to "Find User"
        return redirect('finduser')


    def updateuser(request): # EditUser.html
        # POST request required to show user data was passed
        if request.method == 'POST':
            uname = request.POST.get("username","")
            UserForm = modelform_factory(User, fields='__all__')
            UserForm = UserForm(request.POST)
            if UserForm.is_valid():
                UserForm.save()
                message.success(request, '%s successfully updated!' % uname)
            else:
                message.error(request, 'Invalid user data!')
        else:
            message.error(request, 'Something went wrong!')
        return redirect('finduser')


    def deluser(request):
        # Post request required to show user data was passed
        if request.method == 'POST':
            uname = request.POST.get("username","")
            user  = User.object.get(username = uname)
            return render(request, 'DelUser.html', {'uname':uname})
        else:
            message.error(request, 'Something went wrong!')
            return redirect('finduser')


    def deluserconf(request):
        try: # Try to delete user
            if request.method == 'POST':
                uname = request.POST.get("username","")
                user  = User.objects.get(username = uname)
            else:
                message.error(request, 'Something went wrong!')
                return redirect('finduser')
            user.delete()
            message.success(request, '%s successfully removed!' % uname)
            return render(request, 'DelUserConf.html', {'uname':uname})
        except:
            message.error(request, 'Something went wrong!')
            return redirect('finduser')


  # Station Manipulation **********************************************
    def addstation(request):
        # POST request means we received form data
        if request.method == 'POST':
            smid = request.POST.get("smid","")
            SMForm = modelform_factory(ModuleList, fields='__all__')
            SMForm = SMForm(request.POST)
            if SMForm.is_valid():
                SMForm.save()
                message.success(request, 'Station Module %s successfully added!' % smid)
            else:
                message.error(request, 'Something went wrong!')
            #Strip request and return to "Add Station"
            return redirect('addstation')
        else:
            # GET request means we need to render form
            form = modelform_factory(ModuleList, fields='__all__')
            return render(request, 'AddStation.html', {'form':form})


    def editstation(request):
        # POST request required to show station data was passed
        if request.method == 'POST':
            smid = request.POST.get("smid","")
            SMForm = modelform_factory(ModuleList, fields='__all__')
            SMForm = SMForm(request.POST)
            if SMForm.is_valid():
                # Station data received and form created. Render page.
                return render(request, 'EditStation.html', {'form':SMForm})
            else:
                message.error(request, 'Invalid station data!')
        else:
            message.error(request, 'Something went wrong!')
        # An error has occurred, redirect back to "Find Station"
        return redirect('findstation')


    def updatestation(request):
        # POST request required to show user data was paused
        if request.method == 'POST':
            smid = request.POST.get("smid","")
            SMForm = modelform_factory(ModuleList, fields='__all__')
            SMForm = SMForm(request.POST)
            if SMForm.is_valid():
                SMForm.save()
                message.success(request, 'Station module %s successfully updated!' % smid)
            else:
                message.error(request, 'Invalid station data!')
        else:
            message.error(request, 'Something went wrong!')
        return redirect('findstation')


    def delstation(request):
        # POST request required to show station data was passed
        if request.method == 'POST':
            smid = request.POST.get("smid","")
            sm   = ModuleList.objects.get(smid = smid)
            name = sm.name
            return render(request, 'DelStation.html', {'uname':name,'smid':smid})
        else:
            message.error(request, 'Something went wrong!')
            return redirect('findstation')


    def delstationconf(request):
        try: # Try to delete station module
            if request.method == 'POST':
                smid = request.POST.get("smid","")
                sm   = ModuleList.objects.get(smid = smid)
                name = sm.name
            else:
                message.error(request, 'Something went wrong!')
                return redirect('findstation')
            sm.delete()
            message.success(request, 'Station module %s successfully removed!' % name)
            return render(request, 'DelStationConf.html', {'uname':name,'smid':smid})
        except:
            message.error(request, 'Something went wrong!')
            return redirect('findstation')


  # Searches **********************************************************
    def finduser(request):
        # If POST handling submitted data
        if request.method == 'POST':
            uname = request.POST.get("username","")
            email = request.POST.get("email","")
            if uname or email:
                formset = modelformset_factory(User, fields='__all__')
                if uname:
                    instance = User.objects.get(username=uname)
                elif email:
                    instance = User.objects.get(email=email)
                user = formset(instance=instance)
                return render(request, 'FindUser.html', {'form':user})
            else:
                message.error(request, 'Invalid user data!')
                return redirect('finduser')
        else: #Else throw up the submission form
            #message.info(request, 'Feature not implemented yet.')
            form = modelform_factory(User, fields=['username','email'])
            return render(request, 'FindUser.html', {'form':form})


    def findstation(request):
        # If POST handling submitted data
        if request.method == 'POST':
            smid = request.POST.get("smid","")
            name = request.POST.get("name","")
            if smid or name:
                formset = modelformset_factory(ModuleList, fields='__all__')
                if smid:
                    instance = ModuleList.objects.get(smid = smid)
                elif name:
                    instance = ModuleList.objects.get(name = name)
                station = formset(instance=instance)
                return render(request, 'FindStation.html', {'form':station})
            else:
                message.error(request, 'Invalid station data!')
                return redirect('findstation')
        else: #Else throw up the submission form
            #message.info(request, 'Feature not implemented yet.')
            form = modelform_factory(ModuleList, fields=['smid','name'])
            return render(request, 'FindStation.html', {'form':form})


  # Reports ***********************************************************
    def reports(request):
        return render(request, 'ReportsBase.html')

    def rpt_err(request):
        message.error(request, 'Something went wrong!')
        return render(request, 'ReportsError.html')

    def usebyd(request, start_date, end_date):
        formset = modelformset_factory(UsageLog, fields='__all__')
        formset = formset(queryset=Usagelog.objects.filter(TimeIn__gte(datetime(start_date[0-3],start_date[4-5],start_date[6-7]))))
        formset = formset(queryset=Usagelog.objects.filter(TimeOut__lte(datetime(end_date[0-3],end_date[4-5],end_date[6-7]))))
        if formset.is_valid():
            return render(request, 'RptByDate.html',{'form':formset})
        else:
            message.error(request, 'Something went wrong!')
            return redirect('rpt_base')

    def usebyu(request):
        return render(request, 'RptUseByUser.html')

    def usebysm(request):
        return render(request, 'RptUseBySm.html')

    def usebyud(request):
        return render(request, 'RptUseByUserAndDate.html')

    def usebysmd(request):
        return render(request, 'RptUseBySmAndDate.html')

    def usebysmu(request):
        return render(request, 'RptUseBySmAndUser.html')

    def usebysmud(request):
        return render(request, 'RptUseBySmUserAndDate.html')


#******************************************************************************
# Class for Admin level pages
class AdminView(LoginRequiredMixin, PermissionRequiredMixin):
    permission_required = 'aumwi.is_admin'

    def makemanager():
        test = 2
        return test


#******************************************************************************
# Class for Database Admin pages
class OwnerView(LoginRequiredMixin, PermissionRequiredMixin):
    permission_required = 'aumwi.is_owner'

    def databaseadmin(request):
        return render(request, 'DatabaseAdmin.html')

    def databasebackup(request):
        return render(request, 'DatabaseBackup.html')

    def databaserestore(request):
        return render(request, 'DatabaseRestore.html')


#******************************************************************************
# Logs the user into the Station Module and starts a UsageLog entry
@csrf_exempt
def sm_login(request):
    user = request.POST.get("RFID","")
    smid = request.POST.get("SMID","")
    try:
        user = User.objects.get(rfid = user)
    except (KeyError, User.DoesNotExist):
        return HttpResponse(False)
    else:
        really_there = AuthUser.objects.filter(user_id = user.id, smid_id = smid).exists()
        if really_there == True:
            UsageLog.objects.create(user_id = user.id, smid_id = smid, TimeIn = timezone.now(), TimeOut = timezone.now())
    return HttpResponse(really_there)


#******************************************************************************
# Logs the user out of the Station Module and updates the UsageLog entry
@csrf_exempt
def sm_logout(request):
    smid = request.POST.get("SMID","")
    try:
        UL = UsageLog.objects.filter(smid_id=smid).order_by('-TimeIn')[0]
    except (KeyError, UsageLog.DoesNotExist):
        return HttpResponse (False)
    else:
        UL.set_time_out()
        UL.save()
    return HttpResponse(True)


#******************************************************************************
# Adds the user to the SM AuthList
@csrf_exempt
def sm_add_auth(request):
    user = request.POST.get("user","")
    smid = request.POST.get("smid","")

    if user and smid:
        user = User.objects.get(rfid = user)
        smid = ModuleList.objects.get(smid = smid)
        entry = AuthUser.objects.create(user_id = user.id , smid_id = smid.id)
        return HttpResponse(True)
    else:
        return HttpResponse(False)



#******************************************************************************
# Wrapper for SM function to add user to AuthList
@csrf_exempt
def sm_add(request):
    mgr  = request.POST.get("mgr","")
    if mgr:
        mgr = User.objects.get(rfid = mgr)
        #if  mgr.has_perm(is_manager):
        return sm_add_auth(request)
    return HttpResponse(False)


#*** EOF VIEWS.PY ***
