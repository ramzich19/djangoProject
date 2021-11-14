from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import serializers
from .models import Articles, BlogCategory
from .models import TopBack
from .models import FeedBack
from .models import Formback
from rest_framework.response import Response
from .serializers import TopBackSerializers
from .serializers import ArticlesSerializers
from .serializers import FormbackSerializers
from .serializers import FormSerializers
from .serializers import BlogPostListRetriveSerializer, BlogCategorySerializers, BlogCategoryDetailSerializers


class ArticlesView(generics.ListAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializers


class TopBackView(viewsets.ModelViewSet):
    queryset = TopBack.objects.all()
    serializer_class = TopBackSerializers


class FormbackView(viewsets.ModelViewSet):
    queryset = Formback.objects.all()
    serializer_class = FormbackSerializers


class FormView(viewsets.ModelViewSet):
    queryset = FeedBack.objects.all()
    serializer_class = FormSerializers


class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializers
    action_to_serializer = {
        "list": BlogPostListRetriveSerializer,
        "retrieve": BlogPostListRetriveSerializer,
    }
    def get_serializer_class(self):
        return self.action_to_serializer.get(
            self.action,
            self.serializer_class
        )



class BlogCategoryViewSet(viewsets.ModelViewSet):

    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializers

    action_to_serializer = {
        "retrieve": BlogCategoryDetailSerializers
    }
    def get_serializer_class(self):
        return self.action_to_serializer.get(
            self.action,
            self.serializer_class
        )
