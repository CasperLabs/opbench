# From https://paritytech.github.io/wasmi/parity_wasm/elements/enum.Instruction.html

from operation_benchmarking.operation import ConstantOperation

OPCODE_NAMES = [
    "Unreachable",
    "Nop",
    "Block",
    "Loop",
    "If",
    "Else",
    "End",
    "Br",
    "BrIf",
    "BrTable",
    "Return",
    "Call",
    "CallIndirect",
    "Drop",
    "Select",
    "GetLocal",
    "SetLocal",
    "TeeLocal",
    "GetGlobal",
    "SetGlobal",
    "I32Load",
    "I64Load",
    "F32Load",
    "F64Load",
    "I32Load8S",
    "I32Load8U",
    "I32Load16S",
    "I32Load16U",
    "I64Load8S",
    "I64Load8U",
    "I64Load16S",
    "I64Load16U",
    "I64Load32S",
    "I64Load32U",
    "I32Store",
    "I64Store",
    "F32Store",
    "F64Store",
    "I32Store8",
    "I32Store16",
    "I64Store8",
    "I64Store16",
    "I64Store32",
    "CurrentMemory",
    "GrowMemory",
    "I32Const",
    "I64Const",
    "F32Const",
    "F64Const",
    "I32Eqz",
    "I32Eq",
    "I32Ne",
    "I32LtS",
    "I32LtU",
    "I32GtS",
    "I32GtU",
    "I32LeS",
    "I32LeU",
    "I32GeS",
    "I32GeU",
    "I64Eqz",
    "I64Eq",
    "I64Ne",
    "I64LtS",
    "I64LtU",
    "I64GtS",
    "I64GtU",
    "I64LeS",
    "I64LeU",
    "I64GeS",
    "I64GeU",
    "F32Eq",
    "F32Ne",
    "F32Lt",
    "F32Gt",
    "F32Le",
    "F32Ge",
    "F64Eq",
    "F64Ne",
    "F64Lt",
    "F64Gt",
    "F64Le",
    "F64Ge",
    "I32Clz",
    "I32Ctz",
    "I32Popcnt",
    "I32Add",
    "I32Sub",
    "I32Mul",
    "I32DivS",
    "I32DivU",
    "I32RemS",
    "I32RemU",
    "I32And",
    "I32Or",
    "I32Xor",
    "I32Shl",
    "I32ShrS",
    "I32ShrU",
    "I32Rotl",
    "I32Rotr",
    "I64Clz",
    "I64Ctz",
    "I64Popcnt",
    "I64Add",
    "I64Sub",
    "I64Mul",
    "I64DivS",
    "I64DivU",
    "I64RemS",
    "I64RemU",
    "I64And",
    "I64Or",
    "I64Xor",
    "I64Shl",
    "I64ShrS",
    "I64ShrU",
    "I64Rotl",
    "I64Rotr",
    "F32Abs",
    "F32Neg",
    "F32Ceil",
    "F32Floor",
    "F32Trunc",
    "F32Nearest",
    "F32Sqrt",
    "F32Add",
    "F32Sub",
    "F32Mul",
    "F32Div",
    "F32Min",
    "F32Max",
    "F32Copysign",
    "F64Abs",
    "F64Neg",
    "F64Ceil",
    "F64Floor",
    "F64Trunc",
    "F64Nearest",
    "F64Sqrt",
    "F64Add",
    "F64Sub",
    "F64Mul",
    "F64Div",
    "F64Min",
    "F64Max",
    "F64Copysign",
    "I32WrapI64",
    "I32TruncSF32",
    "I32TruncUF32",
    "I32TruncSF64",
    "I32TruncUF64",
    "I64ExtendSI32",
    "I64ExtendUI32",
    "I64TruncSF32",
    "I64TruncUF32",
    "I64TruncSF64",
    "I64TruncUF64",
    "F32ConvertSI32",
    "F32ConvertUI32",
    "F32ConvertSI64",
    "F32ConvertUI64",
    "F32DemoteF64",
    "F64ConvertSI32",
    "F64ConvertUI32",
    "F64ConvertSI64",
    "F64ConvertUI64",
    "F64PromoteF32",
    "I32ReinterpretF32",
    "I64ReinterpretF64",
    "F32ReinterpretI32",
    "F64ReinterpretI64",
]

