# flink-crud-fa

Servicio CRUD de simbolos para prueba de flink, escrito en python y fastapi.

Se uso la arquitectura hexagonal para fines demostrativos no porque realmente el caso de uso lo amerite, sino
simplemente mostrar lo escalables que pueden ser los sistemas bajo esta arquitectura.

## Requerimientos

* python 3.8
* fastapi

## Instrucciones

### Metodo 1
Se puede usar docker, crear la imagen y correr el contenedor 
```
sudo docker build -t flink-test-crud-fa .
```
y luego
```
sudo docker run -it -d --name flink-test-crud -p 8080:8080 flink-test-crud-fa:latest
```
### Metodo 2
o se puede clonar el repo y ejecutar
```
python pip install -r requirements.txt
```
y luego

```
python main.py
```

## Uso local

Ir a un postman o cualqueir cliente rest y usar el base path: 
```
localhost:8080/v1
```
#### los endpoints son:

para traer todos
```
/symbol  [GET]
```

para traer uno en especifico
```
/symbol/{symbol_id}  [GET]
```

para crear uno nuevo
```
/symbol  [POST]
```
con el payload, no es necesario especificar el uid, este se auto genera:
```
{
    "company_description": "nvidia corporation",
    "company_name": "nvidia",
    "market_values": "30,50,60,100,10",
    "symbol": "NVDA"
}
```

para borrar un simbolo
```
/symbol/{symbol_id}  [DELETE]
```

## Uso en la nube

Lo unico que cambia es el base path, por:
```
https://th6dwh.deta.dev/v1
```