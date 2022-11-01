from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from django.shortcuts import render

def index(request):
    return render(request, 'base.html')

class GetScore(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request):
        input_score = request.query_params.get("score")
        # return error if unable convert to float
        try:
            input_score = float(input_score)
        except:
            return Response({"Error":"Please enter a numeric value!"}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({"Result":input_score+1})