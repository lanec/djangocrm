from django.shortcuts import HttpResponse, render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
# instead of using from django.db import models we will use the below line which will let us use the Q command without having to type models.Q over and over
from django.db.models import Q
from crm.forms import UserForm, SigninForm, IndividualForm
from crm.models import SubscriberOrganization, Individual

def index(request):
	return render(request, 'crm/home.html')

def signup(request):
	if request.method == "POST":
		form = UserForm(request.POST)
		if form.is_valid():
			sub_existing = User.objects.filter(
				Q(username=form.cleaned_data['username']) |
				Q(email=form.cleaned_data['email'])).count() != 0
			org_existing = SubscriberOrganization.objects.filter(org_name=form.cleaned_data['organization']).count() != 0
	
			if sub_existing:
				form.errors['username'] = 'Your username or email already exists!'
		
			elif org_existing:
				form.errors['organization'] = 'An organization with that name already exists!'

			else:
				data = form.cleaned_data

				user = User.objects.create_user(data['username'], data['email'], data['password'])
				user.first_name = data['first_name']
				user.last_name = data['last_name']
				user.save()
				SubscriberOrganization.objects.create(org_name = form.cleaned_data['organization'], subscriber=user)

				return redirect("/")
	else:
		form = UserForm()

	print form.errors
	return render(request, 'crm/signup.html', {'form': form})

def signin(request):
	if request.method == "POST":
		form = SigninForm(request.POST)
		if form.is_valid():
			user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
			if user:
				login(request, user)
				return redirect("/")
			else:
				form.errors['username'] = "Your username or password is invalid!"

	else:
		form = SigninForm()

	return render(request, 'crm/signin.html', {'form': form})

@login_required
def logout_view(request):
	logout(request)
	return redirect("/")

@login_required
def add_individual(request):
	if request.method == "POST":
		form = IndividualForm(request.POST)
		if form.is_valid():
			org=SubscriberOrganization.objects.filter(Q(subscriber=request.user)).get()
			individual = Individual.objects.create(parent_org = org, **form.cleaned_data)
			print "add_individual"
			return redirect("/add_individual")
	else:
		form = IndividualForm()
	return render(request, 'crm/add_individual.html', {'form': form})



#	if request.method == 'GET':
#		return HttpResponse("Signing Up - GET")
#	elif request.method == 'POST':
#		return HttpResponse("Signing Up - POST")