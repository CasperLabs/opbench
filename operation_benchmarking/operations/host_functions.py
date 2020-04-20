import numpy as np

from operation_benchmarking.operation import ConstantOperation, LinearOperation
from operation_benchmarking.models import constant, linear, quadratic


class AddLocalOperation(LinearOperation):
    def get_name(self):
        return "add_local"

    def get_model_variable_descriptions(self):
        return ["Input size"]

    def get_model_variable_units(self):
        return ["byte"]


class CreatePurseOperation(ConstantOperation):
    def get_name(self):
        return "create_purse"


