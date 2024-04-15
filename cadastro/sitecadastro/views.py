from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario


def index(request):
    ultimos_usuarios = Usuario.objects.order_by('-id')[:10]
    return render(request, 'index.html', {'ultimos_usuarios': ultimos_usuarios})
    

def criar_cadastro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        data_nascimento = request.POST.get('data_nascimento')
        email = request.POST.get('email')
        pais_trabalho = request.POST.get('pais_trabalho')
        usuario = Usuario.objects.create(nome=nome, data_nascimento=data_nascimento, email=email, pais_trabalho=pais_trabalho)
        
        usuario.save()
       
        success_message = "Usuário cadastrado com sucesso"
        return render(request, 'criar_cadastro.html', {'success_message': success_message, 'usuario': usuario})
    else:
        return render(request, 'criar_cadastro.html')

def atualizar_cadastro(request, usuario_id):
    usuario = get_object_or_404(Usuario, pk=usuario_id)
    
    if request.method == 'POST':
        usuario.nome = request.POST['nome']
        usuario.data_nascimento = request.POST['data_nascimento']
        usuario.email = request.POST['email']
        usuario.pais_trabalho = request.POST['pais_trabalho']
        # Salvar as atualizações no banco de dados
        usuario.save()
        return redirect('index')
    else:
        return render(request, 'atualizar_cadastro.html', {'usuario': usuario})
  
from django.http import JsonResponse

def deletar_cadastro(request, usuario_id):
    try:
        usuario = Usuario.objects.get(id=usuario_id)
        usuario.delete()
        return JsonResponse({'message': 'Cadastro excluído com sucesso'}, status=200)
    except Usuario.DoesNotExist:
       
        return JsonResponse({'message': 'Usuário não encontrado'}, status=404)

def pesquisar_cadastros(request):
    usuarios = Usuario.objects.all()
    return render(request, 'pesquisar_cadastro.html', {'usuarios': usuarios})