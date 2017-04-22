from django.shortcuts import render
from .models import Profile, SpecialUser, ModuleList, AuthUser, UsageLog
# Create your views here.


#**********************************************************************************************************************
def index(request):
    """
    Landing page of aum
    """

    return render(request, 'index.html')


#*********************************************************************************************************************



