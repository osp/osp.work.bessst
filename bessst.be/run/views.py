from django.shortcuts import redirect

def redirect_to_local_version(request):
    return redirect('/' + request.LANGUAGE_CODE + '/')

