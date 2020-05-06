from rest_framework import serializers

from .models import members

class membersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = members
        fields = ('Id', 'real_name', 'tz' ,'start_datetime', 'start_date' , 'start_time' , 'end_datetime' ,'end_date', 'end_time')
