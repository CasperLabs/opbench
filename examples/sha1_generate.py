from operation_pricing.operations import sha1

N_INPUTS = 10000


op = sha1.SHA1HashOperation()

op.generate_inputs(N_INPUTS)


op.run_test(1, 'data_sha1.csv')
