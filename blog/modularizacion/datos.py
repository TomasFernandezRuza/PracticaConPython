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