from django.shortcuts import render, render_to_response

# Create your views here.
def index(resquest):
    return render(resquest, 'index.html', {})

#def index(resquest):
#    return render_to_response('index.html')
