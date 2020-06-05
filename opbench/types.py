from opbench.operation import Operation
from opbench.models import constant, linear, quadratic, linear_two_arg


class LinearOperation(Operation):
    def runtime_model(self, param, x):
        a, b = param
        x_ = x[0]

        return a * x_ + b

    def get_n_model_param(self):
        return 2

    def get_model_input_size(self):
        return 1

    def get_constant_term_idx(self):
        return 1

    def get_runtime_model(self):
        return linear

    def get_model_definition(self):
        return "f(x) = a * x + b"

    def get_model_parameter_labels(self):
        return ["a", "b"]


class QuadraticOperation(Operation):
    def runtime_model(self, param, x):
        a, b, c = param
        x_ = x[0]

        return a * x_ ** 2 + b * x_ + c

    def get_n_model_param(self):
        return 3

    def get_model_input_size(self):
        return 1

    def get_constant_term_idx(self):
        return 2

    def get_runtime_model(self):
        return quadratic

    def get_model_definition(self):
        return "f(x) = a * x^2 + b * x + c"

    def get_model_parameter_labels(self):
        return ["a", "b", "c"]


class ConstantOperation(Operation):
    def runtime_model(self, param, x):
        return x[0]

    def get_n_model_param(self):
        return 1

    def get_model_input_size(self):
        return 0

    def get_constant_term_idx(self):
        return 0

    def get_runtime_model(self):
        return constant

    def get_model_definition(self):
        return "f(x) = c"

    def get_model_parameter_labels(self):
        return ["c"]

    def get_model_variable_descriptions(self):
        return []

    def get_model_variable_units(self):
        return []


class LinearTwoArgOperation(Operation):
    def runtime_model(self, param, X):
        a, b, c = param
        x, y = X
        return a * x + b * y + c

    def get_n_model_param(self):
        return 3

    def get_model_input_size(self):
        return 2

    def get_constant_term_idx(self):
        return 2

    def get_runtime_model(self):
        return linear_two_arg

    def get_model_definition(self):
        return "f(x, y) = a * x + b * y + c"

    def get_model_parameter_labels(self):
        return ["a", "b", "c"]


TYPES = {
    "constant": ConstantOperation,
    "linear": LinearOperation,
    "linear_two_arg": LinearTwoArgOperation,
    "quadratic": QuadraticOperation,
}
