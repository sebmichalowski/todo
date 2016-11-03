import time
import sys

commands = ['add', 'mark', 'list', 'archive', 'x']
todo_list = [0]

you_saved = 'You saved the following to-do items: \n'
global outprint_menu
outprint_menu = input('Please specify a command [list, add, mark, archive]: ')

def menu(give_outprint_menu):
    if give_outprint_menu == 'add':
        add()
        return main()
    elif give_outprint_menu == 'mark':
        mark()
    elif give_outprint_menu == 'list':
        return listing_tasks(todo_list)
    elif give_outprint_menu == 'archive':
        pass
    elif give_outprint_menu == 'x':
        return quit()
    else:
        print("I can't understant you.")
        time.sleep(1)
        return main()


def add():
    todo_list.append(input('Add an item: '))
    add_next = (input('add another one? y/n'))
    if add_next == 'y':
        add()
    elif add_next == 'n':
        main()
    else:
        print("I can't understant you.")
        time.sleep(1)
    return main()

def mark():
    pass



def listing_tasks(give_saved_list):
    print(you_saved)
    user_list_print(give_saved_list)


def user_list_print(give_list):
    for item in range(len(give_list)):
        print('[]''{}' .format(give_list[item]))


def main():
    outprint_menu
    menu(outprint_menu)


main()
