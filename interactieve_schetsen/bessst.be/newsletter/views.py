import datetime
from django.http import HttpResponseRedirect
from newsletter.models import Email

def signup(request):
    e = Email(email= request.POST['email'], join_date=datetime.datetime.now())
    e.save()
    return HttpResponseRedirect('/')
