from string import ascii_letters, digits, punctuation
from random import shuffle, choice


class PasswordGenerator:
    def __init__(self):
        self.letters = list(ascii_letters)
        self.letters_numbers = list(ascii_letters + digits)
        self.all = list(ascii_letters + digits + punctuation)
        self.passwords = []

        while True:
            try:
                self.number_of_passwords = int(input("\nNumber of passwords to generate: ") or 4)
                self.password_length = int(input("Password length: ") or 8)

                self.menu = int(input(
                    "\n[1] Upper and lowercase letters\n"
                    "[2] Letters with numbers\n"
                    "[3] Letters with numbers and symbols\n"
                    "\nChoose between [1-3]: ") or 3)
                if self.menu not in [1, 2, 3]:
                    raise ValueError
                break
            except ValueError:
                continue

    def run(self):

        for _ in range(self.number_of_passwords):
            password = []

            if self.menu == 1:
                shuffle(self.letters)
                for _ in range(self.password_length):
                    password.append(choice(self.letters))
            elif self.menu == 2:
                shuffle(self.letters_numbers)
                for _ in range(self.password_length):
                    password.append(choice(self.letters_numbers))
            else:
                shuffle(self.all)
                for _ in range(self.password_length):
                    password.append(choice(self.all))

            shuffle(password)
            self.passwords.append("".join(password))

        print(
            f"\n{'Passwords' if self.number_of_passwords > 1 else 'Password'}\n"
            f"{'-' * self.password_length if self.password_length > 9 else '-' * 9}\n")
        print('\n'.join(self.passwords))


def main():
    generator = PasswordGenerator()
    generator.run()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
