# propiedades-alpes-inseparables

## Instrucciones para el despliegue
1. Descargar el repositorio
2. Ejecutar desde la raíz del proyecto:
```docker-compose up --build -d```


## Instrucciones para la ejecución
1. Ejecutar la siguiente instrucción para comandos
```curl --location 'http://127.0.0.1:5001/propiedades/transaccion' \--header 'Content-Type: application/json' \--data '{"id_propiedad":"a10636ff-6783-46c6-a359-60581f22a80b"}'```

2. Ejecutar la siguiente instrucción para queries
```curl --location 'http://127.0.0.1:5001/propiedades/transaccion' \--header 'Content-Type: application/json' \--data ''```

3. La cola de mensajes se puede monitorear en la dirección: http://localhost:15672/#/




