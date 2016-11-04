import time
import sys

commands = ['add', 'mark', 'list', 'archive', 'x']
todo_list = []

you_saved = 'You saved the following to-do items: \n'
global outprint_menu


def menu():
    outprint_menu = input('Please specify a command [list, add, mark, archive]: ')
    if outprint_menu == 'add':
        add()
        main()
    elif outprint_menu == 'mark':
        mark()
    elif outprint_menu == 'list':
        return listing_tasks(todo_list)
    elif outprint_menu == 'archive':
        pass
    elif outprint_menu == 'x':
        return quit()
    else:
        print("I can't understant you.")
        menu()


def add():
    todo_list.append(input('Add an item: '))
    inside_add()


def inside_add():
    add_next = (input('add another one? y/n'))
    if add_next == 'y':
        add()
    elif add_next == 'n':
        main()
    else:
        print("I can't understant you.")
        inside_add()


def mark():
    pass


def listing_tasks(give_saved_list):
    print(you_saved)
    user_list_print(give_saved_list)


def user_list_print(give_list):
    for item in range(len(give_list)):
        print('[]''{}' .format(give_list[item]))


def main():
    menu()


main()
