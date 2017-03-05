from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

def kirr_redirect_view(request, *args, **kwargs):
	return HttpResponse("Function based view")

class KirrCBView(View):
	def get(self, request, *args, **kwargs):
		return HttpResponse("Class based view")
