class Truck:
    '''A Truck class constructs a blueprint for trucks.'''

    def __init__(self, truck_id, start_time, packageList):
        self.truck_id = truck_id
        self.truck_packages = packageList
        self.speed = 18  # average speed = 18 miles/hour
        self.time_left_hub = start_time  # change when truck is moving

        # create a copy of package list to the new memory address allocated.
        self.original_package_list = packageList.copy()

    # remove package from the list
    # O(1)
    def remove_package(self, package_id):
        self.truck_packages.remove(package_id)

    # check if there is package on truck
    # O(1)
    def has_more_package(self):
        return len(self.truck_packages) > 0

    # get total distance
    # O(1)
    def get_total_distance(self):
        return float(self.total_distance)


