from .serializers import WebsiteOrderModelCreateSerializer, WebsiteOrderModelListSerializer , WebsiteOrderFromCartModelSerializer
from ..models import OrderModel 
from rest_framework import generics, status, permissions
from rest_framework.response import Response 


class WebsiteOrderModelCreateAPIView(generics.CreateAPIView):
    queryset = OrderModel.objects.all()
    serializer_class = WebsiteOrderModelCreateSerializer
    permission_classes = [permissions.IsAuthenticated] 

    def create(self, request):
        serializer = WebsiteOrderModelCreateSerializer(data=request.data, context={"request" : request})
        if serializer.is_valid():
            serializer.save()
            return Response({"message" : "Order created"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class WebsiteOrderModelFromCartCreateAPIView(generics.CreateAPIView):
    queryset = OrderModel.objects.all()
    serializer_class = WebsiteOrderFromCartModelSerializer
    permission_classes = [permissions.IsAuthenticated] 

    def create(self, request):
        serializer = WebsiteOrderFromCartModelSerializer(data=request.data, context={"request" : request})
        if serializer.is_valid():
            serializer.save()
            return Response({"message" : "Order created"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)