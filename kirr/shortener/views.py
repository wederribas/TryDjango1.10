from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from .forms import SubmitUrlForm
from .models import KirrURL

TITLE = 'Kirr.co'


class HomeView(View):
	def get(self, request, *args, **kwargs):
		form = SubmitUrlForm()
		context = {
			'title': TITLE,
			'form': form,
		}
		return render(request, 'shortener/home.html', context)

	def post(self, request, *args, **kwargs):
		form = SubmitUrlForm(request.POST)
		context = {
			'title': TITLE,
			'form': form,
		}
		template = 'shortener/home.html'

		if form.is_valid():
			new_url = form.cleaned_data.get('url')
			obj, created = KirrURL.objects.get_or_create(url=new_url)
			context = {
				'title': TITLE,
				'object': obj,
				'created': created,
			}

			if created:
				template = 'shortener/success.html'
			else:
				template = 'shortener/already-exists.html'

		return render(request, template, context)

class KirrShortener(View):
	def get(self, request, shortcode=None, *args, **kwargs):
		obj = get_object_or_404(KirrURL, shortcode=shortcode)
		print(obj.url)
		return HttpResponseRedirect(obj.url)
