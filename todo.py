inport sys

commands = ['add', 'mark', 'list', 'archive', 'x']
todo_list = [0]

you_saved = 'You saved the following to-do items: \n'
outprint_menu = input('Please specify a command [list, add, mark, archive]: ')


def menu(arg):
    if arg == 'add':
        add()
    elif arg == 'mark':
        mark()
    elif arg == 'list':

    elif arg == 'archive':
        pass
    elif arg == 'x':
        quit()


def add():
    todo_list.append(input('Add an item: '))

def mark():



def listing_tasks(arg):
    print(you_saved)
    user_list_print(arg)
    outprint_menu


def user_list_print(arg):
    for item in range(len(arg)):
        print('[]''{}' .format(,arg[item]))


def main():
    add()
    print(todo_list)
    listing_tasks(todo_list)

main()
