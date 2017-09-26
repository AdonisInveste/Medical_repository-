import re 

from django.conf import settings

from django.shortcuts import redirect, reverse

from django.contrib.auth import logout

EXEMPT_URLS = [re.compile(settings.LOGIN_URL.lstrip('/'))]

if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
	
	EXEMPT_URLS += [re.compile(url) for url in settings.LOGIN_EXEMPT_URLS]
	
	
class LoginRequiredMiddleware:
	
	def __init__(self, get_response):
		
		self.get_response = get_response
		
	def __call__(self, request):
		
		response = self.get_response(request)
		return response
	
	
	def process_view(self, request, view_func, view_args, view_kwargs):
		
		assert hasattr(request, 'user')
		path = request.path_info.lstrip('/')
		
		url_is_exempt = any(url.match(path) for url in EXEMPT_URLS)
		
		if path == reverse('Identities:logout').lstrip('/'):
			
			logout(request)
			
		if request.user.is_authenticated() and url_is_exempt:
			
			return redirect(settings.LOGIN_REDIRECT_URL)
		
		elif request.user.is_authenticated() or url_is_exempt: 
			
			return None
		
		else:
			
			return redirect(settings.LOGIN_URL)
			
			
# If the user is not logged in and has an account with the services then the user must be redirected to the login page 

 # if the user is coming to the page for the first time then the user must be directed to the Home page that has the value proposition.
	
# If the user is logged out and the user clicks on the 'brand link' the user should be navigated to the value proposition page. 
		