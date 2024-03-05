# propiedades-alpes-inseparables

## Instrucciones para el despliegue
1. En gitpod, crear un workspace con el código del repositorio
2. En la terminarl de gitpod, ejecutar el comando:
```gp validate```
3. En una nueva terminal en gitpod, ejecutar el comando que permite subir el perfil de pulsar:
```docker-compose --profile pulsar up --build -d```
4. Cada uno de los microservicios se pueden subir de manera independiente con los siguientes comandos:
```flask --app src/mercadoalpes/api run -p 5000```
```flask --app src/propiedadesalpes/api run -p 5001```
```flask --app src/clientesalpes/api run -p 5002```


## Instrucciones para la ejecución
Tenga en cuenta las URL y puertos suministrados por GitPod para la ejecición de la prueba
* Ejecutar la siguiente instrucción para crear un cliente propietario con una propiedad
```curl --location '{{url_servicio_mercado_gitpod}}/cliente/cliente-asincrona' \--header 'Content-Type: application/json' \--data '"id_cliente": "1", "nombre_cliente": "Nombre cliente", "tipo_cliente": "Propietario", "propiedad": { "id_propiedad": "82b98179-6971-43d6-ada6-8c28d85e2c59", "nombre_propiedad" : "Nombre propiedad", "estado_propiedad":"LIBRE", "cliente_propiedad": "1" }'```

* Ejecutar la siguiente instrucción para crear una transaccion sobre una propiedad
```curl --location '{{url_servicio_mercado_gitpod}}/propiedades/transaccion' \--header 'Content-Type: application/json' \--data '{"id_propiedad":"a10636ff-6783-46c6-a359-60581f22a80b", "tipo_transaccion":"VENTA"}'```




