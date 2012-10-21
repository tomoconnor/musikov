#api.py
from tastypie.resources import ModelResource
from musikovweb.models import MidiChain


class MidiChainResource(ModelResource):
    class Meta:
        #queryset = MidiChain.objects.all()
        queryset = MidiChain.objects.filter(transitionSum__gte=1)
        resource_name = 'midichain'
