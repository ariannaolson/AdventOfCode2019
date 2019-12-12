class Detangler:
    dirs = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}

    def __init__(self, filename):
        with open(filename) as f:
            self.wires = [wire.strip().split(",") for wire in f]

    def get_wire_points(self, wire):
        return {(0, 0)}.union(*[point for *point, __ in self.generate_paths(wire)])

    def get_wire_paths(self, wire):
        locations = {(0, 0): 0}
        for point, path in self.generate_paths(wire):
            if point not in locations:
                locations[point] = path
        return locations

    def generate_paths(self, wire):
        point = (0, 0)
        path = 0
        for turn in wire:
            direction = self.dirs[turn[0]]
            length = int(turn[1:])
            for __ in range(length):
                point = tuple([sum(axis) for axis in zip(direction, point)])
                path += 1
                yield point, path


    # Need to: increment one at a time and be checking for matches and narrow down the search space as you go.
    # That means I probably won't be able to recycle my old method. Unless I match the same way and then optimize for something else.
    # If I am going to do it the same way, I need to figure out how to change my set-ing.
    # Other options: set a leash and lengthen it until you get an answer (impractical, but efficient maybe?)
    # Do it from scratch

    def find_shortest_path_intersection(self):
        wire1 = self.get_wire_paths(self.wires[0])
        bound = float('inf')
        wire2 = self.generate_paths(self.wires[1])
        for point, path in wire2:
            if path >= bound:
                return bound
            if point in wire1:
                bound = min(bound, path + wire1[point])

    def find_closest_intersection(self):
        intersections = set.intersection(*[self.get_wire_points(wire) for wire in self.wires])
        distances = {sum([abs(x) for x in point]) for point in intersections if point != (0, 0)}
        return min(distances)

        # run one wire
        # run the next until steps of wire 2 == minsteps in intersections

#    def get_dimensions(self):
#        dim = [[0, 0, 0], [0, 0, 0]] # low, vertical, high, left, horizontal, right
#        for wire in self.wires:
#            for turn in wire:
#                dir = self.dirs[turn[0]]
#                axis = dim[dir[0]]
#                length = int(turn[1:])
#                axis[1] += length * dir[1]
#                axis[0] = min(axis[0], axis[1])
#                axis[2] = max(axis[1], axis[2])
#            dim[0][1] = 0
#            dim[1][1] = 0
#        return dim[0][2] - dim[0][0] + 1, dim[1][2] - dim[1][0] + 1, abs(dim[0][0]), abs(dim[1][0])
#
#    def lay_wires(self):
#        for wire in self.wires:
#            for turn in wire:
#        def lay_wire(self, wire):
#            point = (0, 0, 0)
#            locations = set([point])
#            for turn in wire:
#                direction = self.dirs[turn[0]]
#                length = int(turn[1:])
#                for __ in range(length):
#                    point = tuple([sum(axis) for axis in zip(direction, point)])
#                    locations.add(point)
#            return locations


def main():
    det = Detangler("wire_paths.txt")
    # print(det.find_closest_intersection())
    print(det.find_shortest_path_intersection())


if __name__ == "__main__":
    main()

