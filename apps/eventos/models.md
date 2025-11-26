## RELACIONES
1 evento -> muchas categorias (1:N)
1 categoria -> muchos eventos (1:N)
(n:m)

##### Uno a Muchos (1:m)
Un organizador puede tener muchos eventos. 
Pero cada evento tiene un único organizador.

```
                   (1:n)
|-----------|                |------|
|organizador|(1:1)      (1:n)|evento|       
|-----------|                |------|
```

##### Uno a Uno (1:1) 
Complemento o Detalle extendido de un registro.

Modelo X (parte princiapal), Modelo Y (extensión)

```
class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=100)

class Perfil(models.Model):
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE)
    descripcion = models.TextField()
    foto = models.ImageField()

class Carrito(models.Model):
    pass

class Pasaporte(models.Model):
    pass
```


## ORM (Conjunto de funcionalidades) -> CRUD (Create, Read, Update, Delete)

ORM Object Relational Mapper (Mapeador Objeto-Relacional)

Mysql-connector sqlite3 psycopg -> Escribiamos las sentencias SQL. 
cursor.execute("""
  SELECT * FROM tabla;
""")

**Los modelos nos conectan a la base de datos.**
**ORM nos permite trabajar con la base de datos usando Python.**