from instructions.base.BranchLogic import branch
from instructions.base.Instruction import BranchInstruction

class IF_NULL(BranchInstruction):
    def execute(self, frame):
        ref = frame.operand_stack.pop_ref()
        if ref is None:
            branch(frame, self.offset)


class IF_NON_NULL(BranchInstruction):
    def execute(self, frame):
        ref = frame.operand_stack.pop_ref()
        if ref:
            branch(frame, self.offset)
