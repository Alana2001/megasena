from collections import UserString
import random
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from random import randint 

# Create your views here.
lista_numeros=[]
def geraRandomico(request):
    for i in range(1,7):
        numero = random.randint(1, 60)
        lista_numeros.append(numero)

    return HttpResponse(request, 'randomico', {'lista_numeros':lista_numeros})

def MegaSena(request):
    return render(request, 'loteria/MegaSena.html', {})

def ApostaClientesMega(request):
    return render(request, 'loteria/ApostaClientesMega.html', {})


def resultados(request):
	return render(request, 'loteria/resultados.html', {})

def cria_aposta(request):
	if request.method == 'POST':
		selected_values = request.POST.getlist('numeros')
		escolhido= request.POST.get('concursoselecionado')
		user = get_object_or_404(UserString, pk=request.user.id)
		aposta = ApostaClientesMega.objects.create(id_cliente=user,lista_numeros_apostados=selected_values[0], segundo_animal=selected_values[1], jogo=escolhido)
		aposta.save()
		return render(request, 'loteria/index.html', {})
	else:
		return render(request, 'loteria/ApostaClientesMega.html', {})


def verifica_resultado(request):
    if request.method == "POST":
        task = sorteio.objects.all()
        escolhido = request.POST.get("selecionado")
        sorteio = sorteio.objects.get(jogo=escolhido)
        apostas = apostas.objects.filter(jogo=sorteio)
        result = "Não foi dessa Vez!"
        if apostas and (
            (
                sorteio.lista_numeros == apostas.first().lista_numeros
                or sorteio.lista_numeros_apostados == apostas.first().lista_numeros_apostados
            )
        ):
            result = "Você ganhou!"
        return render(request, "loteria/resultados.html", {"result": result, "task": task})