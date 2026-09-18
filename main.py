from blog.modularizacion.datos import posts
from blog.modularizacion.validaciones import validar_post
from blog.modularizacion.formateador import listar_posts, buscar_por_titulo, filtrar_por_tag


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