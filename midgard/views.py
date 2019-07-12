from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from midgard.models import Vols
from midgard.serializers import VolSerializer
# Create your views here.

@csrf_exempt
def vol_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        vols = Vols.objects.all()
        serializer = VolSerializer(vols, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = VolSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def vol_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        vol = Vols.objects.get(pk=pk)
    except Vols.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = VolSerializer(vol)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = VolSerializer(vol, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        vol.delete()
        return HttpResponse(status=204)