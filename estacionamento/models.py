from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    endereco = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome
    
class Carro(models.Model):
    placa = models.CharField(max_length=20, unique=True)
    modelo = models.CharField(max_length=50)
    cor = models.CharField(max_length=50)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.modelo} - {self.placa}'

class VagaEstacionamento(models.Model):
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE)
    numvaga = models.PositiveIntegerField()
    ocupada = models.BooleanField(default=False)
    entrada = models.DateTimeField(auto_now_add = True)
    saida = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'Vaga {self.numvaga} - {self.carro}'
    
class Pagamento(models.Model):
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE)
    vaga = models.ForeignKey(VagaEstacionamento, on_delete=models.CASCADE)
    hora_entrada = models.DateTimeField(auto_now_add = True)
    hora_saida = models.DateTimeField(null=True, blank=True)
    valor = models.FloatField(null=True)
    
    def __str__(self):
        return f'Pagamento - {self.carro} - {self.vaga} - Entrada: {self.hora_entrada} - Saída: {self.hora_saida}'
