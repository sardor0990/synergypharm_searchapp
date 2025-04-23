from django.shortcuts import render

# Create your views here.
def portal(request):
	links = [
		{'name' : 'Lists Portal', 'url' : 'https://https://lists.synergypharm.org'},
		{'name' : 'Other System', 'url' : 'https://other.system.com'},
	]
	return render(request, 'start/portal.html', {'links' : links})