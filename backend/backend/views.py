from rest_framework import response, generics, permissions,status


class HomeAPIView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        return response.Response(request.data, status=status.HTTP_200_OK)
    
    def get(self, request, *args, **kwargs):
        return response.Response(request.data, status=status.HTTP_200_OK)
