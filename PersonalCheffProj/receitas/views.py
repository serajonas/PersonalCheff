from django.shortcuts import render

def index(request):
    receitas = {
        1: 'Suco de Melão',
        2: 'Pizza',
        3: 'Suco de Melancia',
        4: 'Suco de Abacaxi',
        5: 'Suco de Maracujá',
        6: 'Suco de Laranja',
        7: 'Suco de Acerola',
        8: 'Suco de Uva',
        9: 'Suco de Maça',
        10: 'Suco de Tamarino',

        }

    dados = {
        'lista_receitas' : receitas
        }

    return render(request,'index.html',dados)
    
def contato(request):
    return render(request,'contato.html')    

def sucodelaranja(request):
    return render(request,'sucodelaranja.html')

def sucodelimao(request):
    return render(request, 'sucodelimao.html')
