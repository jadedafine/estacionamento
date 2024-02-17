from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from estacionamento.api.serializers import ClienteSerializer, CarroSerializer, VagaEstacionamentoSerializer, PagamentoSerializer

from estacionamento.models import Cliente, Carro, VagaEstacionamento, Pagamento

class ClienteViewSet(ModelViewSet):
    serializer_class = ClienteSerializer
    permission_classes = [AllowAny]
    queryset = Cliente.objects.all()
    
class CarroViewSet(ModelViewSet):
    serializer_class = CarroSerializer
    permission_classes = [AllowAny]
    queryset = Carro.objects.all()

class VagaEstacionamentoViewSet(ModelViewSet):
    serializer_class = VagaEstacionamentoSerializer
    permission_classes = [AllowAny]
    queryset = VagaEstacionamento.objects.all()

class PagamentoViewSet(ModelViewSet):
    serializer_class = PagamentoSerializer
    permission_classes = [AllowAny]
    queryset = Pagamento.objects.all()
    
    
    