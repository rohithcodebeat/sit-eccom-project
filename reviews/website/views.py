from .serializers import WebsiteProductReviewModelCreateSerializer
from ..models import ProductReviewModel 
from rest_framework import generics, status, permissions
from rest_framework.response import Response 


class WebsiteProductReviewModelCreateAPIView(generics.CreateAPIView):
    queryset = ProductReviewModel.objects.all()
    serializer_class = WebsiteProductReviewModelCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request):
        serializer = self.serializer_class(data=request.data, context={"request" : request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        



