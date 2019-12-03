def get_fuel_requirements(filename):
    fuel = 0
    with open(filename) as f:
        for mass in f:
            fuel += get_fuel(int(mass))
    return fuel


def get_fuel(mass):
    fuel = mass // 3 - 2
    if fuel > 0:
        return fuel + get_fuel(fuel)
    else:
        return 0


print(get_fuel_requirements('module_masses.txt'))
