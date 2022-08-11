## Construyendo imagen apartir de un Dockerfile

```
docker build -t <TAG> .
```

## Corriendo imagen

```
docker run -p 5000:5000 -d <IMAGE_NAME>
```

## Probando imagenapp

1. Prueba dentro del contenedor.
```
docker exec -it <CONTAINER_ID> /bin/sh

localhost:5000

Resultado: Hello World!!!
```

**NOTA: Para probar dentro del contenedo es necesario instalar el "curl"**

2. Prueba en Localhost.
```
curl localhost:5000

Resultado: Hello World!!!
```

3. Prueba en Localhost counter.
```
curl -X GET localhost:5000/counter

Resultado: No hay peticiones...
```

4. Prueba en Localhost counter.
```
curl -X POST localhost:5000/counter

Resultado: 1
```

5. Prueba en Localhost counter.
```
curl -X GET localhost:5000/counter

Resultado: Hay 1 peticiones...
```

## Probando k8s

1. Desplegar en kubernetes
```
kubectl apply -f k8s.yaml
```

2. Verificar el pod quede en estatus "Running"
```
kubectl get pod -n default
```

3. Hacer un port forward para probar la aplicacion en localhost
```
kubectl port-forward svc/devops-exercise <PORT-LOCALHOST>:<PORT-SERVICE>
``` 

4. Prueba en Localhost.
```
curl localhost:5000

Resultado: Hello World!!!
```

5. Prueba en Localhost counter.
```
curl -X GET localhost:5000/counter

Resultado: No hay peticiones...
```

6. Prueba en Localhost counter.
```
curl -X POST localhost:5000/counter

Resultado: 1
```

7. Prueba en Localhost counter.
```
curl -X GET localhost:5000/counter

Resultado: Hay 1 peticiones...
```