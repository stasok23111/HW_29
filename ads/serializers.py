from rest_framework.fields import SerializerMethodField
from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer

from ads.models import Ad, Category
from users.models import User


class AdSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Ad


class AdListSerializer(ModelSerializer):
    author = SlugRelatedField(slug_field="username", queryset=User.objects.all())
    category = SlugRelatedField(slug_field="name", queryset=Category.objects.all())

    class Meta:
        exclude = ('description',)
        model = Ad


class AdAuthorSerializer(ModelSerializer):
    total_ads = SerializerMethodField()

    def get_total_ads(self, obj):
        return obj.ad_set.count()

    class Meta:
        exclude = ('password', 'role')
        model = User


class AdDetailSerializer(ModelSerializer):
    author = AdAuthorSerializer()
    category = SlugRelatedField(slug_field="name", queryset=Category.objects.all())

    class Meta:
        fields = '__all__'
        model = Ad


class CategoryListSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Category


class CategoryCreateSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Ad


class CategoryUpdateSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Ad


class CategorySerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Category
