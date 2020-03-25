from rest_framework.generics import ListAPIView

from scouter.serializers import ProblemSerializer


class ProblemList(ListAPIView):
    serializer_class = ProblemSerializer
