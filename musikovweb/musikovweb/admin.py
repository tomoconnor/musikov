from django.contrib import admin
from musikovweb.models import *

class MidiChainAdmin(admin.ModelAdmin):
	pass

admin.site.register(MidiChain,MidiChainAdmin)
