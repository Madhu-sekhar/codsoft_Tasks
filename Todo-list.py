todo_list=[]
def add(task):
    todo_list.append(task)
    print('Task added :',task)
def view():
    if not todo_list:
        print('nothing in to do list')
    else:
        for index,task in enumerate(todo_list,start=1):
            print(f'{index},{task}')
def remove(taskindex):
    taskindex=int(taskindex)
    if 1<=taskindex<=len(todo_list):
        removed_task=todo_list.pop(taskindex-1)
    else:
        print('invalid index number ')

while True:
    print('options:')
    print('add')
    print('view')
    print('remove')
    print('quit')
    user_input=input(':')
    if user_input=='quit':
        break
    elif  user_input=='add':
        task=input('enter your task:')
        add(task)
    elif user_input=='view':
        view()
    elif user_input=='remove':
        taskindex=int(input('enter your index number:'))
        remove(taskindex)
    else:
        print('invalid input')