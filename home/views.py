from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from home.forms import Identity_form
from home.models import Identity_unique

# Create your views here.

class Identity_view(TemplateView):
	
	
	template_name = 'home/home.html'
	template_patient = 'home/patientprofile.html'
	
	
	
	def get(self, request):
		
		form = Identity_form()
		
		Identities = Identity_unique.objects.all()
		var = {'form': form, 'Identities': Identities}
		return render(request, self.template_name, var)
	
	
	def post(self, request):
		
		form = Identity_form(request.POST)
		
		if form.is_valid():
			
			NIS = form.save(commit=False)
			NIS.user = request.user
			NIS.save()
			
			IdentityContent = form.cleaned_data['NIS']
			
			form = Identity_form
			
			return redirect('home:home')
		
		var = {'form' : form, 'Content': Content }
		return render(request, self.template_patient,  var)
	
	

			