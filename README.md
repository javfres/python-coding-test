# CSV Masking

This is a python coding test I did in about 3 hours.

This script is used to hide sensible data from a CSV file.
The CVS has the following format:

```
ID | Nombre          | Email                          | Facturado | Localidad 
1  | Juan Martinez   | juan@mail.com                  | 15000     | Valladolid
2  | Francisco Gomez | paco@my-mail.com               | 20000     | Salamanca 
3  | Gerardo Puente  | gerardo-puente@mail-sample.com |           | Barcelona 
4  | Javier Cruz     | jcruz@mail.com                 | 12400.27  | Madrid    
5  | Fernando Martin | fm@mail.com                    | 53000     | Soria     
```

And it produces another one removing the name and email columns with X characters
and the numeric columns with its average value.
Example:

```
ID | Nombre          | Email                          | Facturado  | Localidad 
1  | XXXX XXXXXXXX   | XXXX@XXXX.XXX                  | 25100.0675 | Valladolid
2  | XXXXXXXXX XXXXX | XXXX@XX-XXXX.XXX               | 25100.0675 | Salamanca 
3  | XXXXXXX XXXXXX  | XXXXXXX-XXXXXX@XXXX-XXXXXX.XXX |            | Barcelona 
4  | XXXXXX XXXX     | XXXXX@XXXX.XXX                 | 25100.0675 | Madrid    
5  | XXXXXXXX XXXXXX | XX@XXXX.XXX                    | 25100.0675 | Soria     
```

Moreover, it produces a report for the 'Nombre' and 'Facturado' columns.

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

## Usage instructions

This script was made for python 3.6

`python3 ./main.py`


## Code files

The code has the following files

* `main.py`: Main script
* `csv.py`:  CSV class that reads, process, and saves CSV files
* `masking.py`: Marsking module for strings and numbers
* `utils.py`: Extra utilities used for the csv module
* `test.py`: Unit test



## Test

I have included a small unit test for the masking module.
Usage:

`python3 ./test.py`


# Notes

This script has several limitations, the main on is that the
csv parsing is manual. So, it doesn't support commas (',')
inside the string cells. I should be used the built-in csv module.

I have chosen to keep the null values when masking the numbers.
It would be necessary to discuss if that can be dangerous in a real case.

The code is commented and has TODO in things that could be improved.




