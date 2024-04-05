import pyfiglet
from pystyle import *
import random
import os
import webbrowser
import subprocess


class Binary:
    def decimal(self, num):
        result = int(num, 2)  # Convert binary to decimal
        return result

    def hexadecimal(self, num):
        decimal_value = int(num, 2)  # Convert binary to decimal
        result = hex(decimal_value)  # Convert decimal to hexadecimal
        return result

    def octal(self, num):
        decimal_value = int(num, 2)  # Convert binary to decimal
        result = oct(decimal_value)  # Convert decimal to octal
        return result


class Decimal:
    def binary(self, num):
        result = bin(num)  # Convert decimal to binary
        return result

    def hexadecimal(self, num):
        result = hex(num)  # Convert decimal to hexadecimal
        return result
    
    def octal(self, num):
        result = oct(num)  # Convert decimal to octal
        return result

class Hexadecimal:
    def binary(self, num):
        decimal_num = int(num, 16)
        result = bin(decimal_num)[2:]  # Remove '0b' prefix from binary representation
        return f"0b{result}"

    def decimal(self, num):
        return int(num, 16)

    def octal(self, num):
        # Convert hexadecimal to decimal
        decimal_value = int(num, 16)
        # Convert decimal to octal
        result = oct(decimal_value)
        return result

class Octal:
    def binary(self, octal_string):
        # Convert octal to decimal
        decimal_value = int(octal_string, 8)
        # Convert decimal to binary
        result = bin(decimal_value)
        return result
    
    def hexadecimal(self, octal_string):
        # Convert octal to decimal
        decimal_value = int(octal_string, 8)
        # Convert decimal to hexadecimal
        result = hex(decimal_value)
        return f"0x{result}"

    def decimal(self, octal_string):
        result = int(octal_string, 8)  # Convert octal to decimal
        return result



class Bitwise:
    def Not(self, num):
        binary_str = str(num)
        complement_str = ''.join('1' if bit == '0' else '0' for bit in binary_str)
        return complement_str.zfill(len(binary_str))

    def logical_AND(self, bin1, bin2):
        result = ""
        for i in range(len(bin1)):
            result += '1' if bin1[i] == '1' and bin2[i] == '1' else '0'
        return result

    def logical_XOR(self, bin1, bin2):
        result = ""
        for i in range(len(bin1)):
            result += '1' if bin1[i] != bin2[i] else '0'
        return result

    def logical_OR(self, bin1, bin2):
        result = ""
        for i in range(len(bin1)):
            result += '1' if bin1[i] == '1' or bin2[i] == '1' else '0'
        return result

class Menu:

    def generate_ascii_art(self):
        text = "C  N  S"
        with open("pyfigletfonts.txt", "r") as file:
            fonts = file.read().splitlines()
        ascii_art = pyfiglet.Figlet(font=random.choice(fonts), width=100, justify='center')
        shape = ascii_art.renderText(text)
        return shape
    
    def helpMessage(self):
        with open("help.txt", "r") as file:
            message = file.read()
        return message
    
    def repo(self):
        pass
    
    def show(self):
        symbols = '[=]-[=]-[=]-[=]-[S]-[A]-[=]-[=]-[=]-[=]'
        os.system('cls' if os.name == 'nt' else 'clear')
        text= self.generate_ascii_art()
        Write.Print(f'{symbols}v1.0 ...\n', Colors.red_to_blue, interval=0.1)
        Write.Print(f'\n{text}\n', Colors.blue_to_purple,interval=0.01)
        Write.Print(f'\n{symbols}v1.0 ...\n', Colors.blue_to_red, interval=0.1)

    def history(self):
        with open('History.txt', 'r') as file:
            last_history = file.read().splitlines()
        with open('History.txt', 'r') as file:
            all_history = file.read()
        return last_history[len(last_history) - 1], f"\n{all_history}"
    
    def delete_all(self):
        with open('History.txt', 'w') as file:
            return file.write("")

