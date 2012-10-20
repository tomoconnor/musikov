import time
from django.template import Context, Template, loader, RequestContext
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from musikovweb.models import *

def index(request):
	mf = MidiChain.objects.order_by('-rank','-pk')
	return render_to_response('main.html',{'chains':mf},context_instance=RequestContext(request))

def vote(request,direction,chainID):
	mf = MidiChain.objects.get(id=chainID)
	if dir == "up":
		x.rank += 1
	else:
		x.rank -= 1
	x.save()
	return HttpResponseRedirect('/?refresh=' + str(int(time.time())) + "#" + chainID )
