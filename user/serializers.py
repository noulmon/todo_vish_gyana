from rest_framework import serializers

from user.models import User


# class UserDetailsSerializers(serializers.ModelSerializer):


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    password = serializers.CharField(required=True)

    def validate_email(self, email):
        '''Validating email'''
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Email address already exists')
        return email

    def validate_username(self, username):
        '''Validating username'''
        if username is not None and not username == '':
            if User.objects.filter(username=username).exists():
                raise serializers.ValidationError('Username already exists')
        return username

    def validate_password(self, password):
        '''Validating user password'''
        if len(password) < 8:
            raise serializers.ValidationError('Password should be of minimum 8 characters')
        return password

    def create(self, validated_data):
        '''Creating user object'''
        return User.objects.create_user(**validated_data)

    class Meta:
        model = User
        fields = (
            'email',
            'username',
            'password',
        )
