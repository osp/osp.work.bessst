# Create your views here.
import json

from django.shortcuts import render_to_response
from django.template import RequestContext
from django import forms
from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _

from people.models import Individual, Friend, Organization
from projects.models import Project
from flatpages.models import FlatPage

class IndividualForm(ModelForm):
    class Meta:
        model = Friend
        fields = ('location_explanation', 'firstname', 'prefix', 'name', 'email', 'link', 'location_latitude', 'location_longitude', 'newsletter', 'display')

class OrganizationForm(ModelForm):
    class Meta:
        model = Organization
        fields = ('name', 'address', 'city', 'phone', 'email', 'link')
    description = forms.CharField(label=_('Description of the Project'), widget=forms.Textarea)
    existing_partners = forms.CharField(label=_('Existing Partners'), widget=forms.Textarea)
    channels = forms.CharField(label=_('Through which channels can you already communicate?'), widget=forms.Textarea)

    def save(self, force_insert=False, force_update=False, commit=True):
        m = super(OrganizationForm, self).save(commit=False)
        
        # also create a new project that lists the aanvraag
        title = "Bessst label aanvraag " + self.cleaned_data['name']
        project = Project(published=False, axis_id=1, title=title)
        project.description += self.cleaned_data['description']
        project.description += '\n<h2>Existing Partners</h2>'
        project.description += '\n<p>' + self.cleaned_data['existing_partners'] + '</p>'
        project.description += '\n<h2>Through which channels can you already communicate?</h2>'
        project.description += self.cleaned_data['channels']
        project.slug = slugify(title)
        project.save()
        
        if commit:
            m.save()
        return m

def community(request):
    tpl_params = {}
    
    tpl_params['object_list'] = []
    
    # Because friends are a subclass of individuals,
    # We have to weed them out here:
    individuals = Individual.objects.all()
    for i in individuals:
        try:
            f = i.friend
        except Individual.DoesNotExist:
            tpl_params['object_list'].append(i)

    tpl_params['partners'] = Organization.objects.all()
    tpl_params['text'] = FlatPage.objects.get(slug='community')
    
    friends = Friend.objects.all()
    friends_hash = []
    for f in friends:
        hash = { 'name' : False, 'explanation' : f.location_explanation, 'lat' : f.location_latitude, 'lng' : f.location_longitude }
        if f.display:
            hash['name'] = f.get_full_name()
        friends_hash.append(hash)

    tpl_params['friends_json'] = json.dumps(friends_hash, indent=2, ensure_ascii=False)
    
    tpl_params['submitted'] = False
    
    if request.method == 'POST': # If the form has been submitted...
        form = IndividualForm(request.POST) # A form bound to the POST data
        if form.is_valid():
            form.save()
            tpl_params['submitted'] = True
    else:
        form = IndividualForm(label_suffix='')
    tpl_params['form'] = form
    return render_to_response("people/individual_list.html", tpl_params, context_instance = RequestContext(request))

def label_form(request):
    tpl_params = {}
    tpl_params['submitted'] = False

    if request.method == 'POST': # If the form has been submitted...
        form = OrganizationForm(request.POST) # A form bound to the POST data
        if form.is_valid():
            form.save()
            tpl_params['submitted'] = True
    else:
        form = OrganizationForm(label_suffix='')
    tpl_params['form'] = form
    return render_to_response("people/label_form.html", tpl_params, context_instance = RequestContext(request))

