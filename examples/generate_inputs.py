from operation_costing.operations import *

N_INPUTS = 10000

# op = DiophantineOperation()
# op.generate_inputs(N_INPUTS)
# op.run_test(100, 'data_diophantine.csv')

op = SHA1HashOperation()
op.generate_inputs(N_INPUTS)
op.run_test(1, "data_sha1.csv")

op = SelectionSortOperation()
op.generate_inputs(N_INPUTS)
op.run_test(1, "data_selection_sort.csv")
