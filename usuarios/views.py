
from django.shortcuts import render

from .models import Usuario,Genero

# Create your views here.


def index(request):
    usuarios= Usuario.objects.all()
    context={"usuarios":usuarios}
    return render(request, 'usuarios/index.html', context)


def listadoSQL(request):
    usuarios= Usuario.objects.raw('SELECT * FROM usuarios_usuario')
    print(usuarios)
    context={"usuarios":usuarios}
    return render(request, 'usuarios/listadoSQL.html', context)

def crud(request):
    usuarios= Usuario.objects.all()
    context={"usuarios":usuarios}
    return render(request, 'usuarios/usuarios_list.html', context)

def usuariosAdd(request):
    if request.method is not "POST":
        generos=Genero.objects.all()
        context={'generos':generos}
        return render(request,'usuarios/usuarios_add.html',context)
    else:
        rut=        request.POST["rut"]
        nombre=     request.POST["nombre"]
        aPaterno=   request.POST["paterno"]
        aMaterno=   request.POST["materno"]
        fechaNac=   request.POST["fechaNac"]
        genero=     request.POST["genero"]
        telefono=   request.POST["telefono"]
        email=      request.POST["email"]
        direccion=  request.POST["direccion"]
        activo="1"
        objGenero=  Genero.objects.get(id_genero=genero)
        obj=        Usuario.objects.create(
            rut=rut,
            nombre=nombre,
            apellido_paterno=aPaterno,
            apellido_materno=aMaterno,
            fecha_nacimiento=fechaNac,
            id_genero=objGenero,
            telefono=telefono,
            email=email,
            direccion=direccion,
            activo=1
        )
        obj.save()
        context={'mensaje':"Datos grabados"}
        return render(request,'usuarios/usuarios_add.html',context)
    
def usuarios_del(request,pk):
    context={}
    try:
        usuario=    Usuario.objects.get(rut=pk)
        usuario.delete()
        mensaje="Datos eliminados"
        usuarios=   Usuario.objects.all()
        context={'usuarios':usuarios, 'mensaje':mensaje}
        return render(request, 'usuarios/usuarios_list.html',context)
    except:
        mensaje="Error, el rut no existe"
        usuarios=   Usuario.objects.all()
        context={'usuarios':usuarios,'mensaje':mensaje}
        return render(request,'usuarios/usuarios_list.html',context)
    
def usuarios_findEdit(request,pk):
    if pk != "":
        usuario=        Usuario.objects.get(rut=pk)
        generos=        Genero.objects.all()
        print(type(usuario.id_genero.genero))
        context={'usuario':usuario,'generos':generos}
        if usuario:
            return render(request, 'usuarios/usuarios_edit.html',context)
        else:
            context={'mensaje':"Error, rut inexistente"}
            return render(request, 'usuarios/usuarios_list.hmtml',context)
    
def usuariosUpdate(request):
    if request.method=="POST":
        rut=        request.POST["rut"]
        nombre=     request.POST["nombre"]
        aPaterno=   request.POST["paterno"]
        aMaterno=   request.POST["materno"]
        fechaNac=   request.POST["fechaNac"]
        genero=     request.POST["genero"]
        telefono=   request.POST["telefono"]
        email=      request.POST["email"]
        direccion=  request.POST["direccion"]
        activo="1"
        objGenero=  Genero.objects.get(id_genero=genero)

        usuario=Usuario()
        usuario.rut=rut
        usuario.nombre=nombre
        usuario.apellido_paterno=aPaterno
        usuario.apellido_materno=aMaterno
        usuario.fecha_nacimiento=fechaNac
        usuario.id_genero=objGenero
        usuario.telefono=telefono
        usuario.email=email
        usuario.direccion=direccion
        usuario.activo=1
        usuario.save()

        generos=        Genero.objects.all()
        context={'mensaje':"Datos actualizados ",'generos':generos,'usuario':usuario}
        return render(request,'usuarios/usuarios_edit.html',context)
    else:
        usuarios=       Usuario.objects.all()
        context={'usuarios':usuarios}
        return render(request,'usuarios/usuarios_list.hml',context)
