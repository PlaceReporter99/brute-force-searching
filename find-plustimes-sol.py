# https://codegolf.stackexchange.com/questions/287678/generate-a-large-number-using-and-%C3%97
# Input to this program is made as arguments, where the first argument indicates what program length to start from, and 

import math

def contains_duplicate(l):
	dup = set()
	for i in l:
		if str(i) in dup:
			return True
		else:
			dup.add(str(i))
	return False

def numtoradi(num, length):
	a = []
	for i in range(1, length+1):
		a.append(num%i)
		num = num // i
	return a

def numtobin(num, length):
	return [*map(int, bin(num)[2:].zfill(length))]

def generate_all_poss(step_count: int): # instructions in format [({variable, variable}, operator),...]. Variable is int representing variable number, operator is 0 for addition and 1 for multiplication. For example, x3 * x4 is ({3, 4}, 1).
	for a in range(math.factorial(step_count)):
		for b in range(math.factorial(step_count)):
			for c in range(2**step_count):
				yield [({i,j}, k) for i,j,k in zip(numtoradi(a, step_count), numtoradi(b, step_count), numtobin(c, step_count))]
				

leng = 1
find = 10407932194664399081925240327364085538615262247266704805319112350403608059673360298012239441732324184842421613954281007791383566248323464908139906605677320762924129509389220345773183349661583550472959420547689811211693677147548478866962501384438260291732348885311160828538416585028255604666224831890918801847068222203140521026698435488732958028878050869736186900714720710555703168729087

def get_values(length):
	a = filter(lambda x:not contains_duplicate(x) and not ({0}, 1) in x, generate_all_poss(length))
	used = set()
	for i in a:
		if str(i) not in used:
			used.add(str(i))
			s = [1]
			for j in i:
				if len(j[0]) == 1:
					aa = j[0].pop()
					j[0].add(aa)
					if j[1]:
						s.append(s[aa] * s[aa])
					else:
						s.append(s[aa] + s[aa])
				else:
					bb = j[0].pop()
					cc = j[0].pop()
					j[0].add(bb)
					j[0].add(cc)
					if j[1]:
						s.append(s[bb] * s[cc])
					else:
						s.append(s[bb] + s[cc])
			yield i, s[-1]

s = False
while not s:
	for i,j in get_values(leng):
		#print(str(i)+" "*(15*leng - len(str(i)))+str(j))
		if j == find:
			print("solution found for length",leng,"yielding",find,"which is above")
			s = True
			break
	if not s:
		print("no solution found for programs of length",leng,"that yield",find)
	leng += 1
