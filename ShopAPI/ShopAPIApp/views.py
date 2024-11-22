from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Good, Token
from .serializers import GoodSerializer
from django.http import HttpResponse
from .models import Good
from .forms import GoodForm

def home(request):
    return HttpResponse("Welcome to the Shop API!")

class TokenView(APIView):
    def get(self, request):
        token = Token.objects.create()
        return Response({"token": str(token.token)}, status=status.HTTP_200_OK)

class GoodsListView(APIView):
    def get(self, request):
        token = request.query_params.get('token')
        if not token:
            return Response("Token must be present", status=status.HTTP_401_UNAUTHORIZED)

        try:
            Token.objects.get(token=token)
        except Token.DoesNotExist:
            return Response("Token is invalid", status=status.HTTP_401_UNAUTHORIZED)

        goods = Good.objects.all()
        serializer = GoodSerializer(goods, many=True)
        return Response(serializer.data)

class NewGoodView(APIView):
    def post(self, request):
        token = request.query_params.get('token')
        if not token:
            return Response("Token must be present", status=status.HTTP_401_UNAUTHORIZED)

        try:
            Token.objects.get(token=token)
        except Token.DoesNotExist:
            return Response("Token is invalid", status=status.HTTP_401_UNAUTHORIZED)

        serializer = GoodSerializer(data=request.data)
        if serializer.is_valid():
            price = serializer.validated_data['price']
            amount = serializer.validated_data['amount']
            if price <= 0:
                return Response("Price must be more than 0", status=status.HTTP_400_BAD_REQUEST)
            if amount <= 0:
                return Response("Amount must be more than 0", status=status.HTTP_400_BAD_REQUEST)

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