class UnreachableOperation(ConstantOperation):
    def get_name(self):
        return "Unreachable"


class NopOperation(ConstantOperation):
    def get_name(self):
        return "Nop"


class BlockOperation(ConstantOperation):
    def get_name(self):
        return "Block"


class LoopOperation(ConstantOperation):
    def get_name(self):
        return "Loop"


class IfOperation(ConstantOperation):
    def get_name(self):
        return "If"


class ElseOperation(ConstantOperation):
    def get_name(self):
        return "Else"


class EndOperation(ConstantOperation):
    def get_name(self):
        return "End"


class BrOperation(ConstantOperation):
    def get_name(self):
        return "Br"


class BrIfOperation(ConstantOperation):
    def get_name(self):
        return "BrIf"


class BrTableOperation(ConstantOperation):
    def get_name(self):
        return "BrTable"


class ReturnOperation(ConstantOperation):
    def get_name(self):
        return "Return"


class CallOperation(ConstantOperation):
    def get_name(self):
        return "Call"


class CallIndirectOperation(ConstantOperation):
    def get_name(self):
        return "CallIndirect"


class DropOperation(ConstantOperation):
    def get_name(self):
        return "Drop"


class SelectOperation(ConstantOperation):
    def get_name(self):
        return "Select"


class GetLocalOperation(ConstantOperation):
    def get_name(self):
        return "GetLocal"


class SetLocalOperation(ConstantOperation):
    def get_name(self):
        return "SetLocal"


class TeeLocalOperation(ConstantOperation):
    def get_name(self):
        return "TeeLocal"


class GetGlobalOperation(ConstantOperation):
    def get_name(self):
        return "GetGlobal"


class SetGlobalOperation(ConstantOperation):
    def get_name(self):
        return "SetGlobal"


class I32LoadOperation(ConstantOperation):
    def get_name(self):
        return "I32Load"


class I64LoadOperation(ConstantOperation):
    def get_name(self):
        return "I64Load"


class F32LoadOperation(ConstantOperation):
    def get_name(self):
        return "F32Load"


class F64LoadOperation(ConstantOperation):
    def get_name(self):
        return "F64Load"


class I32Load8SOperation(ConstantOperation):
    def get_name(self):
        return "I32Load8S"


class I32Load8UOperation(ConstantOperation):
    def get_name(self):
        return "I32Load8U"


class I32Load16SOperation(ConstantOperation):
    def get_name(self):
        return "I32Load16S"


class I32Load16UOperation(ConstantOperation):
    def get_name(self):
        return "I32Load16U"


class I64Load8SOperation(ConstantOperation):
    def get_name(self):
        return "I64Load8S"


class I64Load8UOperation(ConstantOperation):
    def get_name(self):
        return "I64Load8U"


class I64Load16SOperation(ConstantOperation):
    def get_name(self):
        return "I64Load16S"


class I64Load16UOperation(ConstantOperation):
    def get_name(self):
        return "I64Load16U"


class I64Load32SOperation(ConstantOperation):
    def get_name(self):
        return "I64Load32S"


class I64Load32UOperation(ConstantOperation):
    def get_name(self):
        return "I64Load32U"


class I32StoreOperation(ConstantOperation):
    def get_name(self):
        return "I32Store"


class I64StoreOperation(ConstantOperation):
    def get_name(self):
        return "I64Store"


class F32StoreOperation(ConstantOperation):
    def get_name(self):
        return "F32Store"


class F64StoreOperation(ConstantOperation):
    def get_name(self):
        return "F64Store"


class I32Store8Operation(ConstantOperation):
    def get_name(self):
        return "I32Store8"


class I32Store16Operation(ConstantOperation):
    def get_name(self):
        return "I32Store16"


class I64Store8Operation(ConstantOperation):
    def get_name(self):
        return "I64Store8"


class I64Store16Operation(ConstantOperation):
    def get_name(self):
        return "I64Store16"


class I64Store32Operation(ConstantOperation):
    def get_name(self):
        return "I64Store32"


class CurrentMemoryOperation(ConstantOperation):
    def get_name(self):
        return "CurrentMemory"


