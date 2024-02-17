from rest_framework import serializers
from estacionamento.models import Cliente, Carro, VagaEstacionamento, Pagamento

class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields = "__all__"

class CarroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Carro
        fields = "__all__"

class VagaEstacionamentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = VagaEstacionamento
        fields = "__all__"

class PagamentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pagamento
        fields = "__all__"