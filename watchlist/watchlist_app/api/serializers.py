from rest_framework import serializers
from watchlist_app.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    # default serializers need update and create mthods
    # but the model serialziers has its own methods
    class Meta:
        model = Movie
        fields = "__all__"
        
        # if we dont want active field. we dont need to pass fields if
        # we define exclude
        # exclude = ['active']

    # we need to define validate methods if we need them manually
    # field level validation
    def validate_name(self, value):
        if len(value) < 4:
            raise serializers.ValidationError("Name is too short!")
        else:
            return value

    # Object level validation
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError(
                "Name and Description should be different!")
        else:
            return data


# Validate by validators


# def name_length(value):
#     if len(value) < 4:
#         raise serializers.ValidationError("Name is too short!")
#     else:
#         return value


# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         # instance carries old values, validated_data is the new values
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get(
#             'description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance

    # field level validation
    # def validate_name(self, value):
    #     if len(value) < 4:
    #         raise serializers.ValidationError("Name is too short!")
    #     else:
    #         return value

    # Object level validation
    # def validate(self, data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError(
    #             "Name and Description should be different!")
    #     else:
    #         return data
