inport sys

commands = ['add', 'mark', 'list', 'archive', 'x']
todo_list = [0]


def menu(arg):
    if arg == 'add':
        pass
    elif arg == 'mark':
        pass
    elif arg == 'list':
        pass
    elif arg == 'archive':
        pass
    elif arg == 'x':
        quit()


def add():
    todo_list.append(input('Add an item: '))

def mark():
    pass


def listing_tasks(arg):
        for item in range(len(arg)):
            print('[]''{}' .format(,arg[item]))


def main():
    add()
    print(todo_list)
    listing_tasks(todo_list)

main()
