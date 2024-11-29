import random




def get_divisors(min,max):
  while True:
    x = random.randrange(min,max)
    y = random.randrange(min,max)
    if y !=0:
      if x % y ==0:
        return x, y ,int(x / y)

def get_var_1(min,max):
  x = random.randrange(min,max)
  y = random.randrange(min,max)
  operator = random.randrange(0,4)
  if operator == 0:
    x, y ,z = get_divisors(min,max)
    l = "/"
  elif operator == 1:
    z = x+y
    l = "+"
  elif operator == 2:
    z = x-y
    l = "-"
  elif operator == 3:
    z = x*y
    l = "x"

  print(f"{x} {l} {y} = {z}")
  return x, y ,z, l


def give_answer(z,devi):
  z1 = z
  z2 = z + random.randrange (   ( z - devi   ),   (z + devi)          )
  z3 = z - random.randrange (   ( z - devi   ),   (z + devi)          )
  answer_list = [z1,z2,z3]
  random.shuffle(answer_list)

  print(f" {answer_list[0]}")
  print(f" {answer_list[1]}")
  print(f" {answer_list[2]}")
  return answer_list





