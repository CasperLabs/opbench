import numpy as np

from operation_benchmarking.types import ConstantOperation, LinearOperation
from operation_benchmarking.models import constant, linear, quadratic

# Constant operations


class AddAssociatedKeyOperation(ConstantOperation):
    def get_name(self):
        return "add_associated_key"


class AddOperation(ConstantOperation):
    def get_name(self):
        return "add"


class CreatePurseOperation(ConstantOperation):
    def get_name(self):
        return "create_purse"


class GetArgSizeOperation(ConstantOperation):
    def get_name(self):
        return "get_arg_size"


class GetBalanceOperation(ConstantOperation):
    def get_name(self):
        return "get_balance"


class GetBlocktimeOperation(ConstantOperation):
    def get_name(self):
        return "get_blocktime"


class GetCallerOperation(ConstantOperation):
    def get_name(self):
        return "get_caller"


class GetMainPurseOperation(ConstantOperation):
    def get_name(self):
        return "get_main_purse"


class GetPhaseOperation(ConstantOperation):
    def get_name(self):
        return "get_phase"


class GetSystemContractOperation(ConstantOperation):
    def get_name(self):
        return "get_system_contract"


class IsValidUrefOperation(ConstantOperation):
    def get_name(self):
        return "is_valid_uref"


class ReadValueOperation(ConstantOperation):
    def get_name(self):
        return "read_value"


class RemoveAssociatedKeyOperation(ConstantOperation):
    def get_name(self):
        return "remove_associated_key"


class RevertOperation(ConstantOperation):
    def get_name(self):
        return "revert"


class SetActionThresholdOperation(ConstantOperation):
    def get_name(self):
        return "set_action_threshold"


class TransferFromPurseToAccountOperation(ConstantOperation):
    def get_name(self):
        return "transfer_from_purse_to_account"


class TransferFromPurseToPurseOperation(ConstantOperation):
    def get_name(self):
        return "transfer_from_purse_to_purse"


class TransferToAccountOperation(ConstantOperation):
    def get_name(self):
        return "transfer_to_account"


class UpdateAssociatedKeyOperation(ConstantOperation):
    def get_name(self):
        return "update_associated_key"


# Linear operations


class AddLocalOperation(LinearOperation):
    def get_name(self):
        return "add_local"

    def get_model_variable_descriptions(self):
        return ["Placeholder"]

    def get_model_variable_units(self):
        return ["Placeholder"]


class CallContractOperation(LinearOperation):
    def get_name(self):
        return "call_contract"

    def get_model_variable_descriptions(self):
        return ["Placeholder"]

    def get_model_variable_units(self):
        return ["Placeholder"]


class GetArgOperation(LinearOperation):
    def get_name(self):
        return "get_arg"

    def get_model_variable_descriptions(self):
        return ["Placeholder"]

    def get_model_variable_units(self):
        return ["Placeholder"]


class GetKeyOperation(LinearOperation):
    def get_name(self):
        return "get_key"

    def get_model_variable_descriptions(self):
        return ["Placeholder"]

    def get_model_variable_units(self):
        return ["Placeholder"]


class HasKeyOperation(LinearOperation):
    def get_name(self):
        return "has_key"

    def get_model_variable_descriptions(self):
        return ["Placeholder"]

    def get_model_variable_units(self):
        return ["Placeholder"]


class LoadNamedKeysOperation(LinearOperation):
    def get_name(self):
        return "load_named_keys"

    def get_model_variable_descriptions(self):
        return ["Placeholder"]

    def get_model_variable_units(self):
        return ["Placeholder"]


class NewUrefOperation(LinearOperation):
    def get_name(self):
        return "new_uref"

    def get_model_variable_descriptions(self):
        return ["Placeholder"]

    def get_model_variable_units(self):
        return ["Placeholder"]


class PrintOperation(LinearOperation):
    def get_name(self):
        return "print"

    def get_model_variable_descriptions(self):
        return ["Placeholder"]

    def get_model_variable_units(self):
        return ["Placeholder"]


class PutKeyOperation(LinearOperation):
    def get_name(self):
        return "put_key"

    def get_model_variable_descriptions(self):
        return ["Placeholder"]

    def get_model_variable_units(self):
        return ["Placeholder"]


class ReadHostBufferOperation(LinearOperation):
    def get_name(self):
        return "read_host_buffer"

    def get_model_variable_descriptions(self):
        return ["Placeholder"]

    def get_model_variable_units(self):
        return ["Placeholder"]


class ReadValueLocalOperation(LinearOperation):
    def get_name(self):
        return "read_value_local"

    def get_model_variable_descriptions(self):
        return ["Placeholder"]

    def get_model_variable_units(self):
        return ["Placeholder"]


class RemoveKeyOperation(LinearOperation):
    def get_name(self):
        return "remove_key"

    def get_model_variable_descriptions(self):
        return ["Placeholder"]

    def get_model_variable_units(self):
        return ["Placeholder"]


class RetOperation(LinearOperation):
    def get_name(self):
        return "ret"

    def get_model_variable_descriptions(self):
        return ["Placeholder"]

    def get_model_variable_units(self):
        return ["Placeholder"]


class WriteOperation(LinearOperation):
    def get_name(self):
        return "write"

    def get_model_variable_descriptions(self):
        return ["Placeholder"]

    def get_model_variable_units(self):
        return ["Placeholder"]
