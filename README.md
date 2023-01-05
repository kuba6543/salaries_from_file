# Wykonywane zadanie: nr 1

## Description of programme:

Program will read data from file, count and show salaries of workers mentioned in file.

## Variables in programme:

* database - database of data, read from file
* salaries - calculated salaries, ready to be written

## Functions in programme:

* read_data_from_a_file(filename) - reads a file and puts data into a list named "database"
* calculate_salaries_from_database(database) - calculates salaries from "database" and puts calculations to list named "salaries"
* write_data_to_a_file(database, salaries, output_file) - uses both lists "database" and "salaries" and writes to output_file (may be defined, if not, the output data is saved to a.out file in the same directory)
  
## Exemplary input and output:
input.txt used from main repository folder

```
python Bartuszek_Jakub_318490.py input.txt output.txt
```

output.txt
```
['Sum of salaries', 20475.4]
['Łukasz Stanisławowski', 7300.0]
['Marcin Osadowski', 8975.4]
['Aleksander Jabłonowski', 4200.0]

```
python Bartuszek_Jakub_318490.py input.txt
```

a.out
```
['Sum of salaries', 20475.4]
['Łukasz Stanisławowski', 7300.0]
['Marcin Osadowski', 8975.4]
['Aleksander Jabłonowski', 4200.0]
```
