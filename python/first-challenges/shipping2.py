premium = 125.00

def ground(weight):
    if weight <= 2.0:
        return weight * 1.5 + 20.00
    elif weight > 2.0 and weight <= 6.0:
        return weight * 3.0 + 20.00
    elif weight > 6.0 and weight <= 10.0:
        return weight * 4.0 + 20.00
    else:
        return weight * 4.75 + 20.00

def drone(weight):
    if weight <= 2.0:
        return weight * 4.5
    elif weight > 2.0 and weight <= 6.0:
        return weight * 9.0
    elif weight > 6.0 and weight <= 10.0:
         return weight * 12.0
    else:
        return weight * 14.25

print(ground(8.4))
print(drone(1.5))

def shipping_checker(weight):
    ground_cal = ground(weight)
    drone_cal = drone(weight)
    premium_cal = premium

    if ground_cal < premium_cal and ground_cal < drone_cal:
        print("The cheapest method is Ground and the cost is " + str(ground_cal))
    elif drone_cal < premium_cal and drone_cal < ground_cal:
        print("The cheapest method is Drone and the cost is " + str(drone_cal))
    else:
        print("The cheapest method is Premium and the cost is " + str(premium_cal))

shipping_checker(4.8)
shipping_checker(41.5)
shipping_checker(1.5)