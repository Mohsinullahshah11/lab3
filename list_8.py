# Week 4: => Lab 8: Real-World Applications of Lists
# a Python program that manages a list of tasks (adding, removing, displaying) with a menu-driven interface.
toDoList = []

while True:

    print('\n============== Menu ============== \n')
    print('Enter 1 to Add a Task')
    print('Enter 2 To remove a Task')
    print('Enter 3 To Display Your Tasks')
    print('Enter 0 To Exit')
    print('\n============== END ============== \n')

    option = int(input('Please select an option: '))


    if option == 1:
        task = input('Enter you task: ')
        toDoList.append(task)
        print('Task Added Successfully')
        continue
    elif option == 2:
        index = int(input('Enter The Task Number: '))
        toDoList.pop(index-1)
        print('Task Removed Successfully')
        continue
    elif option == 3:
         print('\n============== To Do Tasks ============== \n')
         if len(toDoList) != 0:
              for item in range(len(toDoList)):
                   print(f'Task {item+1}: {toDoList[item]}')
         print('\n============== END ============== \n')
    elif option == 0:
            break
    else:
         print('Invalid! Please Choose a Correct Option')
    