

def usuarios_busqueda(usuarios):

    arreglo_usuarios = []

    for us in usuarios:
        id_str = str(us['_id'])
        del us['_id']
        del us['password']
        arreglo_usuarios.append({
            '_id': id_str,
            **us
        })

    # Puede ser un arreglo de objetos o diccionarios

    return arreglo_usuarios


def categorias_busqueda(categorias):

    arreglo_categorias = []

    for cate in categorias:
        
        id_str = str(cate['_id'])
        del cate['_id']
        id_usuario = str(cate['usuario'])
        del cate['usuario']

        arreglo_categorias.append({
            '_id': id_str,
            '_id_usuario': id_usuario,
            **cate
        })
        
    return arreglo_categorias
