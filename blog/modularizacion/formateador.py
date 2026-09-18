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