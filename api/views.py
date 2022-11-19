from api.serializers import ProjectSerializer
from rest_framework import viewsets, permissions
from accounts.models import Project
from api.permissions import IsOwnerOfObject

class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOfObject]
    queryset = Project.objects.all()
    serializer_class =ProjectSerializer
    
    def perform_create(self, serializer):
        serializer.save(username=self.request.user)
    




'''
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = [IsAuthenticated, IsOwnerOfObject]
    authentication_classes = (TokenAuthentication,)
'''