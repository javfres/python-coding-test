# CSV Masking

Script python para ocultar datos sensibles en un fichero CSV.
El script leer un fichero CSV del tipo:

```
ID | Nombre          | Email                          | Facturado | Localidad 
1  | Juan Martinez   | juan@mail.com                  | 15000     | Valladolid
2  | Francisco Gomez | paco@my-mail.com               | 20000     | Salamanca 
3  | Gerardo Puente  | gerardo-puente@mail-sample.com |           | Barcelona 
4  | Javier Cruz     | jcruz@mail.com                 | 12400.27  | Madrid    
5  | Fernando Martin | fm@mail.com                    | 53000     | Soria     
```

Y produce otro fichero eliminando los datos sensibles

```
ID | Nombre          | Email                          | Facturado  | Localidad 
1  | XXXX XXXXXXXX   | XXXX@XXXX.XXX                  | 25100.0675 | Valladolid
2  | XXXXXXXXX XXXXX | XXXX@XX-XXXX.XXX               | 25100.0675 | Salamanca 
3  | XXXXXXX XXXXXX  | XXXXXXX-XXXXXX@XXXX-XXXXXX.XXX |            | Barcelona 
4  | XXXXXX XXXX     | XXXXX@XXXX.XXX                 | 25100.0675 | Madrid    
5  | XXXXXXXX XXXXXX | XX@XXXX.XXX                    | 25100.0675 | Soria     
```

Además, produce un informe para las columnas Nombre y Facturado

```
Report for str column 'Nombre'
* avg 13.6
* max 15
* min 11
```

```
Report for numeric column 'Facturado'
* avg 25100.0675
* max 53000.0
* min 12400.27
```

## Instrucciones de ejecución

El script se ha programado para la versión 3.6 de python

`python3 ./main.py`


## Descripción de los archivos

El código se divide en módulos según los siguientes archivos:

* `main.py`: Fichero principal
* `csv.py`: Contine la clase CSV para leer, procesar y guardar ficheros CSV
* `masking.py`: Modulo con las funciones de masking para cadenas y listas de números
* `utils.py`: Utilidades extra usadas por el modulo csv
* `test.py`: Pruebas



## Test

Se ha incluido un pequeño test unitario para el modulo de masking

`python3 ./test.py`


# Notas

El script tiene ciertas limitaciones, la más grave posiblemente es que
el parsing del csv se hace de forma manual. Así que no soporta comas (',')
dentro de las celdas con string. Debería haber utilizado el modulo built-in
`csv`.

He optado por mantener los valores nulos dentro en el masking the números.

El código está comentado y tiene algún TODO en cosas que se podrían mejorar