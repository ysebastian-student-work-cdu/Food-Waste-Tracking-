from django.shortcuts import render

# Create your views here.
def reasons(request):
	return render(request, 'listitems/reasons.html')
