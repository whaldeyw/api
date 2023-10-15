from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated

from .models import Chat
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializer import ChatSerializer


# Create your views here.

# class ChatApiView(generics.ListAPIView):
#     queryset = Chat.objects.all()
#     serializer_class = ChatSerializer

class ChatAPIList(generics.ListCreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class ChatAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (IsAuthenticated, )
    # authentication_classes = (TokenAuthentication, )


class ChatAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (IsAdminOrReadOnly, )
