#!/usr/local/bin/python
# -*- coding: utf-8 -*-

class Car:
    def __init__(self, brand, model, km, service_date):
        self.brand = brand
        self.model = model
        self.km = km
        self.service_date = service_date

def see_vehicles(list):
    for x in list:
        print list.index(x)+1
        print x.brand
        print x.model
        print x.km
        print x.service_date
        print "\n"

    if not list:
        print "You don't have any vehicles in your contact list."

def add_new_vehicle(list):
    brand = raw_input("Please enter vehicle's brand: ")
    model = raw_input("Please enter vehicle's model: ")
    km = raw_input("Please enter vehicle's kilometers done so far: ")
    service_date = raw_input("Please enter vehicle's service date: ")

    new_vehicle = Car(brand = brand, model = model, km = km, service_date = service_date)
    list.append(new_vehicle)

    print "Success! New vehicle has been added."

def edit_vehicle(list):

    see_vehicles(list)

    index = int(raw_input("Please, indicate the number of the vehicle that you wish to edit: ")) - 1

    while True:
        element_to_edit = raw_input("What element you would like to edit: brand, model, kilometers, service date? To stop editing enter quit.  ").lower()
        print element_to_edit

        if element_to_edit == "brand":
            list[index].brand = raw_input("Enter new brand: ")
        elif element_to_edit == "model":
            list[index].model = raw_input("Enter new model: ")
        elif element_to_edit == "kilometers":
            list[index].km = raw_input("Enter new number of kilometers: ")
        elif element_to_edit == "service date":
            list[index].service_date = raw_input("Enter new service date: ")
        elif element_to_edit == "quit":
            break
        else:
            print "The answer is not valid"
            answer = raw_input("Would you like to keep editing? yes/no ").lower()
            if answer == "no":
                break

def update_vehicles_txt(file_name, list):

    txt_file = open(file_name, "w")

    for element in list:
        txt_file.write(element.brand + " ")
        txt_file.write(element.model + " ")
        txt_file.write(element.km + " ")
        txt_file.write(element.service_date)
        txt_file.write("\n")

    txt_file.close()

def main():

    vehicles_list = []

    tesla = Car(brand="tesla", model="x", km="50000", service_date="12/12/18")
    vehicles_list.append(tesla)

    smart = Car(brand="smart", model="sm", km="1300", service_date="13/12/18")
    vehicles_list.append(smart)

    update_vehicles_txt("vehicles.txt", vehicles_list)


    while True:

        print "What would you like to do?"
        print "a) See the list of the vehicles"
        print "b) Edit vehicle"
        print "c) Add new vehicle"

        action = raw_input("Please, select a, b or c: ").lower()


        if action == "a":
            see_vehicles(vehicles_list)
        elif action == "b":
            edit_vehicle(vehicles_list)
            update_vehicles_txt("vehicles.txt", vehicles_list)
        elif action == "c":
            add_new_vehicle(vehicles_list)
            update_vehicles_txt("vehicles.txt", vehicles_list)
        else:
            print "The input is not valid. Please, select a, b or c: "


if __name__ == "__main__":
        main()


