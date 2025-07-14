file= open('test.txt','r')
todos = file.readlines()
file.close()
while True:
    Action=input("Type Add or Show or Exit or Edit or complete: ")
    Action = Action.strip()
    match Action:
        case 'add'|"1":
            todo=input("Enter a todo: ")+"\n"
            file= open('test.txt','r')
            todos = file.readlines()
            file.close()
            todos.append(todo)
            file1 = open('test.txt','w')
            file1.writelines(todos)
            file1.close()
        case 'show'|"2":
            file= open('test.txt','r')
            todos = file.readlines()
            file.close()
            for index,item in enumerate(todos):
                line=f"{index+1}.{item}"
                print(line)
        case 'complete'|"3":
            number=int(input("Enter the number of the line to complete: "))
            todos.pop(number-1)
        case 'edit'|"4":
            number=int(input("Enter the number of the line you want to edit: "))
            number = number-1
            ex_todo=todos[number]
            new_todo=input("Enter the new todo: ")
            todos[number]=new_todo
        case 'exit'|"5":
            print("bye")
            break
           
            
            