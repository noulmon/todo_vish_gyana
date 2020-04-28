from django.db import transaction
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from user.models import User


class UserServices:
    @transaction.atomic
    def register(self, serializer):
        with transaction.atomic():
            '''Checking whether the user details are valid or not'''
            if serializer.is_valid():
                '''Saving user details are valid'''
                user = serializer.save()
                if user:
                    return Response(
                        {
                            'success': True,
                            'message': 'User successfully registered',
                        },
                        status=status.HTTP_201_CREATED
                    )
            return Response(
                {
                    'success': False,
                    'errors': serializer.errors,
                },
                status=status.HTTP_400_BAD_REQUEST
            )

    @transaction.atomic
    def login(self, email, password):
        with transaction.atomic():
            '''Checking whether the user already exists or not'''
            if User.objects.filter(email=email).exists():
                '''User object'''
                user = User.objects.get(email=email)
                '''User password authentication'''
                if user.check_password(password):
                    '''User Token'''
                    token, _ = Token.objects.get_or_create(user=user)
                    return Response(
                        {
                            'success': True,
                            'message': 'User login successful',
                            'token': token.key,
                        },
                        status=status.HTTP_200_OK
                    )
                return Response(
                    {
                        'success': False,
                        'errors': 'Invalid password',
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
            return Response(
                {
                    'success': False,
                    'status_code': 404,
                    'errors': "email not found",
                },
                status=status.HTTP_404_NOT_FOUND
            )
