from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.views import Response
from.serializers import UserSerializer, NoteSerializer, UserItemSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note, UserItem

class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)

class NoteDelete(generics.CreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)
    
# Create your views here.
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


# UserItem Stuff----------------------------------------------------
class AddItemView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = UserItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserItemsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        items = UserItem.objects.filter(user=request.user)
        serializer = UserItemSerializer(items, many=True)
        return Response(serializer.data)