# Url-reputation
## _SOC script tool_
 ![ logo](/img/logo.png "Logo")
Software creado con Python para la automatization de busqueda y analisis de reputacion de URL maliciosas; busca en bases de datos y crea una captura de pantalla, en conjunto de un reporte por consumo de API.
Bases de datos actuales:
- IBM X-force
- VirusTotal
- AbuseIPDB (proximamente)

## Funcionalidad

- Crea captura de pantalla 
- Crea texto de las API
- Guarda en la carpeta `reports`
- Abre automaticamente la carpeta del reporte

## Instalacion
Al tenerlo ya descargado, se procede a configurar el entorno:
```
python .\url-reputation.py --config 
o
python .\url-reputation.py -c 
```

Importante que esta funcion solo es posible en entornos Windows, por el momento.

## Uso
Se debe ingresar una URL en el argumento del programa
```
python .\url-reputation.py example.com
```
En caso de no ingresar la URL, el programa avisa y se cierra:
```
PS C:\url-reputation> python .\url-reputation.py
Usage:
python .\url-reputation.py TARGET
Example: python .\url-reputation.py google.com
PS C:\url-reputation>
```

## **Disclaimer**
**El programa aun esta en beta, por ende es posible que genere errores o atrasos en las tareas.**

 ![ asleep](/img/asleep.jpg "Logo")