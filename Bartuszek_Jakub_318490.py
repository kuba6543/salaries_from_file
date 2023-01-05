try:
    import sys
except:
    raise Exception("Library sys not found, please consider reinstalling Python enviroment")

def read_data_from_a_file(filename):
    file = open(filename,mode="r", encoding='utf8')
    database = []
    for line in file:
        temp = line.split(";")
        temp.pop(len(temp)-1) # Remove /n from the table
        database.append(temp)
    file.close()
    return database

def calculate_salaries_from_database(database):
    i=0
    salaries=[]
    for each in database:
        if(database[i][1]=="UoD"):
            if(database[i][3]=="YES"):
                salaries.append(float(database[i][2]))
            else:
                salaries.append(0)
        elif(database[i][1]=="UZ"):
            bid=float(database[i][2])
            hours=float(database[i][3])
            salaries.append(bid * hours)
        elif(database[i][1]=="UoP"):
            basic_salaries=float(database[i][2])
            overtime_hours=float(database[i][3])
            overtime_bid=float(database[i][4])
            salaries.append(basic_salaries + overtime_hours * overtime_bid)
        i=i+1
    return salaries

def write_data_to_a_file(database, salaries, output_file): 
    output=[]
    output.append(["Sum of salaries", sum(salaries)])
    i=0
    file=open(output_file, mode="w", encoding="utf8")
    for each in database:
        output.append([database[i][0],salaries[i]])
        i=i+1
    i=0
    for each in output:
        file.writelines(str(output[i]))
        file.writelines("\n")
        i=i+1
    file.close()

if __name__ == "__main__":
    try:
        database = read_data_from_a_file(sys.argv[1])
    except:
        sys.exit("Input file not found, please write 'python Bartuszek_Jakub_318490.py <input_file_name> <optional_output_file_name>' in terminal")

    salaries = calculate_salaries_from_database(database)
    
    try:
        write_data_to_a_file(database, salaries, sys.argv[2])
    except:
        write_data_to_a_file(database, salaries, "a.out")