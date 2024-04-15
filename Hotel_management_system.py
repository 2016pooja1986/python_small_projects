import os

def main():
   
    print("******************WELCOME TO COUNTRY INN HOTEL****************")
    print(" ")
    option={1:'Enter customer data ',2:'Calculate roomrent',
            3:'Calculate restaurant bill',4:'Calculate laundry bill',
            5:'calculate game bill',6:'Show total cost',7:'Exit'}
    print("Please choose any one option")
    for i,j in option.items():
        print(i,". ",j)
    op=int(input("Enter the choice from 1 to 7 : "))
    services(op)
    
def customer():
    rm = input("Room no  :   ")
    file = rm + '.txt'
    if os.path.isfile(file) == True:
        print("Room number already booked")
    else:    
        f=open(file,'a')
        name = input("Customer_name  :   ")
        add = input("Address         :   ")
        ph_no= int(input("Phone no.  :   "))        
        chk_in = input("Checkin date :   ")         
        chk_out= input("Checkout date:   ")       
        data ={rm:{'name':name,'address':add,'ph_no':ph_no,'Chk_in':chk_in,
                   'chk_out':chk_out,'rm_rent':0,'res_bill':0,'laund_bill':0
                   ,'game_bill':0,'tot_bill':0}}
        f.write(str(data))
        f.close()
        print("File has created") 
        ch = input("More booking of rooms (Y/N)? : ")
        if ch.upper()=='Y':
            customer()
           
def roomrent():
    rm = input("Room no  :   ")
    file = rm + '.txt'
    if os.path.isfile(file) == True:
        f=open(file,'r')
        data =f.read()
        data1=eval(data)
        f.close()
        print("Record found. Customer name : ",data1[rm]['name'])
        option1={1:'Type A (Rs 6000 per night)',2:'Type B (Rs 5000 per night)',
        3:'Type C (Rs 4000 per night)',4:'Type D (Rs 3000 per night)'}
        for i,j in option1.items():
            print(i,". ",j)
        op1=int(input("Enter the choice : "))
        if op1 == 1:
            day = int(input("No of nights did you stay : "))
            rm_rent = day * 6000
        if op1 == 2:
            day = int(input("No of nights did you stay : "))
            rm_rent = day * 5000
        if op1 == 3:
            day = int(input("No of nights did you stay : "))
            rm_rent = day * 4000
        if op1 == 4:
            day = int(input("No of nights did you stay : "))
            rm_rent = day * 3000    
        print("Room rent of room no ",rm," is Rs ",rm_rent)          
        data1[rm]['rm_rent']= rm_rent    
        os.remove(file)
        f=open(file,'a')
        f.write(str(data1))
        f.close()    
    else:
        print("Room is not booked")
               
def laundary_bill():
    rm = input("Room no  :   ")
    file = rm + '.txt'
    if os.path.isfile(file) == True:
        f=open(file,'r')
        data =f.read()
        data1=eval(data)
        f.close()
        print("Record found. Customer name : ",data1[rm]['name'])
        print("***************Laundary Menu*******************")
        option1={1:'shorts (Rs 3)',2:'Trousers (Rs 4)',
        3:'Shirt (Rs 5)',4:'Jeans (Rs 7)',
        5:'Girl Suit (Rs 8)',6:'Exit'}
        for i,j in option1.items():
            print(i,". ",j)    
        op1=0
        l_bill =data1[rm]['laund_bill']
        while op1 <6 and op1!=6:
            op1=int(input("Enter the choice : "))
            if op1<6:
                q = int(input("Enter the quantity : "))
                if op1 == 1:
                    l_bill += 3*q
                if op1 == 2:    
                    l_bill += 4*q
                if op1 == 3:
                    l_bill += 5*q
                if op1 == 4:    
                    l_bill += 7*q
                if op1 == 5:
                    l_bill += 8*q

        print("Laundary bill of room no ",rm," is Rs ",l_bill)          
        data1[rm]['laund_bill']= l_bill    
        os.remove(file)
        f=open(file,'a')
        f.write(str(data1))
        f.close()          
            
    else:
        print("Room is not booked")    
