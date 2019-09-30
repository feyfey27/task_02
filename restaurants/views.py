from django.shortcuts import render

# Create your views here.

def task2view(request):
	context = {
		"msg": "Hello World!"
	}	
	return render(request, 'task2.html', context)