class GrowMemoryOperation(ConstantOperation):
    def get_name(self):
        return "GrowMemory"


class I32ConstOperation(ConstantOperation):
    def get_name(self):
        return "I32Const"


class I64ConstOperation(ConstantOperation):
    def get_name(self):
        return "I64Const"


class F32ConstOperation(ConstantOperation):
    def get_name(self):
        return "F32Const"


class F64ConstOperation(ConstantOperation):
    def get_name(self):
        return "F64Const"


class I32EqzOperation(ConstantOperation):
    def get_name(self):
        return "I32Eqz"


class I32EqOperation(ConstantOperation):
    def get_name(self):
        return "I32Eq"


class I32NeOperation(ConstantOperation):
    def get_name(self):
        return "I32Ne"


class I32LtSOperation(ConstantOperation):
    def get_name(self):
        return "I32LtS"


class I32LtUOperation(ConstantOperation):
    def get_name(self):
        return "I32LtU"


class I32GtSOperation(ConstantOperation):
    def get_name(self):
        return "I32GtS"


class I32GtUOperation(ConstantOperation):
    def get_name(self):
        return "I32GtU"


class I32LeSOperation(ConstantOperation):
    def get_name(self):
        return "I32LeS"


class I32LeUOperation(ConstantOperation):
    def get_name(self):
        return "I32LeU"


class I32GeSOperation(ConstantOperation):
    def get_name(self):
        return "I32GeS"


class I32GeUOperation(ConstantOperation):
    def get_name(self):
        return "I32GeU"


class I64EqzOperation(ConstantOperation):
    def get_name(self):
        return "I64Eqz"


class I64EqOperation(ConstantOperation):
    def get_name(self):
        return "I64Eq"


class I64NeOperation(ConstantOperation):
    def get_name(self):
        return "I64Ne"


class I64LtSOperation(ConstantOperation):
    def get_name(self):
        return "I64LtS"


class I64LtUOperation(ConstantOperation):
    def get_name(self):
        return "I64LtU"


class I64GtSOperation(ConstantOperation):
    def get_name(self):
        return "I64GtS"


class I64GtUOperation(ConstantOperation):
    def get_name(self):
        return "I64GtU"


class I64LeSOperation(ConstantOperation):
    def get_name(self):
        return "I64LeS"


class I64LeUOperation(ConstantOperation):
    def get_name(self):
        return "I64LeU"


class I64GeSOperation(ConstantOperation):
    def get_name(self):
        return "I64GeS"


class I64GeUOperation(ConstantOperation):
    def get_name(self):
        return "I64GeU"


class F32EqOperation(ConstantOperation):
    def get_name(self):
        return "F32Eq"


class F32NeOperation(ConstantOperation):
    def get_name(self):
        return "F32Ne"


class F32LtOperation(ConstantOperation):
    def get_name(self):
        return "F32Lt"


class F32GtOperation(ConstantOperation):
    def get_name(self):
        return "F32Gt"


class F32LeOperation(ConstantOperation):
    def get_name(self):
        return "F32Le"


class F32GeOperation(ConstantOperation):
    def get_name(self):
        return "F32Ge"


class F64EqOperation(ConstantOperation):
    def get_name(self):
        return "F64Eq"


class F64NeOperation(ConstantOperation):
    def get_name(self):
        return "F64Ne"


class F64LtOperation(ConstantOperation):
    def get_name(self):
        return "F64Lt"


class F64GtOperation(ConstantOperation):
    def get_name(self):
        return "F64Gt"


class F64LeOperation(ConstantOperation):
    def get_name(self):
        return "F64Le"


class F64GeOperation(ConstantOperation):
    def get_name(self):
        return "F64Ge"


class I32ClzOperation(ConstantOperation):
    def get_name(self):
        return "I32Clz"


class I32CtzOperation(ConstantOperation):
    def get_name(self):
        return "I32Ctz"


class I32PopcntOperation(ConstantOperation):
    def get_name(self):
        return "I32Popcnt"


class I32AddOperation(ConstantOperation):
    def get_name(self):
        return "I32Add"


class I32SubOperation(ConstantOperation):
    def get_name(self):
        return "I32Sub"


class I32MulOperation(ConstantOperation):
    def get_name(self):
        return "I32Mul"


