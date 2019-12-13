class PasswordCracker:

    def __init__(self, lower, upper):
        '''Sets the password at the bottom of the search space and establishes the upper bound.'''
        self.password = [int(x) for x in str(lower)]
        self.initialize_value()
        self.bound = [int(x) for x in str(upper + 1)]

    def count_password_matches(self):
        '''Counts the passwords within the bounds that meet the criteria. Use has_repeat for Part 1 matches.'''
        count = 0
        while self.is_in_bounds():
            # if self.has_repeat():
            if self.has_repeating_pair():
                print(self.password)
                count += 1
            self.increment_value(len(self.password) - 1)
        return count

    def get_value(self):
        '''Returns the integer version of the current password.'''
        return int(string(self.password))

    def is_in_bounds(self):
        '''Determines whether password is still below top bound of search space.'''
        for i, digit in enumerate(self.password):
            if digit < self.bound[i]:
                return True
            if digit > self.bound[i]:
                return False
        return False

    def initialize_value(self):
        '''Initializes password to next ascending-only value.'''
        previous = self.password[0]
        for i, digit in enumerate(self.password):
            print("Digit is", digit, "and previous is", previous)
            if digit < previous:
                self.password[i] = previous
            previous = self.password[i]

    def increment_value(self, digit):
        '''Increments value to next ascending-only value.'''
        if self.password[digit] == 9:
            self.password[digit] = self.increment_value(digit - 1)
        else:
            self.password[digit] += 1
        return self.password[digit]

    def has_repeat(self):
        '''Returns True if any adjacent digits are repeating. One of the criteria for Part 1.'''
        previous = -1
        for digit in self.password:
            if previous == digit:
                return True
            previous = digit
        return False

    def has_repeating_pair(self):
        '''Returns True if password contains an adjacent pair of repeating digits. The extra criterion for Part 2.'''
        streak = 1
        previous = -1
        for digit in self.password:
            if previous == digit:
                streak += 1
            else:
                if streak == 2:
                    return True
                streak = 1
                previous = digit
        return streak == 2


def main():
    lower_bound = 372304
    upper_bound = 847060
    pwd = PasswordCracker(lower_bound, upper_bound)
    print("Number of valid passwords:", pwd.count_password_matches())


if __name__ == "__main__":
    main()
