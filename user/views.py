from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from user.serializers import UserSerializer
from user.services import UserServices

user_service = UserServices()


class UserRegistration(APIView):
    """
    API view for User Registration
    """

    @permission_classes((AllowAny,))
    def post(self, request):
        try:
            '''User serializer'''
            serializer = UserSerializer(data=request.data)
            '''User registration service'''
            return user_service.register(serializer=serializer)
        except Exception as e:
            return Response(
                {
                    'success': False,
                    'message': '',
                    'error': e.__str__(),
                },
                status=status.HTTP_403_FORBIDDEN
            )


class Login(APIView):
    """
    API view for user authentication
    """

    @permission_classes((AllowAny,))
    def post(self, request):
        try:
            '''phone'''
            email = request.data.get('email')
            '''password'''
            password = request.data.get('password')
            '''password authentication service'''
            return user_service.login(email=email, password=password)
        except Exception as e:
            return Response(
                {
                    'success': False,
                    'message': '',
                    'errors': e.__str__(),
                },
                status=status.HTTP_403_FORBIDDEN
            )
