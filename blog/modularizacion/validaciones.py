from .datos import estados_post

from .datos import estados_post


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