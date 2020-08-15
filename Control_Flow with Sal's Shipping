# Determines the price for Ground Shipping given a package's weight.
def ground_shipping_cost(weight):
  flat_charge = 20
  cost = 20 
  if weight > 10:
    cost = cost + (4.75 * weight)
  elif weight > 6 and weight <= 10:
    cost = cost + (4.00 * weight)
  elif weight > 2 and weight <= 6:
    cost = cost + (3.00 * weight)
  else:
    cost = cost + (1.50 * weight)
  return cost

print(ground_shipping_cost(8.4))

# Premium Ground Shipping is a one-time flat charge.
premium_ground_shipping = 125

# Determines the price for Drone Shipping given a package's weight.
def drone_shipping(weight):
  cost = 0
  if weight > 10:
    cost = cost + (14.25 * weight)
  elif weight > 6 and weight <= 10:
    cost = cost + (12.00 * weight)
  elif weight > 2 and weight <= 6:
    cost = cost + (9.00 * weight)
  else:
    cost = cost + (4.50 * weight)
  return cost

print(drone_shipping(1.5))

# Determines the cheapest method of shipping and prints shipping price.
def cheapest_shipping(weight):
  ground_cost = ground_shipping_cost(weight)
  drone_cost = drone_shipping(weight)
  premium_cost = 125
  if premium_cost < drone_cost and premium_cost < ground_cost:
    print("Premium Ground Shipping is the cheapest and will cost 125.00 dollars to mail.")
  elif drone_cost < premium_cost and drone_cost < ground_cost:
    print("Drone Shipping is the cheapest and will cost " +str(drone_cost) +" dollars to mail.")
  else: 
    print("Ground Shipping is the cheapest and will cost " +str(ground_cost) +" dollars to mail.")


cheapest_shipping(4.8)

cheapest_shipping(41.5)

# Output printed to the screen:
# 53.6
# 6.75
# Ground Shipping is the cheapest and will cost 34.4 dollars to mail.
# Premium Ground Shipping is the cheapest and will cost 125.00 dollars to mail.
