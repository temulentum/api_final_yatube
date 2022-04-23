from posts.models import Comment, Follow, Group, Post, User
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator


class FollowSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(queryset=User.objects.all(
    ), slug_field='username', default=serializers.CurrentUserDefault())
    following = SlugRelatedField(
        queryset=User.objects.all(), slug_field='username')

    class Meta:
        fields = '__all__'
        model = Follow

        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following')
            )
        ]

    def validate(self, data):
        if data['user'] == data['following']:
            raise serializers.ValidationError(
                'Имя не может совпадать с цветом!')
        return data


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
    post = serializers.PrimaryKeyRelatedField(read_only=True, required=False)

    class Meta:
        fields = ('__all__')
        model = Comment


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('__all__')
        model = Group
