try:
    import sys
except:
    raise Exception("Library sys not found, please consider reinstalling Python enviroment")

def read_from_file(filename):
    file = open(filename,mode="r", encoding='utf8')
    struct = []
    for line in file:
        temp = line.split(";")
        temp.pop(len(temp)-1) # Remove /n from the table
        struct.append(temp)
    file.close()
    return struct

def calculations(struct):
    i=0
    salary=[]
    for each in struct:
        if(struct[i][1]=="UoD"):
            if(struct[i][3]=="YES"):
                salary.append(float(struct[i][2]))
            else:
                salary.append(0)
        elif(struct[i][1]=="UZ"):
            bid=float(struct[i][2])
            hours=float(struct[i][3])
            salary.append(bid * hours)
        elif(struct[i][1]=="UoP"):
            basic_salary=float(struct[i][2])
            overtime_hours=float(struct[i][3])
            overtime_bid=float(struct[i][4])
            salary.append(basic_salary + overtime_hours * overtime_bid)
        i=i+1
    return salary

def write_file(struct, salary, output_file): 
    output=[]
    output.append(["Sum of salaries", sum(salary)])
    i=0
    file=open(output_file, mode="w", encoding="utf8")
    for each in struct:
        output.append([struct[i][0],salary[i]])
        i=i+1
    i=0
    for each in output:
        file.writelines(str(output[i]))
        file.writelines("\n")
        i=i+1
    file.close()
if __name__ == "__main__":
    struct = read_from_file(sys.argv[1])
    salary = calculations(struct)
    write_file(struct, salary, sys.argv[2])
