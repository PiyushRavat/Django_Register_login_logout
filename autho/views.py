from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect, HttpResponse
#from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.models import User
from autho.form import userformA
from django.urls import reverse
# Create your views here.
def index(request):
	return render(request, 'index.html', {})


# def reg(request):
# 	if request.method == "POST":
# 		form = UserCreationForm(request.POST)
# 		if form.is_valid():
# 			user = form.save()
# 			#username = form.cleaned_data.get('username')
# 			#message.success(request, f"New account created : {username}")
# 			login(request, user)
# 			return redirect("home")
# 		else:
# 			for msg in form.error_messages:
# 				print(form.error_messages[msg])

# 	form = UserCreationForm
# 	return render(request, 'reg.html', {"form":form})


#registration
def reg(request):
	if request.method == "POST":
		formA = userformA(request.POST)
		if formA.is_valid():
			username = formA.cleaned_data['username']
			email = formA.cleaned_data['email']
			first_name = formA.cleaned_data['first_name']
			password = formA.cleaned_data['password']
			User.objects.create_user(username=username, email=email, first_name=first_name, password=password)
			return redirect('home')
	
	else:
		formA = userformA()
	return render(request, 'reg.html', {'formA':formA})	


#Login
def login(request):
	context = {}
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user:
			login(request, user)
			return redirect("success")
			#return HttpResponseRedirect(reverse('success'))
		else:
			context["error"] = "ERROR....!!"
			return render(request, "login.html", context)
	else:
		return render(request, "login.html", context)


def success(request):
	context = {}
	context['user'] = request.user
	return render(request, "success.html", context)



def logout(request):
	if request.method == "POST":
		logout(request)
		return HttpResponseRedirect(reverse("login"))