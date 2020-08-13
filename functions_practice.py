# Getting Ready for Physics Class
# You are a physics teacher preparing for the upcoming semester. You want to provide your students with some functions that will help them calculate some fundamental physical properties.

train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1

# converts fahrenheit to celsius
def f_to_c(f_temp):
  c_temp = ((f_temp - 32) * 5/9)
  return c_temp

f100_in_celsius = f_to_c(100)
print(f100_in_celsius)

# converts celsius to fahrenheit
def c_to_f(c_temp):
  f_temp = (c_temp * (9/5) + 32)
  return f_temp

c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)

#determines the force of an object given it's mass & acceleration
def get_force(mass, acceleration):
  return mass * acceleration

train_force = get_force(train_mass, train_acceleration)
print(train_force)

print("The GE train supplies " +str(train_force) +" Newtons of force.")

# function to determine energy by returning mass multiplied by c
# c is a constant set to the speed of light; roughly 3 * 10^8
c = 3 * 10**8
def get_energy(mass, c):
  return mass * c**2

bomb_energy = get_energy(bomb_mass, c)
print(bomb_energy)

print("A 1kg bomb supplies " +str(bomb_energy) +" Joules.")

# determines the scientifical output of work
# work is defined as force multiplied by distance
def get_work(mass, acceleration, distance):
  return get_force(mass, acceleration) * distance

train_work = get_work(train_mass, train_acceleration, train_distance)
print(train_work)

print("The GE train does " +str(train_work) +" Joules over " +str(train_distance) +" meters.")
