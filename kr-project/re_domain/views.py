from django.shortcuts import render
from django.http import HttpResponse

from re_domain.find_domains import find_domains

def index(request, s):
    return HttpResponse(f"{s}: {find_domains(s)}")
