import sys

def read_from_file(filename):
    file = open(filename,mode="r", encoding='utf8')
    struct = []
    for line in file:
        temp = line.split(";")
        temp.pop(len(temp)-1) # Remove /n from the table
        struct.append(temp)
    return struct

def calculations(struct):
    salary=[]
    for i in struct:
        if(struct[i][1]=="UoP"):
            salary[i] = float(struct[i][2]) + (float(struct[i][3]) * int(struct[i][4]))
        elif(struct[i][1]=="UZ"):
            salary[i] = float(struct[i][2]) * int(struct[i][3])
        elif(struct[i][1]=="UoD"):
            if(struct[i][3]=="YES"):
                salary[i] = int(struct[i][2])
            else:
                salary[i] = 0
    return salary

def write_file(struct, salary): 
    output=[]
    sum_of_salaries=0
    for i in salary:
        sum_of_salaries += salary[i]
    output[0]=["Sum of salaries", sum_of_salaries]
    i=0
    for each in struct:
        output[i+1]=[struct[i][0],salary[i]]
    print(output)

struct = read_from_file(sys.argv[1])
salary = calculations(struct)
write_file(struct, salary)