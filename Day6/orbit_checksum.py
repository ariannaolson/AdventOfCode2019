class OrbitChecksum:
    def __init__(self, filename):
        self.orbits = {}
        with open(filename) as f:
            self.make_orbit_tree([orbit.strip() for orbit in f])

    def make_orbit_tree(self, orbits):
        for orbit in orbits:
            parent, child = orbit.split(')')
            if parent not in self.orbits:
                self.orbits[parent] = None
            self.orbits[child] = parent

    def count_total_orbits(self):
        total_orbits = 0
        for orbit in self.orbits.keys():
            total_orbits += self.count_orbits(orbit)
        return total_orbits

    def count_orbits(self, node):
        if not self.orbits[node]:
            return 0
        return 1 + self.count_orbits(self.orbits[node])

    def get_you_to_santa(self):
        santa = self.get_path_to_root('SAN')
        you = self.get_path_to_root('YOU')
        while santa[-1] == you[-1]:
            santa.pop()
            you.pop()
        return len(santa) + len(you)

    def get_path_to_root(self, node):
        path = []
        while self.orbits[node]:
            node = self.orbits[node]
            path.append(node)
        return path


def main():
    oc = OrbitChecksum("orbits.txt")
    print("Total orbits:", oc.count_total_orbits())
    print("Orbital transfers between you and santa:", oc.get_you_to_santa())


if __name__ == "__main__":
    main()
