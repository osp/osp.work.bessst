# Create your views here.
import json

from django.shortcuts import render_to_response
from django.template import RequestContext
from django import forms
from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from django.utils.translation import ugettext_lazy as _

from people.models import Individual, Friend, Organization
from projects.models import Project


class IndividualForm(ModelForm):
    class Meta:
        model = Friend
        fields = ('location_explanation', 'firstname', 'prefix', 'name', 'email', 'link', 'location_latitude', 'location_longitude', 'newsletter', 'display')


def community(request):
    tpl_params = {}
    tpl_params['object_list'] = Individual.objects.all()
    tpl_params['partners'] = Organization.objects.all()
    
    friends = Friend.objects.all()
    friends_hash = [{ 'name' : f.get_full_name(), 'explanation' : f.location_explanation, 'lat' : f.location_latitude, 'lng' : f.
location_longitude} for f in friends]
    tpl_params['friends_json'] = json.dumps(friends_hash, indent=2, ensure_ascii=False)
    
    tpl_params['submitted'] = False
    
    if request.method == 'POST': # If the form has been submitted...
        form = IndividualForm(request.POST) # A form bound to the POST data
        if form.is_valid():
            form.save()
            tpl_params['submitted'] = True
    else:
        form = IndividualForm()
    tpl_params['form'] = form
    return render_to_response("people/individual_list.html", tpl_params, context_instance = RequestContext(request))

