from rest_framework import serializers


class ProblemSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    problem_number = serializers.IntegerField(unique=True)
    title = serializers.CharField(max_length=180)
    slug = serializers.CharField(max_length=180)
    likes = serializers.IntegerField()
    dislikes = serializers.IntegerField()
    difficulty = serializers.IntegerField()
    accepted = serializers.IntegerField()
    submitted = serializers.IntegerField()