class I32DivSOperation(ConstantOperation):
    def get_name(self):
        return "I32DivS"


class I32DivUOperation(ConstantOperation):
    def get_name(self):
        return "I32DivU"


class I32RemSOperation(ConstantOperation):
    def get_name(self):
        return "I32RemS"


class I32RemUOperation(ConstantOperation):
    def get_name(self):
        return "I32RemU"


class I32AndOperation(ConstantOperation):
    def get_name(self):
        return "I32And"


class I32OrOperation(ConstantOperation):
    def get_name(self):
        return "I32Or"


class I32XorOperation(ConstantOperation):
    def get_name(self):
        return "I32Xor"


class I32ShlOperation(ConstantOperation):
    def get_name(self):
        return "I32Shl"


class I32ShrSOperation(ConstantOperation):
    def get_name(self):
        return "I32ShrS"


class I32ShrUOperation(ConstantOperation):
    def get_name(self):
        return "I32ShrU"


class I32RotlOperation(ConstantOperation):
    def get_name(self):
        return "I32Rotl"


class I32RotrOperation(ConstantOperation):
    def get_name(self):
        return "I32Rotr"


class I64ClzOperation(ConstantOperation):
    def get_name(self):
        return "I64Clz"


class I64CtzOperation(ConstantOperation):
    def get_name(self):
        return "I64Ctz"


class I64PopcntOperation(ConstantOperation):
    def get_name(self):
        return "I64Popcnt"


class I64AddOperation(ConstantOperation):
    def get_name(self):
        return "I64Add"


class I64SubOperation(ConstantOperation):
    def get_name(self):
        return "I64Sub"


class I64MulOperation(ConstantOperation):
    def get_name(self):
        return "I64Mul"


class I64DivSOperation(ConstantOperation):
    def get_name(self):
        return "I64DivS"


class I64DivUOperation(ConstantOperation):
    def get_name(self):
        return "I64DivU"


class I64RemSOperation(ConstantOperation):
    def get_name(self):
        return "I64RemS"


class I64RemUOperation(ConstantOperation):
    def get_name(self):
        return "I64RemU"


class I64AndOperation(ConstantOperation):
    def get_name(self):
        return "I64And"


class I64OrOperation(ConstantOperation):
    def get_name(self):
        return "I64Or"


class I64XorOperation(ConstantOperation):
    def get_name(self):
        return "I64Xor"


class I64ShlOperation(ConstantOperation):
    def get_name(self):
        return "I64Shl"


class I64ShrSOperation(ConstantOperation):
    def get_name(self):
        return "I64ShrS"


class I64ShrUOperation(ConstantOperation):
    def get_name(self):
        return "I64ShrU"


class I64RotlOperation(ConstantOperation):
    def get_name(self):
        return "I64Rotl"


class I64RotrOperation(ConstantOperation):
    def get_name(self):
        return "I64Rotr"


class F32AbsOperation(ConstantOperation):
    def get_name(self):
        return "F32Abs"


class F32NegOperation(ConstantOperation):
    def get_name(self):
        return "F32Neg"


class F32CeilOperation(ConstantOperation):
    def get_name(self):
        return "F32Ceil"


class F32FloorOperation(ConstantOperation):
    def get_name(self):
        return "F32Floor"


class F32TruncOperation(ConstantOperation):
    def get_name(self):
        return "F32Trunc"


class F32NearestOperation(ConstantOperation):
    def get_name(self):
        return "F32Nearest"


class F32SqrtOperation(ConstantOperation):
    def get_name(self):
        return "F32Sqrt"


class F32AddOperation(ConstantOperation):
    def get_name(self):
        return "F32Add"


class F32SubOperation(ConstantOperation):
    def get_name(self):
        return "F32Sub"


class F32MulOperation(ConstantOperation):
    def get_name(self):
        return "F32Mul"


class F32DivOperation(ConstantOperation):
    def get_name(self):
        return "F32Div"


class F32MinOperation(ConstantOperation):
    def get_name(self):
        return "F32Min"


class F32MaxOperation(ConstantOperation):
    def get_name(self):
        return "F32Max"


class F32CopysignOperation(ConstantOperation):
    def get_name(self):
        return "F32Copysign"


