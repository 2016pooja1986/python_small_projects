import os

def main():
    print("------------------------------------------------------------------")
    print("                     BANK MANGEMENT SYSTEM                        ")
    print("------------------------------------------------------------------")
    option={1:'New Customer',2:'Existing Customer',3:'Exit'}
    print("Please choose any one option")
    for i,j in option.items():
        print(i,". ",j)
    op=int(input("Enter the choice from 1 to 3 : "))
    services(op)
    
def new_customer():

    print("Enter the below information about new customer")
    ac_no = input("Account no.  :   ")
    file = ac_no + '.txt'
    if os.path.isfile(file) == True:
        print("Account number already exist")
    else:    
        f=open(file,'a')
        name = input("Customer_name :   ")
        add = input("Address        :   ")
        ph_no= int(input("Phone no. :   "))        
        gov_id = input("Govt. ID    :   ")         
        ac_type= input("Account type:   ")       
        amt = int(input("Amount(Rs) :   "))
        data ={ac_no:{'name':name,'address':add,'ph_no':ph_no,'gov_id':gov_id,'type':ac_type,'amount':amt}}
        f.write(str(data))
        f.close()
        print("File has created") 
        ch = input("More account to create (Y/N)? : ")
        if ch.upper()=='Y':
            new_customer()
            
def existing_customer():
    ac_no = input("Account no.  :   ")
    file = ac_no + '.txt'
    if os.path.isfile(file) == True:
        f=open(file,'r')
        data =f.read()
        data1=eval(data)
        f.close()
        print("Record found. Customer name : ",data1[ac_no]['name'])
        option1={1:'Check Balance',2:'Deposit',3:'Withdraw'}
        for i,j in option1.items():
            print(i,". ",j)
        op1=int(input("Enter the choice : "))
        sub_service(op1,data1,ac_no)        
    else:
        print("Record not found")
              
def sub_service(m,d,ac):
    amt = d[ac]['amount']
    if m ==1:
        print("Available Balance = Rs ",amt)
    if m==2:
        dep= int(input("Enter the amount to deposit = Rs "))
        amt += dep
        print("Deposite successful \n Available Balance = Rs ",amt,"\n------------------------------------------------------------------")
        d[ac]['amount']= amt
        file1 = ac + '.txt'
        os.remove(file1)
        f=open(file1,'a')
        f.write(str(d))
        f.close()
    if m==3:
        wid= int(input("Enter the amount withdraw = Rs "))
        amt -= wid
        print("Withdraw successful \n Available Balance = Rs ",amt,"\n------------------------------------------------------------------")
        d[ac]['amount']= amt
        file1 = ac + '.txt'
        os.remove(file1)
        f=open(file1,'a')
        f.write(str(d))
        f.close()    
    if m>3:
        print("Please enter the valid option")
        op2=int(input("Enter the choice : "))
        sub_service(op2,d,ac)
    
def services(n):
    if n ==1:
        new_customer()     
        
    if n==2:
        existing_customer()
    if n==3:
        exit()
    if n>3:
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




