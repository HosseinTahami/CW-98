import argparse

parser = argparse.ArgumentParser()

parser.add_argument('first_number', help = 'Enter First Number')
parser.add_argument('second_number', help = 'Enter Second Number')

args = parser.parse_args()
print(type(args))
print(f'Sum: {int(args.first_number) + int(args.second_number)}')