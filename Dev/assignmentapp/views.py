from django.shortcuts import render
from django.http import HttpResponse
#from .models import Board
from django.utils.translation import activate
from django.utils.translation import ugettext_lazy as _

# Create your views here.
def testlang(request):
        return HttpResponse(_('Welcome to the discussion board!'))

def home(request):
    #boards = Board.objects.all()
        return render(request, 'home.html')
		#return render(request, 'home.html', {'boards': boards})
	
def cities(request):
        return render(request, 'cities.html')	