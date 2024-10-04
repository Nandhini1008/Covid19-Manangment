import mysql.connector as sqlor
import csv
def ENTRY():
    l=[]
    SNo=int(input("Enter the patient's code number: "))
    l.append(SNo)
    Name=input("Enter the name of the patient: ")
    l.append(Name)
    Age=input("Enter the age of the patient: ")
    l.append(Age)
    Gender=input("Enter the gender of the patient: ")
    l.append(Gender)
    Address=input("Enter the patient's residential address: ")
    l.append(Address)
    Symptoms=input("Enter the Symptoms faced by the patient: ")
    l.append(Symptoms)
    d=tuple(l)
    try:
        mycon=sqlor.connect(host="localhost", user="root", passwd="mypass", database="cscpro")
        cursor=mycon.cursor()
        input_query="INSERT INTO coronalist(SNO,NAME,AGE,GENDER,ADDRESS,SYMPTOMS) VALUES(%s,%s,%s,%s,%s,%s)"
        cursor.execute(input_query,d)
        mycon.commit()
    except EOFError:
        format(error)
    f1=open("COVID-19.csv","w")
    c1=csv.writer(f1)
    c1.writerow(["SNo","Name","Age","Gender","Address","Symptoms"])
    c1.writerow(l)
    f1.close()
    print()
    
def DISPLAY():
    print("The patient details present is: ")
    mycon=sqlor.connect(host="localhost", user="root", passwd="mypass", database="cscpro")
    cursor=mycon.cursor()
    cursor.execute("select * from coronalist")
    s=cursor.fetchall()
    for a1 in s:
        print(a1)
    
def Change_of_values():
    f=open("COVID-19.csv","w")
    c=csv.writer(f)
    c.writerow(["SNo","Name","Age","Gender","Address","Symptoms"])
    mycon=sqlor.connect(host="localhost", user="root", passwd="mypass", database="cscpro")
    cursor=mycon.cursor()
    cursor.execute("select * from coronalist")
    s=cursor.fetchall()
    for a1 in s:
        print(a1)
        print()
    l=[]
    ch=int(input("Enter the SNo of the person to be changed: "))
    l.append(ch)
    t=["SNo","Name","Age","Gender","Address","Symptoms"]
    print("Type the Column as given below")
    print(t)
    q=input("Enter the column need to be changed")
    o=[]
    for i in s:
        m=list(i)
        for k in m:
            if ch==k:
                for j in range(len(t)):
                    b=t[j]
                    if q==b:
                        n=input("Enter the "+q+" "+"of the patient: ")
                        m[j]=n
                        l.append(n)
        o.append(m)
        
    for i1 in o:
        c.writerow(m)
    l1=l[::-1]
    d1=tuple(l1)
    try:
        mycon=sqlor.connect(host="localhost",user="root",passwd="mypass",database="cscpro")
        cursor=mycon.cursor()
        update_sql="UPDATE coronalist SET "+q+" "+"=%s WHERE SNo=%s"
        cursor.execute(update_sql,d1)
        mycon.commit()
    except EOFError:
        format(error)
    f.close()
    print()
    
def Change_of_null_values():
    f=open("COVID-19.csv","w")
    c=csv.writer(f)
    c.writerow(["SNo","Name","Age","Gender","Address","Symptoms"])
    mycon=sqlor.connect(host="localhost", user="root", passwd="mypass", database="cscpro")
    cursor=mycon.cursor()
    cursor.execute("select * from coronalist")
    s=cursor.fetchall()
    for a1 in s:
        print()
    t=["SNo","Name","Age","Gender","Address","Symptoms"]
    o1=[]
    for i in s:
        q=[]
        l=[]
        l1=[]
        m1=list(i)
        for j in range(len(m1)):
            v=m1[j]
            k=t[j]
            if v=="":
                print(m1)
                l.append(m1[0])
                print("The update is needed for")
                print(k)
                l1.append(k)
                m=input("Enter the required data: ")
                m1[j]=m
                q.append(m)
                continue
        o1.append(m1)
    for i1 in o1:
        c.writerow(i1)
        
    if len(s)>=1:
        for i in range(len(l)):
            q1=[]
            q1.append(q[i])
            d2=tuple(q1)
            try:
                mycon=sqlor.connect(host="localhost",user="root",passwd="mypass",database="cscpro")
                cursor=mycon.cursor()
                null_query="UPDATE coronalist SET "+l1[i]+" "+"=%s WHERE SNo= "+str(l[i])
                cursor.execute(null_query,d2)
                mycon.commit()
            except EOFError:
                format(error)
    else:
        print("No details of the patient is present")
    f.close()            
    print()
    
def Remove_of_values():
    f=open("COVID-19.csv","w")
    c=csv.writer(f)
    c.writerow(["SNo","Name","Age","Gender","Address","Symptoms"])
    mycon=sqlor.connect(host="localhost", user="root", passwd="mypass", database="cscpro")
    cursor=mycon.cursor()
    cursor.execute("select * from coronalist")
    s=cursor.fetchall()
    for a1 in s:
        print(a1)
        print()
    
    d11=[]
    o2=[]
    if s==[]:
        print("No details about the patient is present")
    else:
        t=["SNo","Name","Age","Gender","Address","Symptoms"]
        ch=int(input("Enter the SNo needed to be removed: "))
        for i in range(len(s)):
            m=list(s[i])
            for k in m:
                if ch==k:
                    d11.append(m[0])
                    for x in range(len(m)):
                        m[x]=""
            o2.append(m)
    for i3 in o2:
        c.writerow(i3)
        
    d3=tuple(d11)
    if d3==():
        print()
    else:
        try:
            mycon=sqlor.connect(host="localhost",user="root",passwd="mypass",database="cscpro")
            cursor=mycon.cursor()
            delete_sql="DELETE FROM coronalist WHERE SNo=%s"
            cursor.execute(delete_sql,d3)
            mycon.commit()
        except EOFError:
            format(error)
    
    f.close()
    print()
    
print()    
print("$$$$$$$$$$$$$$ PATIENT DETAILS $$$$$$$$$$$$$$$")
y=True
while y:
    print("Welcome to covid-19 managment")
    print("1.ENTER 1 to enter the details of the patient.")
    print("2.ENTER 2 to change any values of the patient.")
    print("3.ENTER 3 to enter the unentered values.")
    print("4.ENTER 4 to remove any patient details.")
    print("5.ENTER 5 to view all the details of the patients.")
    print("6.ENTER 6 to exit from the covid-19 managment.")
    ch1=int(input("Enter any values from (1 to 5): "))
    if ch1==1:
        ENTRY()
    elif ch1==2:
        Change_of_values()
    elif ch1==3:
        Change_of_null_values()
    elif ch1==4:
        Remove_of_values()
    elif ch1==5:
        DISPLAY()
    elif ch1==6:
        print("Thank you for using the COVID-19 MANAGMENT SYSYTEM")
        break  
    else:
        print("Invalid input")
        y=True
    
                
                
            
            
        
    
    
    
        


    
   


    

                        
                    
            
    
                        
                    
                     
                    
                    
                

        
    
    
    
