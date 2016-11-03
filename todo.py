import time
import sys

commands = ['add', 'mark', 'list', 'archive', 'x']
todo_list = [0]

you_saved = 'You saved the following to-do items: \n'
outprint_menu = input('Please specify a command [list, add, mark, archive]: ')


def menu(give_outprint_menu):
        if give_outprint_menu == 'add':
            add()
        elif give_outprint_menu == 'mark':
            mark()
        elif give_outprint_menu == 'list':
            return listing_tasks(arg)
        elif give_outprint_menu == 'archive':
            pass
        elif give_outprint_menu == 'x':
            return quit()

        else:
            print("I can't understant you.")
            time.sleep(1)
            #menu()


def add():
    todo_list.append(input('Add an item: '))


def mark():



def listing_tasks(give_saved_list):
    print(you_saved)
    user_list_print(give_saved_list)


def user_list_print(give_list):
    for item in range(len(give_list)):
        print('[]''{}' .format(,arg[item]))


def main():
    outprint_menu
    add()
    listing_tasks(todo_list)

main()
