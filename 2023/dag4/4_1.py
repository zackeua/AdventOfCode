import sys
import math
def main():
	with open(sys.argv[1], 'r') as f:
		data = f.readlines()
		data = [line.split(': ')[1].strip().split(' | ') for line in data]

		total = 0
		for card in data:
			winning_numbers, numbers = card
			winning_numbers = set(map(int, winning_numbers.split()))
			numbers = set(map(int, numbers.split()))

			overlap = winning_numbers.intersection(numbers)

			score = math.floor(2 ** (len(overlap)-1)) 
			total += score
		
		print(total)

if __name__ == '__main__':
	main()
