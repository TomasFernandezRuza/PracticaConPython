import json

from blog.modularizacion.modelos import Post


ARCHIVO_JSON = "posts.json"


def cargar_posts():
    try:
        with open(ARCHIVO_JSON, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        posts = []

        for dato in datos:
            post = Post.desde_diccionario(dato)
            posts.append(post)

        return posts

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []

    except (KeyError, TypeError):
        return []


def guardar_posts(posts):
    datos = []

    for post in posts:
        datos.append(post.a_diccionario())

    with open(ARCHIVO_JSON, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)