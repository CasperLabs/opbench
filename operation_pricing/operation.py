import time
import progressbar

class Operation:

    def __init__(self):
        self.inputs = []

    def generate_inputs(self, n_input):
        for i in range(n_input):
            self.inputs.append(self._generate_input())

    def execute(self, input_):
        raise Exception('This should be implemented')

    def _generate_input(self):
        raise Exception('This should be implemented')

    def map_input(self):
        raise Exception('This should be implemented')


    def batch_execute(self, n_executions, input_):
        for i in range(n_executions):
            self.execute(input_)


    def run_test(self, n_executions, opath):

        ofile = open(opath, 'w')

        bar = progressbar.ProgressBar(max_value=len(self.inputs))

        ofile.write('time_vars,n_exec,elapsed_time\n')

        for n, input_ in enumerate(self.inputs):
            start = time.time()
            self.batch_execute(n_executions, input_)

            end = time.time()

            time_vars = self.map_input(input_)

            elapsed_time = end-start

            ofile.write("\""+str(time_vars)
                        +"\","
                        +str(n_executions)
                        +',%.6e'%elapsed_time
                        +'\n')
            ofile.flush()
            bar.update(n)

            # print(time_vars, elapsed_time)
        ofile.close()

