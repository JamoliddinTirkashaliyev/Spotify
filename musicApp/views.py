from django.shortcuts import get_object_or_404
from rest_framework import status, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.pagination import *


# class QoshiqchilarAPI(APIView):
#     def get(self, request):
#         qoshiqchilar = Qoshiqchi.objects.all()
#         serializers = QoshiqchiSerializers(qoshiqchilar, many=True)
#         return Response(serializers.data)
#
#     def post(self, request):
#         qoshiqchi = request.data
#         serializers = QoshiqchiSerializers(data=qoshiqchi)
#         if serializers.is_valid():
#             serializers.save()
#             return Response({'success': True, 'create_data': serializers.data})
#         return Response({'success': False, 'errors': serializers.errors})
#
#
# class QoshiqchiAPI(APIView):
#     def get(self, request, pk):
#         qoshiqchi = Qoshiqchi.objects.get(id=pk)
#         serializers = QoshiqchiSerializers(qoshiqchi)
#         return Response(serializers.data)
#
#     def put(self, request, pk):
#         qoshiqchi = Qoshiqchi.objects.filter(id=pk)
#         serializers = QoshiqchiSerializers(qoshiqchi.first(), data=request.data)
#         if serializers.is_valid():
#             data = serializers.validated_data
#             qoshiqchi.update(
#                 ism=data.get('ism'),
#                 tugilgan_yil=data.get('tugilgan_yil'),
#                 davlat=data.get('davlat'),
#             )
#             serializers = QoshiqchiSerializers(qoshiqchi.first())
#             return Response({'success': True, 'create_data': serializers.data})
#         return Response({'success': False, 'errors': serializers.errors})
#
#     def delete(self, request, pk):
#         aktyor = Qoshiqchi.objects.get(id=pk)
#         aktyor.delete()
#         return Response({'success': True, 'message':'qoshiqchi Ochirildi'})

# class QoshiqlarAPI(APIView):
#     def get(self, request):
#         qoshiqlar = Qoshiq.objects.all()
#         serializers = QoshiqSerializers(qoshiqlar, many=True)
#         return Response(serializers.data)
#
#     def post(self, request):
#         qoshiq = request.data
#         serializers = QoshiqSerializers(data=qoshiq)
#         if serializers.is_valid():
#             serializers.save()
#             return Response({'success': True, 'create_data': serializers.data})
#         return Response({'success': False, 'errors': serializers.errors})
#
class MyCustomPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 100


class AlbomModelViewSet(ModelViewSet):
    queryset = Albom.objects.all().order_by('sana')
    serializer_class = AlbomSerializers

    filter_backends = [filters.SearchFilter]
    search_fields = ['nom']

    pagination_class = MyCustomPagination

    @action(detail=True, methods=['get'])
    def qoshiqlar(self, request, pk):
        albom = self.get_object()
        qoshiq = Qoshiq.objects.filter(albom=albom)
        serializer = AlbomSerializers(qoshiq, many=True)
        return Response(serializer.data)


class QoshiqchilarModelViewSet(ModelViewSet):
    queryset = Qoshiqchi.objects.all().order_by('tugilgan_yil')
    serializer_class = QoshiqchiSerializers

    filter_backends = [filters.SearchFilter]
    search_fields = ['ism', 'davlat']

    pagination_class = MyCustomPagination

    @action(detail=True, methods=['get'])
    def albomlar(self, request, pk):
        qoshiqchi = self.get_object()
        albom = Albom.objects.filter(qoshiqchi=qoshiqchi)
        serializer = AlbomSerializers(albom, many=True)
        return Response(serializer.data)


class QoshiqlarModelViewSet(ModelViewSet):
    queryset = Qoshiq.objects.all().order_by('davomiylik')
    serializer_class = QoshiqSerializers

    filter_backends = [filters.SearchFilter]
    search_fields = ['nom', 'janr']

    pagination_class = MyCustomPagination
