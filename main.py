from blog.modularizacion.modelos import Autor, Post, Blog
from blog.modularizacion.datos import cargar_posts, guardar_posts


def mostrar_posts(posts):
    if len(posts) == 0:
        print("No se encontraron posts.")
        return

    for post in posts:
        print("--------------------")
        print("Título:", post.titulo)
        print("Autor:", post.autor.nombre)
        print("Estado:", post.estado)


def crear_nuevo_post(blog):
    print("\n--- CREAR POST ---")

    titulo = input("Título: ").strip()
    contenido = input("Contenido: ").strip()
    nombre_autor = input("Nombre del autor: ").strip()
    bio = input("Bio del autor: ").strip()
    tags_texto = input("Tags separados por coma: ").strip()
    estado = input("Estado: ").strip()

    if titulo == "" or contenido == "" or nombre_autor == "":
        print("Error: título, contenido y autor son obligatorios.")
        return

    tags = []

    for tag in tags_texto.split(","):
        tag = tag.strip()

        if tag != "":
            tags.append(tag)

    autor = Autor(nombre_autor, bio)

    nuevo_id = len(blog.posts) + 1

    nuevo_post = Post(
        nuevo_id,
        titulo,
        contenido,
        autor,
        tags,
        estado
    )

    blog.agregar_post(nuevo_post)

    print("Post creado correctamente.")


def main():

    posts = cargar_posts()

    blog = Blog(posts)

    while True:

        print("\n--- MENU DEL BLOG ---")
        print("1. Ver todos los posts")
        print("2. Buscar por título")
        print("3. Filtrar por tag")
        print("4. Crear nuevo post")
        print("5. Validar posts")
        print("6. Guardar posts en JSON")
        print("7. Salir")

        opcion = input("Elegí una opción: ")

        if opcion == "1":

            mostrar_posts(blog.listar_posts())

        elif opcion == "2":

            titulo = input("Título a buscar: ")

            resultados = blog.buscar_por_titulo(titulo)

            mostrar_posts(resultados)

        elif opcion == "3":

            tag = input("Tag a buscar: ")

            resultados = blog.filtrar_por_tag(tag)

            mostrar_posts(resultados)

        elif opcion == "4":

            crear_nuevo_post(blog)

        elif opcion == "5":

            print("Validación de posts.")

            for post in blog.posts:

                if post.titulo == "" or post.contenido == "":
                    print("Post", post.id, "tiene errores.")

                else:
                    print("Post", post.id, "correcto.")

        elif opcion == "6":

            guardar_posts(blog.posts)

            print("Posts guardados correctamente.")

        elif opcion == "7":

            guardar_posts(blog.posts)

            print("Posts guardados.")
            print("Hasta luego.")

            break

        else:

            print("Opción incorrecta.")


if __name__ == "__main__":
    main()