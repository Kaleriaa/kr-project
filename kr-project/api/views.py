from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FindDomain
from .serializers import FindDomainSerializer
from re_domain.find_domains import find_domains


class FindDomainView(APIView):
    def get(self, request, text):
        searcher = FindDomain(text, find_domains(text))
        serializer_for_request = FindDomainSerializer(instance=searcher)
        return Response(serializer_for_request.data)
