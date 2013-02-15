# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.forms import ModelForm

from people.models import Individual, Friend, Organization

class IndividualForm(ModelForm):
    class Meta:
        model = Friend
        fields = ('firstname', 'prefix', 'name', 'email', 'link', 'location_latitude', 'location_longitude', 'location_explanation', 'newsletter', 'display')

def community(request):
    tpl_params = {}
    tpl_params['object_list'] = Individual.objects.all()
    tpl_params['partners'] = Organization.objects.all()
    
    if request.method == 'POST': # If the form has been submitted...
        form = IndividualForm(request.POST) # A form bound to the POST data
        if form.is_valid():
            form.save()
    else:
        form = IndividualForm()
    
    tpl_params['form'] = form
    return render_to_response("people/individual_list.html", tpl_params, context_instance = RequestContext(request))

