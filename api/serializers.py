from rest_framework import serializers
from .models import Articles,BlogCategory
from .models import TopBack
from .models import Formback
from .models import FeedBack



class ArticlesSerializers(serializers.ModelSerializer):

    class Meta:
        model = Articles
        fields = '__all__'


class TopBackSerializers(serializers.ModelSerializer):

    class Meta:
        model = TopBack
        fields = '__all__'


class FormbackSerializers(serializers.ModelSerializer):

    class Meta:
        model = Formback
        fields = '__all__'


class FormSerializers(serializers.ModelSerializer):

    class Meta:
        model = FeedBack
        fields = '__all__'


class BlogPostListRetriveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Articles
        fields = '__all__'


class BlogCategorySerializers(serializers.ModelSerializer):


    class Meta:
        model = BlogCategory
        fields = '__all__'


class BlogCategoryDetailSerializers(serializers.ModelSerializer):
    posts = serializers.SerializerMethodField()

    class Meta:
        model = BlogCategory
        fields = '__all__'

    @staticmethod
    def get_posts(obj):
        return ArticlesSerializers(Articles.objects.filter(blog_category=obj),many=True).data