def restaurant_bill():
    rm = input("Room no  :   ")
    file = rm + '.txt'
    if os.path.isfile(file) == True:
        f=open(file,'r')
        data =f.read()
        data1=eval(data)
        f.close()
        print("Record found. Customer name : ",data1[rm]['name'])
        print("***************Restaurant Menu*******************")
        option1={1:'Water (Rs 20)',2:'Tea (Rs 10)',
        3:'Breakfast combo (Rs 90)',4:'Lunch (Rs 110)',
        5:'Dinner (Rs 150)',6:'Exit'}
        for i,j in option1.items():
            print(i,". ",j)    
        op1=0
        r_bill =data1[rm]['res_bill']
        while op1 <6 and op1!=6:
            op1=int(input("Enter the choice : "))
            if op1<6:
                q = int(input("Enter the quantity : "))
                if op1 == 1:
                    r_bill += 20*q
                if op1 == 2:    
                    r_bill += 10*q
                if op1 == 3:
                    r_bill += 90*q
                if op1 == 4:    
                    r_bill += 110*q
                if op1 == 5:
                  r_bill += 150*q
            
        print("Restaurant bill of room no ",rm," is Rs ",r_bill)          
        data1[rm]['res_bill']= r_bill    
        os.remove(file)
        f=open(file,'a')
        f.write(str(data1))
        f.close()          
            
    else:
        print("Room is not booked")    
def game_bill():
    rm = input("Room no  :   ")
    file = rm + '.txt'
    if os.path.isfile(file) == True:
        f=open(file,'r')
        data =f.read()
        data1=eval(data)
        f.close()
        print("Record found. Customer name : ",data1[rm]['name'])
        print("***************Game Menu*******************")
        option1={1:'Table Tennis (Rs 60)',2:'Bowling (Rs 80)',
        3:'Snooker (Rs 70)',4:'Video games (Rs 90)',
        5:'Pool (Rs 50)',6:'Exit'}
        for i,j in option1.items():
            print(i,". ",j)    
        op1=0
        g_bill =data1[rm]['game_bill']
        while op1 <6 and op1!=6:
            op1=int(input("Enter the choice : "))
            if op1<6:
                q = int(input("No of hours : "))
                if op1 == 1:
                    g_bill += 60*q
                if op1 == 2:    
                    g_bill += 80*q
                if op1 == 3:
                    g_bill += 70*q
                if op1 == 4:    
                    g_bill += 90*q
                if op1 == 5:
                  g_bill += 50*q

        print("Gaming bill of room no ",rm," is Rs ",g_bill)          
        data1[rm]['game_bill']= g_bill    
        os.remove(file)
        f=open(file,'a')
        f.write(str(data1))
        f.close()          
            
    else:
        print("Room is not booked")    
def Total_cost():
    rm = input("Room no  :   ")
    file = rm + '.txt'
    if os.path.isfile(file) == True:
        f=open(file,'r')
        data =f.read()
        data1=eval(data)
        f.close()
        t_bill =data1[rm]['game_bill'] +data1[rm]['laund_bill']+ data1[rm]['res_bill'] + data1[rm]['rm_rent']
        gst = 0.18*t_bill
        t_bill1 =t_bill + gst
        print("********************Hotel Bill********************")
        print("CUSTOMER DETAILS")
        print("Room no : ",rm)
        print("Customer name : ",data1[rm]['name'])
        print("Customer address : ",data1[rm]['address'])
        print("Checking date : ",data1[rm]['Chk_in'])
        print("Checkout date : ",data1[rm]['chk_out'])
        print("Room rent : Rs ",data1[rm]['rm_rent'])
        print("Food bill : Rs ",data1[rm]['res_bill'])
        print("Laundry bill : Rs ",data1[rm]['laund_bill'])
        print("Gaming bill : Rs ",data1[rm]['game_bill'])
        print("Sub total bill : Rs ",t_bill)
        print("Additional Service charges(18%) : Rs ",gst)
        print("Grand total bill : Rs ",t_bill1)
    else:
        print("Room is not booked")     
   
def services(n):
    if n ==1:
        customer()             
    if n==2:
        roomrent()
    if n==3:
        restaurant_bill()
    if n==4:
        laundary_bill()
    if n==5:
        game_bill()
    if n==6:
        Total_cost()     
    if n==7:
        exit()
    if n>7:
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




