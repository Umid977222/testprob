from .models import Problems
from .serializers import ProblemSerializers
from rest_framework import viewsets, permissions


class ProblemViewSet(viewsets.ModelViewSet):
    """"""
    queryset = Problems.objects.all().order_by('product_model')
    serializer_class = ProblemSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
