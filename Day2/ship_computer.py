import operator


class ShipComputer:
    opcodes = {1:operator.add, 2:operator.mul}
    HALT = 99

    def __init__(self, filename):
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

    def execute(self):
        opcode = self.intcode[self.ip]
        while self.ip < len(self.intcode) and opcode != self.HALT:
            self.operation(self.opcodes[opcode])
            self.ip += 4
            opcode = self.intcode[self.ip]
        return self.intcode[0]

    def operation(self, op):
        loperand = self.intcode[self.intcode[self.ip + 1]]
        roperand = self.intcode[self.intcode[self.ip + 2]]
        addr = self.intcode[self.ip + 3]
        self.intcode[addr] = op(loperand, roperand)

    def print_intcode(self):
        print(', '.join((str(x) for x in self.intcode)))


def main():
    comp = ShipComputer("intcode.txt")
    print("Inputs are", comp.find_inputs_for(19690720))
    # comp.print_intcode()


if __name__ == "__main__":
    main()
