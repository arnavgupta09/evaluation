
def add_task(l1):
    name = input("Enter name: ")
    idd = int(input("Enter id: "))
    status = input("Enter status: ")
    l1.append([name,idd,status])

def update(l1):
    flag=0
    idd = int(input("Enter task id to modify: "))
    c1 = input("Do you want to update the name?(y/n)")
    c2 = input("Do you want to update the status?(y/n)")
    for i in l1:
        if(i[1]==idd):
            if(c1=='y' or c1=='Y'):
                i[0] = input("Enter new task name: ")
            if(c2=='y' or c2=='Y'):
                i[2] = input("Enter new task status: ")
            print("Updated!")
            flag=1
    
    if(flag==0):
        print("Not found!")



def deleting(l1):
    flag=0
    nm = input("Enter name to delete: ")
    for i in l1:
        if(i[0]==nm):
            l1.remove(i)
            flag=1

    if(flag==0):
        print("Name not found!")


def listalltasks(l1):
    print("Name\t\tID")
    for i in l1:
        print(i[0],"\t\t",i[1])


def searchtasks(l1):
    m = int(input("Enter 1 for name, 2 for id: "))
    flag=0
    if(m==1):
        nm = input("Enter name: ")
        print()
        for i in l1:
            if(i[0]==nm):
                print("Id is: ",i[1],"\nStatus is: ",i[2])
                flag=1
    elif(m==2):
        idd = int(input("Enter id: "))
        print()
        for i in l1:
            if(i[1]==idd):
                print("Name is: ",i[0],"\nStatus is: ",i[2])
                flag=1
    else:
        print("Invalid choice")
        return

    if(flag==0):
        print("Not found")

def listbylastcharacter(l1):
    c = input("Enter last letter: ")
    print()
    for i in l1:
        if(i[0].endswith(c)):
            print("Name: ",i[0], "\nID: ",i[1],"\nStatus: ",i[2])
            print()


def main():
    ch = 'y'
    l1=[]
    while(ch=='y' or ch=='Y'):
        print("Enter your choice: ")
        print("1 for Add\n2 for Update\n3 for deleting\n4 for Lising all tasks\n5 for Searching\n6 for Listing by last letter\n")
        i = int(input("Enter your choice: "))
        if(i==1):
            add_task(l1)
        elif (i==2):
            update(l1)
        elif (i==3):
            deleting(l1)
        elif (i==4):
            listalltasks(l1)
        elif (i==5):
            searchtasks(l1)
        elif (i==6):
            listbylastcharacter(l1)
        else:
            print("Invalid choice")

        print()
        ch = input("Do you want to continue?(y/n)")
        if(ch=='n' or ch=='N'):
            print("Thankyou and Goodbye!")

        print()


main()



        


    
            
