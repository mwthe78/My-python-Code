train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1

def f_to_c(f_temp):
  c_temp=(f_temp-32)*5/9
  return c_temp
f100_in_celcius=f_to_c(100)

def c_to_f(c_temp):
  f_temp=c_temp*5/9+32
  return f_temp
c0_in_fahrenheit=c_to_f(0)
print(c0_in_fahrenheit)
print(f100_in_celcius)

def get_force(mass,accelaration):
  force=mass*accelaration
  return force
train_force=get_force(train_mass,train_acceleration)
print(train_force)

print("The GE train supplies "+ str(train_force)+" Newtons of force")

def get_energy(mass,c=3*10**8):
  get_energy=mass*c**2
  return get_energy
bomb_mass=1000
bomb_energy=get_energy(bomb_mass)
print("A 1kg bomb supplies ",bomb_energy," Joules")

def get_work(mass,acceleration,distance):
  force=get_force(mass,acceleration)*distance
  return force
train_work=get_work(train_mass,train_acceleration,train_distance)
print("The GE train does ",train_work," Joules of work over ",train_distance, " meters.")
  