# Name: Tzu-Chun (Jill) Lin

import csv
import datetime
import math

from hash_table import ChainingHashTable
from package import Package
from truck import Truck

# Ref: C950 - Webinar-2 - Getting Greedy, who moved my data?
# Ref: W-2_ChainingHashTable_zyBooks_Key-Value_CSV_Greedy.py

# Create a hash table instance
p_hash = ChainingHashTable()

# uses cvs.reader and for loop to Load packages into Hash Table
# O(n)
with open('WGUPSPackage.csv') as csvfile:
    packageData = csv.reader(csvfile, delimiter=',')
    next(packageData)  # skip header
    for package in packageData:
        pID = int(package[0])
        pAddress = package[1]
        pCity = package[2]
        pState = package[3]
        pZipcode = package[4]
        pWeight = package[6]
        pDeadline = package[5]
        pStatus = package[7]  # 'at the hub',  'en route', 'delivered'

        # package object
        p = Package(pID, pAddress, pCity, pState, pZipcode, pWeight, pDeadline, pStatus)

        # insert package object into the hash table, key=pID and item = p
        p_hash.insert(pID, p)

# create an empty list and use a for loop to load address data from csv file
# O(n)
d_address_data = []
with open("WGUPSAddress.csv") as csvfile:
    address = csv.reader(csvfile, delimiter=',')

    for row in address:
        d_address_data.append(row[1])

# create an empty list and use a for loop to load distance data from csv file
# O(n)
distance_data = []  # create an empty list
with open("WGUPSDistance.csv") as cvsfile:
    distance = csv.reader(cvsfile)

    for row in distance:
        distance_data.append(row)

# look up distance from distance_data in a 2D array by package address
# input: 2 different package address
# output: distance
# O(1)
def get_distance(add1, add2):

    distance = distance_data[d_address_data.index(add1)][d_address_data.index(add2)]
    return float(distance)


# It uses while loop and nested for loop to iterate through packages in truck. -> O(n^2)
# Since the data is stored in the chaining hash table, when performing search function in the nested loop,
# the worst case of the entire program could be O(n^3).
def deliver_packages(truck):
    '''
    - Greedy algorithm: find the shortest possible route to deliver next package by selecting the best option
      available at the moment.
    - Input: truck object
    - Output: package instance
    '''
    current_address = d_address_data[0]  # Delivery starts from the HUB
    current_time = truck.time_left_hub
    total_distance = 0

    # print("truck",truck.truck_id, "left the hub @",current_time)
    while truck.has_more_package():      # O(n)
        min_distance = 9999
        min_package = None       # next package to deliver with the shortest distance from current location

        for package_id in truck.truck_packages:    # O(n)
            package = p_hash.search(package_id)    # worst case: O(n)
            package.status = "en route"

            # check if package is still on the truck
            # to get distance between current address and remaining packages' address
            if package.is_not_delivered():
                distance = get_distance(current_address, package.address)

                # if the shortest distance is found, assign distance to min_distance and next location to min_package
                if distance < min_distance:
                    min_distance = distance
                    min_package = package

        # if next package is found, update the information and remove delivered package from the truck package list.
        if min_package is not None:
            total_distance += min_distance
            travel_time = min_distance / truck.speed
            current_time += datetime.timedelta(hours = travel_time)
            min_package.delivery_time = current_time
            min_package.status = "delivered"
            current_address = min_package.address
            truck.remove_package(min_package.id)

            print(min_package)
            # print(min_package.id, " is delivered")

    back_to_hub = get_distance(current_address, d_address_data[0])  # empty truck back to HUB
    truck.get_total_distance = total_distance + back_to_hub       # get truck's route distance
#    route_distance = truck.get_total_distance
#    print(f"Truck {truck.truck_id}  distance: {route_distance}")

# load packages into truck manually
truck1 = Truck(1, datetime.timedelta(hours=8, minutes=0), [1,4,5,13,14,15,16,19,20,21,29,30,34,37,39,40])
truck2 = Truck(2, datetime.timedelta(hours=9, minutes=10), [2,3,6,7,8,10,12,17,18,25,26,31,32,33,36,38])
truck1_second_route = Truck(1, datetime.timedelta(hours=10, minutes=30),[9,11,22,23,24,27,28,35])

# Call deliver_packages function.
deliver_packages(truck1)
deliver_packages(truck2)
deliver_packages(truck1_second_route)

total_distance = truck1.get_total_distance + truck2.get_total_distance + truck1_second_route.get_total_distance

print(f'\nDelivery completed in {total_distance:.2f} miles.')

# check if package id is in the truck
# O(1)
def truck_for_package(package_id):

    if package_id in truck1.original_package_list:
        return truck1
    elif package_id in truck2.original_package_list:
        return truck2
    elif package_id in truck1_second_route.original_package_list:
        return truck1_second_route

# In order to show all packages status at a given time, utilize for loop and method in the Package class.
# O(N)
def search_by_time(given_time):
    hr, min = given_time.split(":")
    requested_time = datetime.timedelta(hours=int(hr), minutes=int(min))
    for package_id in range(1, 41):
        pkg = p_hash.search(package_id)
        print(pkg.get_status_for_time(requested_time,truck_for_package(package_id).time_left_hub))


# Ref: C950 - Webinar-4 - Python Modules
# G.  An interface for the user to view the status and info
# main - START
if __name__ == '__main__':

    print("\n--------------------------------------------")
    print("Welcome to Parcel Service tracking system!")
    print("--------------------------------------------")

    # loop until user is satisfied
    # Provide an interface for the user to view the status and info of
    # any package at any time and the total mileages traveled by all trucks.
    isExit = True
    while (isExit):
        print("\nOptions:")
        print("1. Search for an individual package information. ")
        print("2. View packages information at a particular time.")
        print("3. Exit the Program.")
        option = input("Choose an option (1, 2, or 3):")

        if option == "1":
            print("Please enter package id:")
            print(p_hash.search(int(input())))

        elif option == "2":
            print("Please enter a time after 8:00am. (For example : 11:30)")
            search_by_time(input())

        elif option == "3":
            isExit = False

        else:
            print("Wrong option, please try again!")
# main - END
