from django import forms 
from home.models import Identity_unique

class Identity_form(forms.ModelForm):
	
	NIS = forms.CharField()
	First_Name = forms.CharField()
	Last_Name = forms.CharField()

	
	
	class Meta: 
		
		model = Identity_unique
		
		fields = ('NIS','First_Name', 'Last_Name' )
		
		