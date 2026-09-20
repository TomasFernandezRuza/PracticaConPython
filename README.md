# Blog de consola

Proyecto desarrollado en Python para administrar publicaciones de un blog desde la consola.

## Funcionalidades

El programa permite:

- Ver todos los posts.
- Buscar posts por título.
- Filtrar posts por tag.
- Crear nuevos posts.
- Validar posts.
- Guardar los posts en un archivo JSON.

## Programación Orientada a Objetos

El proyecto utiliza tres clases principales:

### Autor

Representa al autor de una publicación y contiene su nombre y biografía.

### Post

Representa una publicación del blog. Contiene un título, contenido, autor, tags y estado.

### Blog

Administra la lista de posts y permite realizar operaciones como listar, buscar, filtrar y agregar publicaciones.

## Persistencia con JSON

Los posts se guardan en el archivo `posts.json`.

Antes de guardar los objetos, estos se convierten en diccionarios.

Al iniciar el programa, los datos de `posts.json` se cargan y se convierten nuevamente en objetos.

## Ejecución

Para ejecutar el programa:

py main.py

## Cambios respecto a la entrega anterior

Se incorporó Programación Orientada a Objetos mediante las clases Autor, Post y Blog.

También se agregó persistencia de datos utilizando JSON.