from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = fields = [ 

                        'project_name','company_address','company_name', 
                        'date' ,'date_to_start','start_time' ,'finish_time',
                       'street_address','fax_number','phone_number',
                        'department_Location','id'

                         ]
        extra_kwargs = {

            'url': {'view_name': 'Event', 'lookup_field': 'id'},
        }