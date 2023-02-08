from django.http import JsonResponse
from archa.serializers import UserSerializer, CardSerializer, AdminCardSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet
from rest_framework.generics import RetrieveAPIView
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, ListModelMixin
from rest_framework.permissions import IsAuthenticated
from archa.models import Card

class MeView(RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

class CardViewSet(ReadOnlyModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.card_set

class AdminCardViewSet(RetrieveModelMixin, UpdateModelMixin, ListModelMixin, GenericViewSet):
    queryset = Card.objects.all()
    serializer_class = AdminCardSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Card.objects.filter(company__permission__user=self.request.user, company__permission__level="admin")
