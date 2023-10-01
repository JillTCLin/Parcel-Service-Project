class Package:
    '''
    A Package class constructs a blueprint for packages. It defines what package is.
    '''

    def __init__(self, id, address, city, state, zipcode, weight, deadline, status):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.weight = weight
        self.deadline = deadline
        self.status = "at hub"
        self.delivery_time = None

    # Overwrites print(Package) otherwise it will print object reference
    def __str__(self):
        return "%s, Address: %s, %s, %s %s | Weight: %s | Deadline: %s | %s @ %s " % (self.id, self.address,
                                                                                      self.city, self.state,
                                                                                      self.zipcode, self.weight,
                                                                                      self.deadline, self.status,
                                                                                      self.delivery_time)

    # If there is delivery time, package is delivered.
    # O(1)
    def is_delivered(self):
        return self.delivery_time is not None

    # the opposite of the "is delivered()" method
    # O(1)
    def is_not_delivered(self):
        return not self.is_delivered()

    # Class method to get status of the package at the requested time. initial status is en route
    # if given time is before or equal the time the truck left the hub, the package is at hub
    # if given time is after delivered time, the package is delivered
    # Output: Updated status. Packages show delivered time if it delivered or requested time at hub or en route.
    # O(1)
    def get_status_for_time(self, requested_time, truck_start_time):
        new_status = "en route"

        if requested_time <= truck_start_time:
            new_status = "at hub"
            self.delivery_time = requested_time

        elif self.delivery_time < requested_time:
            new_status = "delivered"

        if new_status == "en route":
            self.delivery_time = requested_time

        return "ID: %s, Address: %s, %s, %s %s | Weight: %s | Deadline: %s | %s @ %s" % (self.id, self.address,
                                                                                         self.city, self.state,
                                                                                         self.zipcode, self.weight,
                                                                                         self.deadline, new_status,
                                                                                         self.delivery_time)
