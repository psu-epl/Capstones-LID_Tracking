from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
#from .models import Question
#commenting this section out to remove from project. Leaving it here for now just in case things go sidewats.

def index(request):
    return render(request, 'aum/index.html')
#def detail(request, question_id):
#    return HttpResponse("You're looking at question %s." % question_id)
#
#def results(request, question_id):
#    response = "You're looking at the results of question %s."
#    return HttpResponse(response % question_id)
#
#def vote(request, question_id):
#    return HttpResponse("You're voting on question %s." % question_id)
#    
def user(request, user_id):  #added this view for user
    q=User.objects.get(pk = user_id)
    return HttpResponse("You're looking at a user account for %s." % q)


#THIS WAS ADDED TO TRY FOR A LOGIN ATTEMPT
def login(request):   #removed  , u ,p
   u= request.POST['u']
   p = request.POST['p']
   
   try:
        U2=User.objects.get(username=u)
   except (KeyError, User.DoesNotExist):
       return HttpResponseRedirect(reverse( 'aum:index'))
       #return HttpResponse("That User Doesn't Exist")     HttpResponseRedirect
   else:
        P2 = U2.password
        answer = (p==P2)
        return HttpResponse("Is that a real password and real user?   True or False: %s" %answer)

#def vote(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    try:
#        selected_choice = question.choice_set.get(pk=request.POST['choice'])
#    except (KeyError, Choice.DoesNotExist):
#        # Redisplay the question voting form.
#        return render(request, 'aum/details.html', {
#            'question': question,
#            'error_message': "You didn't select a choice.",
#        })
#    else:
#        selected_choice.votes += 1
#        selected_choice.save()
#        # Always return an HttpResponseRedirect after successfully dealing
#        # with POST data. This prevents data from being posted twice if a
#        # user hits the Back button.
#        return HttpResponseRedirect(reverse('aum:results', args=(question.id,)))