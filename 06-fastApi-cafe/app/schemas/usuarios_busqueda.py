


def usuarios_busqueda(usuarios):
    
    arreglo_usuarios = []
    print('hola', usuarios)
    for us in usuarios:
        print(us)
        id_str = str(us['_id'])
        del us['_id']
        del us['password']
        arreglo_usuarios.append({
        '_id': id_str,
        **us
    })
    
    #Puede ser un arreglo de objetos o diccionarios
    
    return arreglo_usuarios
    