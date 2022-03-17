from rest_framework import viewsets
from frontend.api.serializers import formSerializer
from frontend.models import form


class formView(viewsets.ModelViewSet):
    queryset = form.objects.all().order_by('-id')
    serializer_class = formSerializer
