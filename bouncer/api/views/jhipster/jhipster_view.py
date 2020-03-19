from .create_file import create_file
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class JhipsterView(APIView):
        def post(self, request):
                data = request.data

                try:
                        return Response(create_file(data))

                except:
                        return Response(dict(error="OOPS!, Something went wrong"), status=status.HTTP_400_BAD_REQUEST)