
class task:
    def __init__(self, title, description, status):
        self.title = title
        self.description = description
        self.status = status

mytasks = []

def strike(text):
    result = ''
    for c in text:
        result = result + c + '\u0336'
    return result



def addtask():
    title = input("Enter the Task: ")
    desc = input("Enter the Description: ")

    mytasks.append(task(title,desc,"Pending"))



def displaytask():
    # enumerate to iterate two variables in the list. One for the task and other for the number of the task
    for index,todo in enumerate(mytasks):
        print(index+1,") ",todo.title,sep='')
        print("  ",todo.description,"|",todo.status)


def completetask():

    while True:
        try:
            index = int(input("Enter the task number which is complete: "))
        except ValueError:
            print("Invalid Input")
            continue
        break

    index = index - 1 # mytasks index 0 will be the task number 1. So subtracting 1 from index
    mytasks[index].status = "Complete"

    mytasks[index].description = strike(mytasks[index].description)

def deletetask():

    while True:
        try:
            index = int(input("Enter the task number to be deleted: "))
        except ValueError:
            print("Invalid Input")
            continue
        break

    index = index-1
    mytasks.pop(index)


while True:
    print("\nMenu")  
    print("1. Add Task")  
    print("2. Display All Tasks")  
    print("3. Mark Task As Completed")  
    print("4. Delete Task")  
    print("5. Exit\n")  

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
        deletetask()
        continue

    elif choice =='5':
        break

    else:
        print("Invalid Choice")
        continue
