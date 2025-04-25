from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def portal(request):
	links = [
		{'name' : 'Lists Portal', 'url' : 'https://https://lists.synergypharm.org'},
		{'name' : 'Other System', 'url' : 'https://other.system.com'},
	]
	return render(request, 'start/portal.html', {'links' : links})