import time
import sys
import traceback
from django.template import Context, Template, loader, RequestContext
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from musikovweb.models import *
from musikovweb.forms import *

from musikovweb.musikov_class import MusikovSong
import logging

logger = logging.getLogger(__name__)


def process(upload_id):

	def cb(ms):
		nc = MidiChain()
		nc.fileName = ms.SongName
		nc.filePath = ms.SongPath
		nc.rank = 100
		nc.transitionMatrix = ms.TransitionMatrix
		nc.noteMapping = ms.NoteMapping
		nc.inverseNoteMapping = ms.InverseNoteMapping
		nc.transitionFrequencies = ms.TransitionFrequencies
		nc.transitionSum = ms.TransitionSum
		nc.pngFile = ms.pngFile
		nc.svgFile = ms.svgFile
		nc.dotFile = ms.dotFile
		nc.save()

	uf = UploadedFile.objects.get(id=upload_id)
	ufp = uf.uploadfile._get_path()
	#try:
	ms = MusikovSong(ufp)
	ms.loadSong(ufp)
	ms.run_with_callback(cb)
	#except:
	#	ex, val, tb = sys.exc_info()
	#	logger.error(traceback.format_exception(ex, val, tb))


def index(request):
	if request.method == 'POST':
		form = UploadForm(request.POST, request.FILES)
		if form.is_valid():
			newfile = UploadedFile(uploadfile = request.FILES[u'userFile'])
			newfile.save()
			process(newfile.id)
			# Redirect to the document list after POST
			return HttpResponseRedirect(reverse('musikovweb.views.index'))
	else:
		form = UploadForm() # A empty, unbound form
		mf = MidiChain.objects.order_by('-rank','-pk')
		return render_to_response('js.html',{'chains':mf,'form':form},context_instance=RequestContext(request))

def api_list(request):
	mf = MidiChain.objects.order_by('-rank','-pk')
	return render_to_response('list.json',{'chains':mf,'form':form},context_instance=RequestContext(request))

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
