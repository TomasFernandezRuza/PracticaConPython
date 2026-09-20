class Autor:
    def __init__(self, nombre, bio):
        self.nombre = nombre
        self.bio = bio

    def a_diccionario(self):
        return {
            "nombre": self.nombre,
            "bio": self.bio
        }

    @classmethod
    def desde_diccionario(cls, datos):
        return cls(
            datos["nombre"],
            datos["bio"]
        )


class Post:
    def __init__(self, id, titulo, contenido, autor, tags, estado):
        self.id = id
        self.titulo = titulo
        self.contenido = contenido
        self.autor = autor
        self.tags = tags
        self.estado = estado

    def a_diccionario(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "contenido": self.contenido,
            "autor": self.autor.a_diccionario(),
            "tags": self.tags,
            "estado": self.estado
        }

    @classmethod
    def desde_diccionario(cls, datos):
        autor = Autor.desde_diccionario(datos["autor"])

        return cls(
            datos["id"],
            datos["titulo"],
            datos["contenido"],
            autor,
            datos["tags"],
            datos["estado"]
        )


class Blog:
    def __init__(self, posts=None):
        self.posts = posts if posts is not None else []

    def agregar_post(self, post):
        self.posts.append(post)

    def listar_posts(self):
        return self.posts

    def buscar_por_titulo(self, texto):
        resultados = []

        for post in self.posts:
            if texto.lower() in post.titulo.lower():
                resultados.append(post)

        return resultados

    def filtrar_por_tag(self, tag):
        resultados = []

        for post in self.posts:
            tags_minusculas = []

            for etiqueta in post.tags:
                tags_minusculas.append(etiqueta.lower())

            if tag.lower() in tags_minusculas:
                resultados.append(post)

        return resultados