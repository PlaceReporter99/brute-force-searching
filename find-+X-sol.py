# https://codegolf.stackexchange.com/questions/287678/generate-a-large-number-using-and-%C3%97
# Input to this program is made as arguments, where the first argument indicates what program length to start from, and 

import sys
def generate_all_poss(instructions: list, step_count: int): # instructions in format [({variable, variable}, operator),...]. Variable is int representing variable number, operator is 0 for addition and 1 for multiplication. For example, x3 * x4 is ({3, 4}, 1).
	if len(instructions) >= step_count:
		return instructions
	elif len(instructions) == 0:
		return generate_all_poss([({0}, 1)], step_count)
	else:
		return[generate_all_poss(instructions + [({f, s}, o)], step_count)for f in range(len(instructions) + 1)for s in range(len(instructions) + 1)for o in[0,1]]

leng = int(sys.argv[1])
find = int(sys.argv[2])

def get_values(length):
	a = generate_all_poss([], length)
	try:
		while type(a[0][0]) is list:
			b = []
			for i in a:
				b += [*i]
			a = b
	except:
		pass

	values = []
	if len(a) == 1:
		a = [a]
	for i in a:
		s = [1]
		for j in i:
			if len(j[0]) == 1:
				aa = j[0].pop()
				j[0].add(aa)
				s.append(eval(f"{s[aa]} {['+', '*'][j[1]]} {s[aa]}"))
			else:
				bb = j[0].pop()
				cc = j[0].pop()
				j[0].add(bb)
				j[0].add(cc)
				s.append(eval(f"{s[bb]} {['+', '*'][j[1]]} {s[cc]}"))
		values.append(s[-1])
	return zip(a, values)


s = False
while not s:
	for i,j in get_values(leng):
		if j == find:
			print(str(i)+" "*(15*leng - len(str(i)))+str(j))
			s = True
			break
	if not s:
		print("no solution found for programs of length",leng,"that yield",find)
	leng += 1
