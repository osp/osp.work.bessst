from django.shortcuts import render_to_response
from django.template import RequestContext 

from axis.models import Axis

def home(request):
    tpl_params = {}
    tpl_params['object_list'] = Axis.objects.all()
    return render_to_response("home.html", tpl_params, context_instance = RequestContext(request))
