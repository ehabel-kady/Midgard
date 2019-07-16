from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from rest_framework.parsers import JSONParser
from midgard.models import Vols
from midgard.serializers import VolSerializer, UserSerializer
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from rest_framework.response import Response
from midgard.permissions import IsOwnerOrReadOnly
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework import permissions
from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.core.mail import send_mail, BadHeaderError

from .forms import SignUpForm, ContactForm
User = get_user_model()
# Create your views here.

class VolList(APIView):
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    def get(self, request, format=None):
        snippets = Vols.objects.all()
        serializer = VolSerializer(snippets, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = VolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class VolDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Vols.objects.get(pk=pk)
        except Vols.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = VolSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = VolSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)


class VolsView(TemplateView):
    template_name = "vols.html"

    def get(self,request, *args, **kwargs):
        vols = Vols.objects.all().order_by('id')
        context = {
            'vols': vols,
        }
        return render(request, self.template_name, context)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserInfo(generics.RetrieveAPIView):
    template_name = "userinfo.html"
    def get(self,request, *args, **kwargs):
        queryset = User.objects.all()
        context = {
            'users': queryset,
        }
        print(queryset[1].vols)
        return render(request, self.template_name, context)
class IndexView(TemplateView):
    template_name = "home.html"

    def get(self,request, *args, **kwargs):
        context = {
        }
        return render(request, self.template_name, context)
@csrf_protect
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/home')
    else:
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['ehabwork0@gmail'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('thanks')
        else:
            return HttpResponse('Invalid.')
    return render(request, "contact.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')
