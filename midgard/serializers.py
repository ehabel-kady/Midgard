from midgard.models import Vols, statut_choices, capteurs_choices
from rest_framework import serializers
from django.contrib.auth.models import User

class VolSerializer(serializers.ModelSerializer):
    # # date_du_vol = serializers.DateTimeField(auto_now_add=True)
    # id = serializers.IntegerField(read_only=True)
    # nome = serializers.CharField(max_length=50, allow_blank=True, default='')
    # case = serializers.CharField(max_length=100, allow_blank=True, default='')
    # statut = serializers.ChoiceField(choices=statut_choices, default='Prévu')
    # capteurs = serializers.ChoiceField(choices=capteurs_choices, default='Optique')

    # def create(self, validated_data):
    #     """
    #     Create and return a new `Snippet` instance, given the validated data.
    #     """
    #     return Vols.objects.create(**validated_data)
    
    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Snippet` instance, given the validated data.
    #     """
    #     # instance.date_du_vol = validated_data.get('date_du_vol', instance.date_du_vol)
    #     instance.nome = validated_data.get('nome', instance.nome)
    #     instance.case = validated_data.get('case', instance.case)
    #     instance.statut = validated_data.get('statut', instance.statut)
    #     instance.capteurs = validated_data.get('capteurs', instance.capteurs)
    #     instance.save()
    #     return instance
    class Meta:
        model = Vols
        fields = ('id', 'image', 'date_du_vol', 'nome', 'case', 'statut', 'capteurs')

class UserSerializer(serializers.ModelSerializer):
    vols = serializers.PrimaryKeyRelatedField(many=True, queryset=Vols.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'vols')