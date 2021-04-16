from datetime import datetime
from django.utils.timesince import timesince
from rest_framework import serializers
from news.models import Article


class ArticleSerializer(serializers.ModelSerializer):

    time_since_publication= serializers.SerializerMethodField()

    class Meta:
        model= Article
        fields = "__all__"

    def get_time_since_publication(self, object):
        publication_date= object.publication_date
        now= datetime.now()
        time_difference= timesince(publication_date, now)
        return time_difference     