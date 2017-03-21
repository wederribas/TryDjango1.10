from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.views import View

from analytics.models import ClickEvent

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

		print(obj)
		return render(request, template, context)

class URLRedirectView(View):
	def get(self, request, shortcode=None, *args, **kwargs):
		qs = KirrURL.objects.filter(shortcode__iexact=shortcode)
		if qs.count != 1 and not qs.exists():
			raise Http404
		obj = qs.first()
		ClickEvent.objects.create_event(obj)
		return HttpResponseRedirect(obj.url)
