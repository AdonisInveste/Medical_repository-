from django.shortcuts import render, redirect

from django.urls import reverse
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

from django.contrib.auth.models import User
from Identities.forms import CreateAccountForm, UpdateAccountForm
from django.contrib.auth.models import User

# Create your views here.

def iivri(request):
	return render(request, 'Identities/iivri.html')

def register(request):
	
	if request.method == 'POST':
		
		form = CreateAccountForm(request.POST)
		
		if form.is_valid():
			form.save()
			return redirect('/Identity')
		else: 
			return redirect(reverse('Identities:logout'))
		
	else:
		
		form = CreateAccountForm()
		var = {'form':form}
		return render(request, 'Identities/create_account.html', var)
	
	
def view_profile(request):
	
	args = {'user': request.user}
	return render(request, 'Identities/profile.html', args)


def edit_profile(request):
	
	if request.method == 'POST':
		
		form = UpdateAccountForm(request.POST, instance=request.user)
		
		if form.is_valid():
			form.save()
			return redirect(reverse('Identities:view_profile'))
		
		else: 
			return redirect('/Identity/profile/edit')
		
		
	else:
		
		form = UpdateAccountForm(instance=request.user)
		
		var = {'form': form}
		
		return render(request, 'Identities/edit_profile.html', var)
	
	
def change_password(request):
	
	if request.method == 'POST':
		
		form = PasswordChangeForm(data=request.POST, user=request.user)
		
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect(reverse('Identities:change_password'))
		
		else:
			
			return redirect('/Identity/change-password')
		
	else: 
		
		form = PasswordChangeForm(user=request.user)
		
		var = {'form': form}
		return render(request, 'Identities/change_password.html', var)
			