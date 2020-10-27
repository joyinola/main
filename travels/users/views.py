from django.shortcuts import render
from django.contrib.auth import authenticate, login,logout
# Create your views here.
def indexx(request):
	if request.user.is_authenticated:
		return render(request, 'users/index.html')
	return render(request, 'users/login.html')
def login_view(request):
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']
		user=authenticate(request, username=username,password=password)
		if user:
			login(request, user)
			return render(request, 'users/index.html')
		return render(request,'users/login.html', {'message':'Invalid Credentials'})
	return render(request,'users/login.html')

def logout_view(request):
	logout(request)
	return render(request, 'users/login.html', {'message':'Logged Out'})