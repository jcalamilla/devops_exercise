## Construyendo imagen apartir de un Dockerfile

```
docker build -t <TAG> .
```

## Corriendo imagen

```
docker run -p 5000:5000 -d <IMAGE_NAME>
```

## Probando imagen

1. Prueba dentro del contenedor.
```
docker exec -it <CONTAINER_ID> /bin/sh

localhost:5000

Resultado: Hello World!!!
```

**NOTA: Para probar dentro del contenedo es necesario instalar el "curl"**

2. Prueba en Localhost.
```
localhost:5000

Resultado: Hello World!!!
```