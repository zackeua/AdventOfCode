import sys

def main():
	with open(sys.argv[1], 'r') as f:
		data = f.readlines()
		data = [line.split(': ')[1].strip().split(' | ') for line in data]
		
		total_for_each_card = {i+1:1 for i in range(len(data))}
		for i, card in enumerate(data, start=1):
			winning_numbers, numbers = card
			winning_numbers = set(map(int, winning_numbers.split()))
			numbers = set(map(int, numbers.split()))

			overlap = winning_numbers.intersection(numbers)
			if overlap != 0:
				for elem in range(i+1, i+1+len(overlap)):
					total_for_each_card[elem] += total_for_each_card[i]
		total = sum(total_for_each_card.values())
		print(total)

if __name__ == '__main__':
	main()
