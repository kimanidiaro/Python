

#from funkshons import get_todos, write_todos
import funkshons
import time


now = time.strftime("%b %d, %Y %H:%M:%S")
print("IT BE", now)



while True:
    user_action = input("Type add, show, edit, complete or exit")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos =funkshons.get_todos()
        todos.append(todo + '\n')


        funkshons.write_todos(todos)

    elif user_action.startswith("show"):

       todos = funkshons.get_todos("todos.txt")


       for index, item in enumerate(todos):
           item = item.strip('\n')
           row = f"{index + 1}-{item}"
           print(row)

    elif user_action.startswith("edit"):
        try:
             number =int(user_action[5:])
             print(number)

             number = number - 1

             todos = funkshons.get_todos()

             new_todo = input("Enter new todo: ")
             todos[number] = new_todo + '\n'


             funkshons.write_todos(todos)
        except ValueError:
            print("Not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos = get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            message = f"{todo_to_remove} was removed from list"
            print(message)
        except IndexError:
            print("D'oh")
            continue


    elif user_action.startswith("exit"):
        break


    else:
        print("D'oh")

        print("Bye!")