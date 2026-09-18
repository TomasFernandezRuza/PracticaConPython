# Datos del autor
perfil_autor = {
    "nombre": "Tomas Fernandez",
    "email": "tomas@email.com"
}

# Estados posibles de los posts
estados_post = ("borrador", "publicado", "archivado")

# Etiquetas disponibles
etiquetas_blog = {"python", "programacion", "tecnologia", "linux"}

# Lista de posts
posts = [
    {
        "id": 1,
        "titulo": "Aprendiendo Python",
        "contenido": "Python es un lenguaje de programación.",
        "autor": perfil_autor,
        "tags": ["python", "programacion"],
        "estado": "publicado"
    },
    {
        "id": 2,
        "titulo": "Introduccion a Linux",
        "contenido": "Linux es un sistema operativo.",
        "autor": perfil_autor,
        "tags": ["linux", "tecnologia"],
        "estado": "publicado"
    },
    {
        "id": 3,
        "titulo": "",
        "contenido": "Este post tiene un título vacío.",
        "autor": perfil_autor,
        "tags": ["python"],
        "estado": "borrador"
    }
]


# 1. Mostrar menú
def mostrar_menu():
    print("\n--- MENU DEL BLOG ---")
    print("1. Ver todos los posts")
    print("2. Buscar por titulo")
    print("3. Filtrar por tag")
    print("4. Validar posts")
    print("5. Salir")

    try:
        opcion = int(input("Elegí una opción: "))
        return opcion
    except ValueError:
        print("Error: tenés que ingresar un número.")
        return 0


# 2. Listar todos los posts
def listar_posts(lista):
    print("\n--- POSTS ---")

    for post in lista:
        titulo = post.get("titulo", "Sin titulo")
        autor = post.get("autor", {})

        if isinstance(autor, dict):
            nombre_autor = autor.get("nombre", "Autor desconocido")
        else:
            nombre_autor = "Autor incorrecto"

        print("Titulo:", titulo)
        print("Autor:", nombre_autor)
        print("--------------------")


# 3. Buscar por título
def buscar_por_titulo(lista, termino):
    if termino.strip() == "":
        print("Error: la búsqueda no puede estar vacía.")
        return

    encontrados = []

    for post in lista:
        titulo = post.get("titulo", "")

        if termino.lower() in titulo.lower():
            encontrados.append(post)

    if len(encontrados) == 0:
        print("No se encontraron posts.")
    else:
        listar_posts(encontrados)


# 4. Filtrar por tag
def filtrar_por_tag(lista, tag):
    if tag.strip() == "":
        print("Error: el tag no puede estar vacío.")
        return

    encontrados = []

    for post in lista:
        tags = post.get("tags", [])

        if isinstance(tags, list):
            for etiqueta in tags:
                if tag.lower() == etiqueta.lower():
                    encontrados.append(post)
                    break

    if len(encontrados) == 0:
        print("No se encontraron posts con ese tag.")
    else:
        listar_posts(encontrados)


# 5. Validar un post
def validar_post(post):
    if not isinstance(post, dict):
        return False, "El post no es un diccionario"

    claves_obligatorias = [
        "id",
        "titulo",
        "contenido",
        "autor",
        "tags",
        "estado"
    ]

    for clave in claves_obligatorias:
        if clave not in post:
            return False, "Falta la clave: " + clave

    if post.get("titulo", "").strip() == "":
        return False, "El titulo está vacío"

    if post.get("contenido", "").strip() == "":
        return False, "El contenido está vacío"

    autor = post.get("autor")

    if not isinstance(autor, dict):
        return False, "El autor debe ser un diccionario"

    if "nombre" not in autor:
        return False, "Falta el nombre del autor"

    if not isinstance(post.get("tags"), list):
        return False, "Tags debe ser una lista"

    if post.get("estado") not in estados_post:
        return False, "El estado no es válido"

    return True, "Post válido"


# Programa principal
if __name__ == "__main__":

    while True:

        opcion = mostrar_menu()

        if opcion == 1:
            listar_posts(posts)

        elif opcion == 2:
            termino = input("Ingresá el título a buscar: ")
            buscar_por_titulo(posts, termino)

        elif opcion == 3:
            tag = input("Ingresá el tag a buscar: ")
            filtrar_por_tag(posts, tag)

        elif opcion == 4:
            print("\n--- VALIDACION DE POSTS ---")

            for post in posts:
                valido, mensaje = validar_post(post)

                print(
                    "Post",
                    post.get("id", "sin ID"),
                    ":",
                    mensaje
                )

        elif opcion == 5:
            print("Programa finalizado. ¡Hasta luego!")
            break

        elif opcion != 0:
            print("Opción inexistente. Elegí entre 1 y 5.")