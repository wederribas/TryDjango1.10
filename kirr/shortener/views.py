from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from .forms import SubmitUrlForm
from .models import KirrURL


class HomeView(View):
	def get(self, request, *args, **kwargs):
		form = SubmitUrlForm()
		context = {
			'title': 'Kirr.co',
			'form': form,
		}
		return render(request, 'shortener/home.html', context)

	def post(self, request, *args, **kwargs):
		form = SubmitUrlForm(request.POST)
		context = {
			'title': 'Kirr.co',
			'form': form,
		}
		return render(request, 'shortener/home.html', context)

class KirrShortener(View):
	def get(self, request, shortcode=None, *args, **kwargs):
		obj = get_object_or_404(KirrURL, shortcode=shortcode)
		print(obj.url)
		return HttpResponseRedirect(obj.url)
