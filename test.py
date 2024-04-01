import random

# TODO: Use this logic to generate tasks with division operation
rand_int1 = random.randint(5, 20)
rand_int2 = random.randint(5, 20)
minimal = min(rand_int1, rand_int2)
multiplication = rand_int1 * rand_int2

print(f'{multiplication} / {minimal} = {int(multiplication/minimal)}')

