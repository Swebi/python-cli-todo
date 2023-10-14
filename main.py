
class task:
    def __init__(self, title, description, status):
        self.title = title
        self.description = description
        self.status = status

mytasks = []

def strike(text):
    result = ''
    for c in text:
        result += + c + '\u0336'
    return result

def remove_strike(text):
    result = ''
    for char in text:
        if char != '\u0336':
            result += char
    return result



def addtask():

    while True:
        
        title = input("Enter the Task: ")
        desc = input("Enter the Description: ")

        if title=='' or title.isspace() or desc=='' or desc.isspace():
            print("\nEmpty Task. Please enter a valid task\n")
            continue
        else:
            mytasks.append(task(title,desc,"Pending"))
            break



def displaytask():
    # enumerate to iterate two variables in the list. One for the task and other for the number of the task
    for index,todo in enumerate(mytasks):
        print(index+1,") ",todo.title,sep='')
        print("  ",todo.description,"-",todo.status)
           
    if len(mytasks)==0:
        print("No Tasks. Add A New Task or Load From Files")
        return 0

def completetask():

    if len(mytasks)==0:
        return 0 #Using return here to stop the function if there are no existing tasks

    while True:
        try:
            index = int(input("\nEnter the task number which is complete: "))
        except ValueError:
            print("Invalid Input")
            continue
        break

    if index<=0 or index>len(mytasks):
        print("Invalid Index")
        
    else:
        index = index - 1 # mytasks index 0 will be the task number 1. So subtracting 1 from index
        mytasks[index].status = "Complete"
        mytasks[index].description = strike(mytasks[index].description)

def pendingtask():

    if len(mytasks)==0:
        return 0 #Using return here to stop the function if there are no existing tasks

    while True:
        try:
            index = int(input("\nEnter the task number which is pending: "))
        except ValueError:
            print("Invalid Input")
            continue
        break

    if index<=0 or index>len(mytasks):
        print("Invalid Index")
        
    else:
        index = index - 1 # mytasks index 0 will be the task number 1. So subtracting 1 from index
        mytasks[index].status = "Pending"
        mytasks[index].description = remove_strike(mytasks[index].description)

def deletetask():

    if len(mytasks)==0:
        return 0 #Using return here to stop the function if there are no existing tasks

    while True:
        try:
            index = int(input("\nEnter the task number to be deleted: "))
        except ValueError:
            print("Invalid Input")
            continue
        break

    if index<=0 or index>=len(mytasks):
        print("Invalid Index")
        
    else:
        index = index-1
        mytasks.pop(index)


def save():

    if len(mytasks)==0:
        print("No Tasks. Add A New Task or Load From Files")
        return 0 #Using return here to stop the function if there are no existing tasks
    
    with open("mytask.txt",'w') as myfile:
        for todo in mytasks:
            mystr = (todo.title,"|",todo.description,"|",todo.status,"|","\n") #tuple with all the values 

            #adding | to separate title, desc etc, used later during loading from file

            mystr = "".join(mystr)
            # converted the tuple into a string with format "title | description status" and now we can write this to the file
            # and separate to multiple lines using \n

            
            myfile.write(mystr)
    
    print("Saved to File")


def load():
    with open("mytask.txt",'r') as myfile:
        for line in myfile:
            line = (line.split("|")) #splitting the line which was read, by | as it is stored in the txt file
            # ['chemistry', 'assingment', 'Pending', '\n'] returned line is in this format
            linetask = line[0]
            linedesc = line[1]
            linestatus = line[2]

            #adding to tasks array
            
            mytasks.append(task(linetask,linedesc,linestatus))

    print("Loaded From File")
  

while True:
    print("\nMenu")  
    print("1. Add Task")  
    print("2. Display All Tasks")  
    print("3. Mark Task As Completed")  
    print("4. Mark Task As Pending")  
    print("5. Delete Task")
    print("6. Save")
    print("7. Load")
    print("8. Exit\n")

    choice = input("Enter the Choice: ")
    print()

    if choice == '1':
        addtask()
        continue

    elif choice == '2':
        displaytask()
        continue
    
    elif choice == '3':
        displaytask()
        completetask()
        continue

    elif choice == '4':
        displaytask()
        pendingtask()
        continue
    
    elif choice == '5':
        displaytask()
        deletetask()
        continue

    elif choice =='6':
        save()
        continue

    elif choice =='7':
        mytasks = []  #emptying the current tasks so we can replace it with the loaded tasks
        load()
        continue

    elif choice =='8':
        break

    else:
        print("Invalid Choice")
        continue
