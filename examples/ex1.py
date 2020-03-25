from operation_pricing.operations import diophantine

N_INPUTS = 10000

a = 14251345112342512342
b = 12420358403158023482

gcd = diophantine.greatest_common_divisor(a, b)

c = 123148012345125*gcd
# print(c)

op = diophantine.DiophantineOperation()

op.generate_inputs(N_INPUTS)


print(op.run_test(1000, 'test.csv'))
