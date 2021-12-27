from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from .models import Directory, DirectoryItem
from .serializers import DirectorySerializer, DirectoryItemSerializer


def info(request):
    directories = Directory.objects.order_by('name').all()
    return render(
        request, 'form/info.html',
        {
            'directories': directories
        }
        )


class DirectoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Directory.objects.all()
    serializer_class = DirectorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Directory.objects.all()
        date = self.request.query_params.get('date')
        if date is not None:
            queryset = queryset.filter(start_date__gte=date)
        return queryset


class DirectoryItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DirectoryItem.objects.all()
    serializer_class = DirectoryItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = DirectoryItem.objects.all()
        version = self.request.query_params.get('version')
        name = self.request.query_params.get('name')
        if name is not None and version is not None:
            queryset = queryset.filter(directory__name=name).filter(directory__version=version)
        return queryset
