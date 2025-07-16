while True:
    file= open('test.txt','r')
    todos = file.readlines()
    file.close()
    Action=input("Type 1.Add or 2.Show or 3.complete or 4.Edit or 5.exit: ")
    Action = Action.strip()
    match Action:
        case 'add'|"1":
            todo=input("Enter a todo: ")+"\n"
            todos.append(todo)
            file = open('test.txt','w')
            file.writelines(todos)
            file.close()

        case 'complete'|"3":
            number = int(input("Enter the number of the line to complete: "))
            file = open('test.txt', 'r')
            todos = file.readlines()
            file.close()
            todos.pop(number - 1)
            file = open('test.txt', 'w')
            file.writelines(todos)
            file.close()

        case 'show'|"2":
            file= open('test.txt','r')
            todos = file.readlines()
            file.close()
            for index,item in enumerate(todos):
                line=f"{index+1}.{item}"
                print(line)
        
        case 'edit'|"4":
            number=int(input("Enter the number of the line you want to edit: "))
            number = number-1
            ex_todo=todos[number]
            new_todo=input("Enter the new todo: ")
            todos[number]=new_todo
        case '5.exit'|"5":
            print("bye")
            break
           
            
            