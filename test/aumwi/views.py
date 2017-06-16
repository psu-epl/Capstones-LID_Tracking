from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

# This is a very simplistic way of coding that could be used for the home view.
# Since it is class-based, it makes testing very easy.
class HomeView(TemplateView):
    template_name = 'aum/index.html'

# This auto-completed after I typed 'class' when I first started coding. Not sure why.
'''
class ClassName(object):
    """docstring for ."""
    def __init__(self, arg):
        super(, self).__init__()
        self.arg = arg
'''

# This commented out block is the code provided to me for testing
'''
from django.shortcuts import render
from .models import User, ModuleList, AuthUser, UsageLog
# Create your views here.


#**********************************************************************************************************************
def index(request):
    return render(request, 'index.html')


#*********************************************************************************************************************
'''
