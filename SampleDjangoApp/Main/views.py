from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import render

from Main.models import ScoreLog
from Main.serializers import ScoreLogSerializer

def index(request):
    return render(request, 'index.html')

class GetScore(APIView):

    # only allow authenticated user to access
    permission_classes = [IsAuthenticated]

    def get(self, request):
        input_score = request.query_params.get("score")
        
        # error checking: input type
        try:
            input_score = float(input_score)
        except:
            return Response({"Error":"Please enter a numeric value!"}, status=status.HTTP_400_BAD_REQUEST)
        
        # processing the input
        output_score = input_score + 1

        # saving output to db
        ScoreLog.objects.create(user=request.user, score=output_score)

        return Response({"Result":output_score})

class ScoreLogViewSet(viewsets.ModelViewSet):

    queryset = ScoreLog.objects.all()
    serializer_class = ScoreLogSerializer