class F64AbsOperation(ConstantOperation):
    def get_name(self):
        return "F64Abs"


class F64NegOperation(ConstantOperation):
    def get_name(self):
        return "F64Neg"


class F64CeilOperation(ConstantOperation):
    def get_name(self):
        return "F64Ceil"


class F64FloorOperation(ConstantOperation):
    def get_name(self):
        return "F64Floor"


class F64TruncOperation(ConstantOperation):
    def get_name(self):
        return "F64Trunc"


class F64NearestOperation(ConstantOperation):
    def get_name(self):
        return "F64Nearest"


class F64SqrtOperation(ConstantOperation):
    def get_name(self):
        return "F64Sqrt"


class F64AddOperation(ConstantOperation):
    def get_name(self):
        return "F64Add"


class F64SubOperation(ConstantOperation):
    def get_name(self):
        return "F64Sub"


class F64MulOperation(ConstantOperation):
    def get_name(self):
        return "F64Mul"


class F64DivOperation(ConstantOperation):
    def get_name(self):
        return "F64Div"


class F64MinOperation(ConstantOperation):
    def get_name(self):
        return "F64Min"


class F64MaxOperation(ConstantOperation):
    def get_name(self):
        return "F64Max"


class F64CopysignOperation(ConstantOperation):
    def get_name(self):
        return "F64Copysign"


class I32WrapI64Operation(ConstantOperation):
    def get_name(self):
        return "I32WrapI64"


class I32TruncSF32Operation(ConstantOperation):
    def get_name(self):
        return "I32TruncSF32"


class I32TruncUF32Operation(ConstantOperation):
    def get_name(self):
        return "I32TruncUF32"


class I32TruncSF64Operation(ConstantOperation):
    def get_name(self):
        return "I32TruncSF64"


class I32TruncUF64Operation(ConstantOperation):
    def get_name(self):
        return "I32TruncUF64"


class I64ExtendSI32Operation(ConstantOperation):
    def get_name(self):
        return "I64ExtendSI32"


class I64ExtendUI32Operation(ConstantOperation):
    def get_name(self):
        return "I64ExtendUI32"


class I64TruncSF32Operation(ConstantOperation):
    def get_name(self):
        return "I64TruncSF32"


class I64TruncUF32Operation(ConstantOperation):
    def get_name(self):
        return "I64TruncUF32"


class I64TruncSF64Operation(ConstantOperation):
    def get_name(self):
        return "I64TruncSF64"


class I64TruncUF64Operation(ConstantOperation):
    def get_name(self):
        return "I64TruncUF64"


class F32ConvertSI32Operation(ConstantOperation):
    def get_name(self):
        return "F32ConvertSI32"


class F32ConvertUI32Operation(ConstantOperation):
    def get_name(self):
        return "F32ConvertUI32"


class F32ConvertSI64Operation(ConstantOperation):
    def get_name(self):
        return "F32ConvertSI64"


class F32ConvertUI64Operation(ConstantOperation):
    def get_name(self):
        return "F32ConvertUI64"


class F32DemoteF64Operation(ConstantOperation):
    def get_name(self):
        return "F32DemoteF64"


class F64ConvertSI32Operation(ConstantOperation):
    def get_name(self):
        return "F64ConvertSI32"


class F64ConvertUI32Operation(ConstantOperation):
    def get_name(self):
        return "F64ConvertUI32"


class F64ConvertSI64Operation(ConstantOperation):
    def get_name(self):
        return "F64ConvertSI64"


class F64ConvertUI64Operation(ConstantOperation):
    def get_name(self):
        return "F64ConvertUI64"


class F64PromoteF32Operation(ConstantOperation):
    def get_name(self):
        return "F64PromoteF32"


class I32ReinterpretF32Operation(ConstantOperation):
    def get_name(self):
        return "I32ReinterpretF32"


class I64ReinterpretF64Operation(ConstantOperation):
    def get_name(self):
        return "I64ReinterpretF64"


class F32ReinterpretI32Operation(ConstantOperation):
    def get_name(self):
        return "F32ReinterpretI32"


class F64ReinterpretI64Operation(ConstantOperation):
    def get_name(self):
        return "F64ReinterpretI64"

