"""
Problem 24: Lexicographic Permutations

A permutation is an ordered arrangement of objects.
For example, 3124 is one possible permutation of the
digits 1,2,3, and 4. If all of the permuatations are
listed numerically or alphabetically, we call it 
lexicographic order. The lexicographic permutations of
0,1, and 2 are:

012, 021, 102, 120, 201, 210

What is the millionth lexicographic permutation of
the digits 0,1,2,3,4,5,6,7,8, and 9?
"""
import time

def run():
	numbers = [0,1,2,3,4,5,6,7,8,9]
	#numbers = [0,1,2,3]
	print("START: {}".format(numbers))
	for _ in range(1,1000000):
		idx = len(numbers)-1
		minimum = idx
		past_numbers = [minimum]
		not_broken = True
		while idx > 0 and not_broken:
			idx-=1
			for index in range(len(past_numbers)):
				#print("INDEX: {}, VALUE: {}".format(index,numbers[past_numbers[index]]))
				if numbers[idx] < numbers[past_numbers[index]]:
					temp = numbers[idx]
					numbers[idx] = numbers[past_numbers[index]]
					numbers[past_numbers[index]] = temp
					not_broken = False
					break
			if not_broken:
				#print("NOT_HIGHER_THAN")
				insrt_idx = 0
				while insrt_idx < len(past_numbers) and numbers[idx] > numbers[past_numbers[insrt_idx]]:
					insrt_idx+=1
				past_numbers.insert(insrt_idx,idx)
				#print("PAST: {}".format(past_numbers))
		#print("PROGRESS: {}".format(numbers))
		start = idx
		while idx < len(numbers)-2:
			idx+=1
			if numbers[idx] > numbers[idx+1]:
				temp = numbers[idx]
				numbers[idx] = numbers[idx+1]
				numbers[idx+1] = temp
				idx = start
		print("INTER: {}".format(numbers))
		# Check if exhausted all options
		finished = True
		for i in range(len(numbers)-1):
			if numbers[i] > numbers[i+1]:
				finished = False
				break
		if finished:
			print("DONE_EARLY")
			break
		# EndCheck
		#time.sleep(1)
	print("FINAL: {}".format(numbers))



if __name__ == "__main__":
	run()
