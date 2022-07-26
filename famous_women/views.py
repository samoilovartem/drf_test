from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated

from .models import FamousWomen, Category
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import FamousWomenSerializer
from .pagination import FamousWomenApiListPagination


# class FamousWomenViewSet(viewsets.ModelViewSet):
#     queryset = FamousWomen.objects.all()
#     serializer_class = FamousWomenSerializer
#
#     # def get_queryset(self):
#     #     pk = self.kwargs.get('pk')
#     #     if not pk:
#     #         return FamousWomen.objects.all()[:3]
#     #     return FamousWomen.objects.filter(pk=pk)
#
#     @action(methods=['get'], detail=False)
#     def category(self, request):
#         categories = Category.objects.all()
#         return Response({'categories': [category.name for category in categories]})


class FamousWomenApiList(generics.ListCreateAPIView):
    queryset = FamousWomen.objects.all()
    serializer_class = FamousWomenSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = FamousWomenApiListPagination


class FamousWomenApiUpdate(generics.RetrieveUpdateAPIView):
    queryset = FamousWomen.objects.all()
    serializer_class = FamousWomenSerializer
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication, )


class FamousWomenApiDestroyView(generics.RetrieveDestroyAPIView):
    queryset = FamousWomen.objects.all()
    serializer_class = FamousWomenSerializer
    permission_classes = (IsAdminOrReadOnly,)


# class FamousWomenApiView(APIView):
#     def get(self, request):
#         list_of_famous_women = FamousWomen.objects.all().values()
#
#         return Response({'posts': FamousWomenSerializer(list_of_famous_women,
#                                                         many=True).data})
#
#     def post(self, request):
#         serializer = FamousWomenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'post': serializer.data})
#
#     def put(self,  request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({"error": "Method PUT is not allowed"})
#
#         try:
#             instance = FamousWomen.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object doesn`t exist"})
#
#         serializer = FamousWomenSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})
