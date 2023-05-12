from rest_framework.serializers import ModelSerializer
from .models import CustomUser as User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import Permission
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from rest_framework.exceptions import APIException

class UsersSerializer(ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields=('id','username','password','password2', 'full_name','email','is_verified','is_active')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            full_name=validated_data['full_name'],
        )

        user.set_password(validated_data['password'])
        user.save() 
        return user
    
    
class UserAuthSerializer(ModelSerializer):
    class Meta:
        model = User
        fields=('id','username', 'full_name','email', 'is_verified','is_active')


class PermissionSerializer(serializers.ModelSerializer):
    permission = serializers.SerializerMethodField()
    class Meta:
        ref_name="document_serializer"
        model = Permission
        fields = '__all__'

    def get_permission(self, obj):
        return obj.content_type.app_label+'.'+obj.codename


class ChangePasswordByAdminSerializer(serializers.Serializer):
    new_password = serializers.CharField(max_length=128, write_only=True, required=True)
    confirm_password = serializers.CharField(max_length=128, write_only=True, required=True)


    def validate(self, data):
        user=User.objects.get(id= self.context['request'].parser_context['kwargs']['pk'])
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError({'confirmpassword': ("The two password fields didn't match.")})
        password_validation.validate_password(data['new_password'], user)
        return data

    def save(self, **kwargs):
        password = self.validated_data['new_password']
        user =User.objects.get(id= self.context['request'].parser_context['kwargs']['pk'])
        user.set_password(password)
        user.save()
        return user