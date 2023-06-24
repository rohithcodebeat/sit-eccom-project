from rest_framework import generics, status, permissions
from rest_framework.response import Response 
from .serializers import DashboardOrderModelUpdateSerializer
from ..models import OrderModel


class DashboardOrderModelUpdateGenericAPIView(generics.GenericAPIView):
    queryset = OrderModel.objects.all()
    serializer_class = DashboardOrderModelUpdateSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    def put(self, request, id):
        queryset = self.queryset.get(pk=id)
        serializer = self.serializer_class(data=request.data, instance=queryset)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

