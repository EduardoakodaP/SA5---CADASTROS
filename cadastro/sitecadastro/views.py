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
    # Recupere o usuário correspondente ao ID fornecido ou retorne um erro 404 se não encontrado
    usuario = get_object_or_404(Usuario, pk=usuario_id)
    
    if request.method == 'POST':
        # Processar os dados do formulário
        usuario.nome = request.POST['nome']
        usuario.data_nascimento = request.POST['data_nascimento']
        usuario.email = request.POST['email']
        usuario.pais_trabalho = request.POST['pais_trabalho']
        # Salvar as atualizações no banco de dados
        usuario.save()
        # Redirecionar para a página de detalhes do usuário ou para onde desejar
        return redirect('index')
    else:
        # Se não for uma solicitação POST, renderize o template de atualização de cadastro com o usuário correspondente
        return render(request, 'atualizar_cadastro.html', {'usuario': usuario})
  
from django.http import JsonResponse

def deletar_cadastro(request, usuario_id):
    try:
        # Obtém o objeto de modelo correspondente ao ID do usuário
        usuario = Usuario.objects.get(id=usuario_id)
        # Exclui o objeto do banco de dados
        usuario.delete()
        # Retorna uma resposta JSON indicando sucesso
        return JsonResponse({'message': 'Cadastro excluído com sucesso'}, status=200)
    except Usuario.DoesNotExist:
        # Retorna uma resposta JSON indicando erro
        return JsonResponse({'message': 'Usuário não encontrado'}, status=404)

def pesquisar_cadastros(request):
    usuarios = Usuario.objects.all()
    return render(request, 'pesquisar_cadastro.html', {'usuarios': usuarios})