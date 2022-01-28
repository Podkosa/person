from rest_framework import serializers
from .models import People
from datetime import datetime

class PeopleSerializer(serializers.ModelSerializer):
    def validate_iin(self, value):
        if len(value) != 12 or not value.isnumeric():
            raise serializers.ValidationError("Incorrect IIN format, should be 12 numbers")
        try:
            datetime.strptime(value[0:6:1], '%y%m%d')
        except ValueError:
            raise ValueError("Incorrect IIN format, first 6 numbers are not YY-MM-DD")  
        if datetime.strptime(value[0:6:1], '%y%m%d') > datetime.today():
            raise ValueError("Incorrect IIN format, calculated age < 0, first 6 numbers should be YY-MM-DD")  
        if int(value[6]) < 1 or int(value[6]) > 6:
            raise ValueError("Incorrect IIN format, 7th number should be 1-6")  
        return value
    
    class Meta:
        model = People
        fields = '__all__'  
        read_only_fields = ['age']