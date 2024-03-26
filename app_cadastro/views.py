from django.shortcuts import render
from .models import User
# Create your views here.
def home(request):
    return render(request,'users/home.html')

def users(request):
    #Salvar os dados da tela para o banco de dados
    new_user = User()
    new_user.name = request.POST.get('name')
    new_user.password = request.POST.get('password')
    new_user.save()
    #Exibir todos os usuarios ja cadastrados em uma nova pagina
    users = {
        'users': User.objects.all()
    }
    # Retornar os dados para a pagina de listagem de usuarios
    return render(request, 'users/users.html', users)

