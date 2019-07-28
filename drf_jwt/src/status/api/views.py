from rest_framework import generics, mixins, permissions

from status.models import Status
from .serializers import StatusSerializer


class StatusAPIDetailView(
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.RetrieveAPIView
):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = StatusSerializer
    queryset = Status.objects.all()
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# Login required mixin /decorator
class StatusAPIView(
    mixins.CreateModelMixin,
    generics.ListAPIView
):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = StatusSerializer
    passed_id = None

    def get_queryset(self):
        request = self.request
        print(request.user)
        qs = Status.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