class Execute:
    def __init__(self):
        self.menu = Menu()
        self.bitwise = Bitwise()
        self.binary = Binary()
        self.decimal = Decimal()
        self.hexa = Hexadecimal()
        self.octal = Octal()

    def check_libraries(self,*libraries):
        for lib in libraries:
            try:
                __import__(lib)
            except ImportError:
                print(f"The library '{lib}' is not installed.\n check internet connection to auto install")
                subprocess.run(f'pip install {lib}')

    def read_file(self, path):
        with open(path, 'r') as file:
            message = file.read()
        return message
    
    def save_file(self, x):
        with open('History.txt', 'a') as file:
            file.write(f"{str(x)}\n")


    def run(self):
        libraries_to_check = ['pyfiglet', 'random', 'os', 'pystyle', 'webbrowser', 'subprocess']
        self.check_libraries(*libraries_to_check)
        self.menu.show()
        print("\nWrite ? for appear help message")
        answer = None  # Initialize answer variable
        while True:
            try:
                choice = input('\033[31mCNS$ \033[0m')
                if choice == '?' or choice == 'help':
                    Write.Print(f'{self.menu.helpMessage()}\n', Colors.blue_to_cyan, interval=0.0009)
                elif 'Dev Repo' in choice:
                    self.menu.repo()
                elif choice == "Exit":
                    break
                elif 'Binary' in choice:
                    if '-I' in choice:
                        num = input('#> ')
                    elif '-F' in choice:
                        path = input('# ')
                        num = self.read_file(path=path)
                    if '-D' in choice:
                        answer = self.binary.decimal(num)
                    elif '-H' in choice:
                        answer = self.binary.hexadecimal(num)
                    elif '-O' in choice:
                        answer = self.binary.octal(num)
                elif 'Decimal' in choice:
                    if '-I' in choice:
                        num = int(input('#> '))
                    elif '-F' in choice:
                        path = input('# ')
                        num = self.read_file(path=path)
                    if '-B' in choice:
                        answer = self.decimal.binary(num)
                    elif '-H' in choice:
                        answer = self.decimal.hexadecimal(num)
                    elif '-O' in choice:
                        answer = self.decimal.octal(num)
                elif 'Hexa' in choice:
                    if '-I' in choice:
                        num = input('#> ')
                    elif '-F' in choice:
                        path = input('# ')
                        num = self.read_file(path=path)
                    if '-B' in choice:
                        answer = self.hexa.binary(num)
                    elif '-D' in choice:
                        answer = self.hexa.decimal(num)
                    elif '-O' in choice:
                        answer = self.hexa.octal(num)
                elif 'Octal' in choice:
                    if '-I' in choice:
                        num = input('#> ')
                    elif '-F' in choice:
                        path = input('# ')
                        num = self.read_file(path=path)
                    if '-B' in choice:
                        answer = self.octal.binary(num)
                    elif '-H' in choice:
                        answer = self.octal.hexadecimal(num)
                    elif '-D' in choice:
                        answer = self.octal.decimal(num)
                elif 'Not' == choice:
                    num = input('#> ')
                    answer = self.bitwise.Not(num)
                elif 'And' == choice:
                    num1 = input('#> ')
                    num2 = input('#> ')
                    answer = self.bitwise.logical_AND(num1, num2)
                elif 'Xor' == choice:
                    num1 = input('#> ')
                    num2 = input('#> ')
                    answer = self.bitwise.logical_XOR(num1, num2)
                elif 'Or' == choice:
                    num1 = input('#> ')
                    num2 = input('#> ')
                    answer = self.bitwise.logical_OR(num1, num2)
                elif choice == "L-H":
                    print(f"$ {self.menu.history()[0]}\n")
                elif choice == "A-H":
                    print(f"$ {self.menu.history()[1]}\n")
                elif choice == 'Delete':
                    self.menu.delete_all()
                elif choice == 'Repo':
                    webbrowser.open('https://github.com/KRATOS-REPOS/30-days-programming/CNS')
                else:
                    print('\033[31m[!]\033[0m Command not found \033[31m[!]\033[0m\n')

                if answer is not None:
                    self.save_file(answer)
                    print(f"$ {answer}\033[0m\n")
            except:
                print('\033[31m[!]\033[0m Command not found \033[31m[!]\033[0m\n')

if __name__ == "__main__":
    main = Execute()
    main.run()