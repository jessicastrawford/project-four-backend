from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from designs.serializers import DesignSerializer
# import django.contrib.auth.password_validation as validation



User = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)

    def validate(self, data):
        password = data.pop('password')
        password_confirmation = data.pop('password_confirmation')

        if password != password_confirmation:
            raise ValidationError({'password_confirmation': 'Does Not Match'})
        # try:
        #     validation.validate_password(password=password)
        # except ValidationError as err: 
        #     raise ValidationError({'password': err.messages})
        
        data['password'] = make_password(password)

        return data
        
    class Meta:
        model = User
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    saved_designs = DesignSerializer(many=True)
    added_designs = DesignSerializer(many=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'profile_image', 'job_title', 'company', 'saved_designs', 'added_designs')
