import sys

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
                salary[i] = float(struct[i][2])
            else:
                salary[i] = 0
        elif(struct[i][1]=="UZ"):
            bid=float(struct[i][2])
            hours=float(struct[i][3])
            salary[i] = bid * hours
        elif(struct[i][1]=="UoP"):
            basic_salary=float(struct[i][2])
            overtime_hours=float(struct[i][3])
            overtime_bid=float(struct[i][4])
            salary[i] = basic_salary + overtime_hours * overtime_bid
        i=i+1
        
    return salary

def write_file(struct, salary, output_file): 
    output=[]
    sum_of_salaries=0
    for i in salary:
        sum_of_salaries += salary[i]
    output[0]=["Sum of salaries", sum_of_salaries]
    i=0
    if(output_file):    file=open(output_file, mode="w", encoding="utf8")
    else:               file=open("a.out", mode="w",encoding="utf8")
    for each in struct:
        file.writelines(output[i])
        output[i+1]=[struct[i][0],salary[i]]
        i=i+1
    file.close()

struct = read_from_file(sys.argv[1])
salary = calculations(struct)
write_file(struct, salary, sys.argv[2])
