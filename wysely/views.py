from django.shortcuts import render


def not_found(request):
	return render(request, '404.html')

def server_error(request):
	return render(request, '500.html')

def permission_denied(request):
	return render(request, '403.html')

def bad_request(request):
	return render(request, '400.html')

def not_allowed(request):
	return render(request, '405.html')