import time
from django.template import Context, Template, loader, RequestContext
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from musikovweb.models import *
from musikovweb.forms import *


def index(request):
	if request.method == 'POST':
		form = UploadForm(request.POST, request.FILES)
		if form.is_valid():
			newfile = UploadedFile(uploadfile = request.FILES[u'userFile'])
			newfile.save()

			# Redirect to the document list after POST
			return HttpResponseRedirect(reverse('musikovweb.views.index'))
	else:
		form = UploadForm() # A empty, unbound form
		mf = MidiChain.objects.order_by('-rank','-pk')
		return render_to_response('main.html',{'chains':mf,'form':form},context_instance=RequestContext(request))

def urlsubmit(request):
	if request.method == 'POST':
		pass
		#urllib2 it
		


def vote(request,dir,id):
	mf = MidiChain.objects.get(id=id)
	if dir == "up":
		mf.rank += 1
	else:
		mf.rank -= 1
	mf.save()
	return HttpResponseRedirect('/?refresh=' + str(int(time.time())) + "#" + id )
