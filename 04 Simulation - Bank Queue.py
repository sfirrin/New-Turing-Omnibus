# Still trying to figure this one out

import math, random

def inv_integral_dist(x, avg):
    return avg*math.log(1-x)

class bank:
    def __init__(self, avg_arrival, avg_service):
        self.avg_arrival = avg_arrival
        self.avg_service = avg_service
        self.customers_served = 0
        self.clock = 0
        self.queue = 0
        self.ttn_arrival = 0
        self.tt_end_of_service = 0
    def new_round(self):

        tt_end_of_service = self.inv_ingegral_dist(random.random(),
                                              self.avg_service)
        if (self.ttn_arrival < tt_end_of_service):
            self.tt_end_of_service -= self.ttn_arrival
            self.clock += self.ttn_arrival
            self.ttn_arrival = inv_integral_dist(random.random(),
                                        self.avg_arrival)
