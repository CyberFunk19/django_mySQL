from django.http import JsonResponse
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .serializer import (StudentSerializer, Student)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)


        # Add custom claims
        token['username'] = user.username
        # ...


        return token




class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getNotes(request):
	return 'im protected'
        
        


def index(req):
    return JsonResponse('hello', safe=False)




def myProducts(req):
    all_products = StudentSerializer(Student.objects.all(), many=True).data
    return JsonResponse(all_products, safe=False)
