class Detangler:
    dirs = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}

    def __init__(self, filename):
        with open(filename) as f:
            # Made to accommodate n wires. Just in case.
            self.wires = [wire.strip().split(",") for wire in f]

    def get_wire_points(self, wire):
        '''Returns a set of the points a wire traverses.'''
        return {(0, 0)}.union(*[point for *point, __ in self.generate_paths(wire)])

    def get_wire_paths(self, wire):
        '''Returns a dictionary of the points a wire traverses mapped to their lowest path length.'''
        locations = {(0, 0): 0}
        for point, path in self.generate_paths(wire):
            if point not in locations:
                locations[point] = path
        return locations

    def generate_paths(self, wire):
        '''Yields next point and path length a wire goes through. Backbone logic of both problems.'''
        point = (0, 0)
        path = 0
        for turn in wire:
            direction = self.dirs[turn[0]]
            length = int(turn[1:])
            for __ in range(length):
                point = tuple([sum(axis) for axis in zip(direction, point)])
                path += 1
                yield point, path

    def find_shortest_path_intersection(self):
        '''Finds the shortest total path to an intersection by shrinking the total bounded search space.'''
        wire1 = self.get_wire_paths(self.wires[0])
        bound = float('inf')
        wire2 = self.generate_paths(self.wires[1])
        for point, path in wire2:
            if path >= bound:
                return bound
            if point in wire1:
                bound = min(bound, path + wire1[point])

    def find_closest_intersection(self):
        '''Finds the closest wire intersection by Manhattan Distance.'''
        intersections = set.intersection(*[self.get_wire_points(wire) for wire in self.wires])
        distances = {sum([abs(x) for x in point]) for point in intersections if point != (0, 0)}
        return min(distances)


def main():
    det = Detangler("wire_paths.txt")
    # Solution to Part 1
    print("Closest intersection:", det.find_closest_intersection())
    # Solution to Part 2
    print("Shortest path intersection:", det.find_shortest_path_intersection())


if __name__ == "__main__":
    main()

