import os

def main():
    print("************ WELCOME TO STUDENT MANGEMENT SYSTEM ***************")
    print("==================================================================")
    option={1:'To view student list',2:'To add new to list',3:'To remove the data',4:'To search the data',5:'Exit'}
    print("Please choose any one option")
    for i,j in option.items():
        print(i,". ",j)
    op=int(input("Select an option from 1 to 5 : "))
    operation(op)
    
def operation(n):
    if n ==1:
        if os.path.isfile('student.txt') == True:
            f=open('student.txt','r')
            print(f.read())
            f.close()
        else:
            f=open('student.txt','w')
            f.close()
    if n==2:
        f=open('student.txt','a')
        stud_name = input("Enter the name of student to add ")
        f.write(stud_name + '\n')
        f.close()
        print("Data is added successfully")
    if n==3:
        f=open('student.txt','r')
        l=list(f.readlines())
        f.close()
        stud_name = input("Enter the name of student to delete ")
        l.remove(stud_name + '\n')                 
        f=open('student.txt','w')
        f.writelines(l)
        f.close()
        print("Data is deleted from file")
    if n ==4:
        f=open('student.txt','r')
        l=f.read()
        stud_name = input("Enter the name of student to search ")
        stud_name1 = stud_name + '\n'
        if stud_name1 in l:
            print(stud_name," is found")
        else:
            print(stud_name," not found")
        f.close()
       
    if n ==5 :
        exit()
    if n>5:
        print("Please enter the valid option")
        
    
    c = input("Do you want to continue Y or N ? ")
    again(c)
    
def again(a):    
    if a.upper()== 'Y':
        main()
    elif a.upper()== 'N':
        exit()
    else:
        print("Please enter the valid option")
        b = input("Do you want to continue Y or N ? ")
        again(b)
        

main()




