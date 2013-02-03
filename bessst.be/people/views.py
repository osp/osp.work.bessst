# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.forms import ModelForm

from people.models import Individual, Organization

class IndividualForm(ModelForm):
    class Meta:
        model = Individual

def community(request):
    if request.method == 'POST': # If the form has been submitted...
        form = IndividualForm(request.POST) # A form bound to the POST data
        if form.is_valid():
            pass
    tpl_params = {}
    tpl_params['object_list'] = Individual.objects.all()
    tpl_params['partners'] = Organization.objects.all()
    tpl_params['form'] = IndividualForm()
    return render_to_response("people/individual_list.html", tpl_params, context_instance = RequestContext(request))

