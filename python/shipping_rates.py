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

ground_rate = ground(weight)

def drone(weight):
    if weight <= 2.0:
        return weight * 4.5
    elif weight > 2.0 and weight <= 6.0:
        return weight * 9.0
    elif weight > 6.0 and weight <= 10.0:
         return weight * 12.0
    else:
        return weight * 14.25

drone_rate = drone(weight)
  
def shipping_rate(weight):
    if ground_rate < drone_rate and ground_rate < premium:
        return ground_rate
    elif drone_rate < ground_rate and drone_rate < premium:
        return drone_rate
    else:
        return premium
  

print(ground(8.4))
print(drone(1.5))

print(shipping_rate(4.8))
print(shipping_rate(41.5))