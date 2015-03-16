from sys import argv
from time import time, sleep

from datetime import datetime

empty_file = True
ts = time()
parameters = argv
current_order = {"Ivan": 11, "Petkan": 23}
another = {"dsdasf": 11, "Petkaasfasfn": 23}
order = {}
loaded_list_of_orders = {}

list_of_orders = {}
content = []
list_of_all_orders = []
#current_order = {}


def take():

    the_name = " ".join(content[1:len(content) - 1])
    if the_name in current_order:
        current_order[the_name] += int(content[-1])
        print("Taking order from {} for {}".format(the_name, content[-1]))
    else:
        current_order[the_name] = int(content[-1])
        print("Taking order from {} for {}".format(the_name, content[-1]))


def menu():
    while True:
        enter_command()
        if content[0] == "take":
            take()
        elif content[0] == "status":
            status()
        elif content[0] == "save":
            save()
        elif content[0] == "list":
            print (" ".join(current_order))
        elif content[0] == "load ":
            print(" a ")  # list_of_orders[int[content[1]]]
        elif content[0] == "finish":
            finish()
        else:
            print(
                "Wrong command pleace enter some of these : \n take <name> <price>\nstatus\nsave\nlist\nload <number of list>\nfinish")


def enter_command():
    inputCommand = input("Enter comand :")
    content = list(inputCommand.split(" "))


def status():
    for key in current_order:
        print("{} - {}".format(key, current_order[key]))


def save():

    stamp = "orders_" + \
        datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')
    context = ""
    for item in list(current_order):
        #context += (item + " - " + current_order(item))
        print(context)
    this_content = "\n\n{}\n{}".format(stamp, context)
    file = open("PizzaOrderList.txt", 'a+')
    file.write(this_content)


def main():
    save()


def show_list():
    print("\n".join(list_of_all_orders))


def load():
    load_number = content[1]
    for row in list(list_of_orders[(list_of_all_orders[load_number-1])].split("\n")):
        current_row = row.split("-")
        current_order[current_row[0]] = current_row[1]


def load_orders():
    file = open("PizzaOrderList.txt", 'r+')

    readed_text = file.read()
    if len(list(readed_text.split())) < 1:
        empty_file = True
        print("We dont have any orders yet")
    else:
        empty_file = False
        loaded_list_of_orders = list(readed_text.split("\n\n"))
        single_order = []
        for item in loaded_list_of_orders:
            single_order = item.split("\n")
            content = "\n".join(single_order[1:])
            list_of_orders[single_order[0]] = content
            list_of_all_orders.append(single_order[0])





        #print(list_of_orders[single_order[0]])
        #print (list_of_orders)

if __name__ == '__main__':
    load_orders()
    show_list()
    save()
