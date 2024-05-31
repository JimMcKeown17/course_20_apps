from functions import get_todos, write_todos
import time

now = time.strftime('%b %d, %Y %H:%M:%S')
print(f'The time is {now}')

while True:
    user_action = input("Type add, show, complete, or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add') or user_action.startswith('new'):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + '\n')

        write_todos(todos)

    elif user_action.startswith('show'):
        todos = get_todos('todos.txt')

        # todos = [todo.strip("\n") for todo in todos]

        for index, item in enumerate(todos):
            item = item.strip("\n")
            item = item.title()
            print(f"{index + 1}. {item}")
    elif user_action.startswith('edit'):
        try:
            todos = get_todos()

            number = int(user_action[5:])
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue


    elif user_action.startswith('complete'):
        try:
            todos = get_todos()

            number = int(user_action[9:])
            number = number - 1
            todo_to_remove = todos[number].strip('\n')
            todos.pop(number)

            print(f"Todo {todo_to_remove} was removed from the list.")

            write_todos(todos)

        except IndexError:
            print("There is no item with that umber.")
            continue

    elif user_action.startswith('exit'):
        break

print("Bye")
