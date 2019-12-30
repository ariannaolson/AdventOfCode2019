import operator


class ShipComputer:
    HALT = 99

    def __init__(self, filename):
        self.opcodes = {
            1: self.add, 2: self.mul, 3: self.input, 4: self.output, 5: self.jump_if_true, 6: self.jump_if_false,
            7: self.lt, 8: self.eq
        }
        with open(filename) as f:
            self.initcode = [int(x) for x in f.read().split(",")]
        self.intcode = list(self.initcode)
        self.ip = 0

    def reset(self):
        self.intcode = list(self.initcode)
        self.ip = 0

    def set_inputs(self, noun, verb):
        self.intcode[1] = noun
        self.intcode[2] = verb

    def find_inputs_for(self, output):
        for noun in range(0, 100):
            for verb in range(0, 100):
                self.set_inputs(noun, verb)
                if self.execute() == output:
                    return 100 * noun + verb
                self.reset()
        return -1

    def get_param_address(self, param):
        param_select = 10 ** (param + 1)
        is_immediate = (self.intcode[self.ip] // param_select) % 10
        if is_immediate:
            return self.ip + param
        else:
            return self.intcode[self.ip + param]

    def execute(self):
        opcode = self.intcode[self.ip] % 100
        while self.ip < len(self.intcode) and opcode != self.HALT:
            self.opcodes[opcode]()
            opcode = self.intcode[self.ip] % 100
        return self.intcode[0]

    def add(self):
        self.binop(operator.add)

    def mul(self):
        self.binop(operator.mul)

    def input(self):
        self.intcode[self.get_param_address(1)] = int(input("Enter a value: "))
        self.ip += 2

    def output(self):
        print(self.intcode[self.get_param_address(1)])
        self.ip += 2

    def jump_if_true(self):
        if self.intcode[self.get_param_address(1)]:
            self.ip = self.intcode[self.get_param_address(2)]
        else:
            self.ip += 3

    def jump_if_false(self):
        if not self.intcode[self.get_param_address(1)]:
            self.ip = self.intcode[self.get_param_address(2)]
        else:
            self.ip += 3

    def lt(self):
        self.compare(operator.lt)

    def eq(self):
        self.compare(operator.eq)

    def compare(self, comparator):
        loperand = self.intcode[self.get_param_address(1)]
        roperand = self.intcode[self.get_param_address(2)]
        addr = self.get_param_address(3)
        if comparator(loperand, roperand):
            self.intcode[addr] = 1
        else:
            self.intcode[addr] = 0
        self.ip += 4

    def binop(self, op):
        loperand = self.intcode[self.get_param_address(1)]
        roperand = self.intcode[self.get_param_address(2)]
        addr = self.get_param_address(3)
        self.intcode[addr] = op(loperand, roperand)
        self.ip += 4

    def print_intcode(self):
        print(', '.join((str(x) for x in self.intcode)))


def main():
    comp = ShipComputer("intcode.txt")
    print("Inputs are", comp.find_inputs_for(19690720))
    # comp.print_intcode()
    comp5 = ShipComputer("test_diagnostic_code.txt")
    print("Diagnostics result:")
    comp5.execute()


if __name__ == "__main__":
    main()
