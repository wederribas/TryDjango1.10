from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import KirrURL

def kirr_redirect_view(request, shortcode=None, *args, **kwargs):
	# One possibility
	# try:
	# 	obj = KirrURL.objects.get(shortcode=shortcode)
	# except:
	# 	obj = KirrURL.objects.all().first()

	# Another possibility
	# obj_url = None
	# qs = KirrURL.objects.filter(shortcode__iexact=shortcode.upper())
	# if qs.exists() and qs.count() == 1:
	# 	obj = qs.first()
	# 	obj_url = obj.url

	# The best one
	obj = get_object_or_404(KirrURL, shortcode=shortcode)

	return HttpResponse("Hello. The URL is: {sc}".format(sc=obj.url))

class KirrCBView(View):
	def get(self, request, shortcode=None, *args, **kwargs):
		return HttpResponse("Hello from the other side. Shortcode => {sc}".format(sc=shortcode))
