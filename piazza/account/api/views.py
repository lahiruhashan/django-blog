from django.http import JsonResponse

from account.api.serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser


@api_view(['POST',])
def register_view(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RegistrationSerializer(data=data)
        response = {}
        if serializer.is_valid():
            account = serializer.save()
            response['response'] = "Successfully registered a new user"
            response['email'] = account.email
            response['username'] = account.username
            token = Token.objects.get(user=account).key
            response['token'] = token
            return JsonResponse(response)
        return JsonResponse(serializer.errors, status=400)
