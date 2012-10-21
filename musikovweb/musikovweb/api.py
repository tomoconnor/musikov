#api.py
from tastypie.resources import ModelResource
from musikovweb.models import MidiChain


class MidiChainResource(ModelResource):
    class Meta:
        queryset = MidiChain.objects.all()
        resource_name = 'midichain'