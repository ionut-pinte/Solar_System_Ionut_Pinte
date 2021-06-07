# task17
from csv import reader
import tui
import visual
import json
import matplotlib.pyplot as plt

import matplotlib.animation as animation
import numpy as np


# task1
def welcome():
    print("------------------------------Solar Record Management System------------------------------")


# task2
def menu():
    print("1) Load Data")
    print("2) Process Data")
    print("3) Visualize Data")
    print("4) Save Data")
    print("5) Exit")
    inp = input("Enter Your Selection from (1-5) :")

    if int(inp) >= 0 and int(inp) <= 5:
        return int(inp);
    else:
        print("Invalid input u need to enter between 1 to 5")
        return "None"


# task3
def started(operation):
    print(operation + " has started.")


# task4
def completed(operation):
    print(operation + " has completed.")


# task5
def error(error_msg):
    print("Error! " + error_msg + ".")


# task6
def source_data_path():
    inp = input("Please Enter a csv file path i.e (example.csv) :")
    if inp.endswith(".csv"):
        return inp
    else:
        print("Invalid file path, you need to enter a csv file")
        return "None"


# task7
def process_type():
    print("1) Retrieve entity")
    print("2) Retrieve entity details")
    print("3) Categorise entities by type")
    print("4) Categorise entities by gravity")
    print("5) Summarize entities by orbit")
    inp = input("Enter Your Selection from (1-5) :")

    if int(inp) >= 0 and int(inp) <= 5:
        return int(inp);
    else:
        print("Invalid input u need to enter between 1 to 5")
        return "None"


# task8
def entity_name():
    inp = input("Enter the name of an entity :")
    return inp;


# task9
def entity_details():
    inp = input("Enter the name of an entity :")
    lst = []
    n = int(input("Enter number of elements for list column indexes: "))
    print("Enter column indexes")
    for i in range(0, n):
        ele = int(input())
        lst.append(ele)
    lst2 = [inp, lst]
    return lst2


# task10
def list_entity(entity, cols=[]):
    if len(cols) == 0:
        print(entity)
    else:
        print("[", end='')
        for i in cols:
            print(entity[i], end=',')
        print("]")


# task11
def list_entities(entities, cols=[]):
    if len(cols) == 0:
        for i in entities:
            print(i);

    else:
        for i in entities:
            print("[", end='')
            for j in cols:
                print(i[j], end=',')
            print("]")


# task12
def list_categories(categories):
    for key in categories:
        print("key:", key, "Value:", categories[key])


# task13
def gravity_range():
    lowerInp = input("Enter lower limit for gravity :")
    upperInp = input("Enter upper limit for gravity :")
    lst = []
    while float(lowerInp) < float(upperInp):
        lst.append(float("{:.2f}".format(float(lowerInp))))
        lowerInp = float(lowerInp) + 0.1
    return lst;


# task14
def orbits():
    lst = []
    n = int(input("Enter number of entities u want to enter: "))
    for i in range(0, n):
        nm = input("Enter " + str(i + 1) + " entity name : ")
        lst.append(nm)
    return lst


def visualise():
    print("1) Entities by type")
    print("2) Entities by gravity")
    print("3) Summary of orbits")
    print("4) Animate gravities")
    inp = input("Enter Your Selection from (1-4) :")

    if int(inp) >= 0 and int(inp) <= 4:
        return int(inp);
    else:
        print("Invalid input u need to enter between 1 to 4")
        return "None"


# task16
def save():
    print("1) Export as Json")
    inp = input("Enter Your Selection from :")

    if int(inp) == 1:
        return int(inp);
    else:
        print("Invalid input")
        return "None"


# task18
records = []


# task26
def orbits(summary):
    lst1 = summary["orbited planet"]["small"]
    lst2 = summary["orbited planet"]["large"]
    plt.text("small", len(lst1))
    plt.text("large", len(lst2))

    print(summary["orbited planet"])


# task27
def gravity_animation(categories):
    fig, ax = plt.subplots()

    x = categories["low"]
    line, = ax.plot("np.sin(x)low", x)

    def init():
        line.set_ydata([np.nan] * len(x))
        return line,

    def animate(i):
        line.set_ydata(np.sin(x + i / 100))
        return line,

    ani = animation.FuncAnimation(
        fig, animate, init_func=init, interval=2, blit=True, save_count=50)


def run():
    # task19
    welcome()
    # task20
    inpMenu = menu()
    # task21
    # task29
    while inpMenu != 5:
        if inpMenu == 1:
            started("Data loading")
            path = source_data_path()
            if path != "None":
                with open(path, 'r') as read_obj:
                    csv_reader = reader(read_obj)
                    for row in csv_reader:
                        records.append(row)
                completed("Data loading")
            else:
                print("Data not loaded, Write the correct path")
        # task22
        elif inpMenu == 2:
            started("Data processing")
            inpProcess = process_type()
            if inpProcess != "None":
                if inpProcess == 1:
                    entity_name()
                elif inpProcess == 2:
                    entity_detaile()
                elif inpProcess == 3:
                    list_entities(records, [])
                elif inpProcess == 4:
                    gravity_range()
                elif inpProcess == 5:
                    orbits()
                completed("Data procesiing")
            else:
                print("Data not processed")
        # task23
        elif inpMenu == 3:
            started("Visualize Data")
            # task25
            visualise()
            completed("Visualize Data")
        # task24
        elif inpMenu == 4:
            started("Save Data")
            saveInp = save()
            # task28
            if saveInp == 1:
                with open('data.json', 'w') as jsonfile:
                    json.dump(records, jsonfile)
            completed("Save Data")

        # task30
        else:
            print("Invalid input")
        inpMenu = menu()


run()
