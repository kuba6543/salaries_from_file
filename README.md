# Wykonywane zadanie: nr 1

## Description of programme:

Program will read data from file, count and show salaries of workers mentioned in file.

## Variables in programme:

* struct - struct of data, read from file
* salary - calculated salaries, ready to be written

## Functions in programme:

* read_from_file(filename) - reads a file and puts data into a list named "struct"
* calcualtions(struct) - calculates salaries from "struct" and puts calculations to list named "salary"
* write_file(struct, salary, output_file) - uses both lists "struct" and "salary" and writes to output_file (must be defined)
  
## Exemplary input and output:

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