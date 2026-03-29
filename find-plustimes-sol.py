# https://codegolf.stackexchange.com/questions/287678/generate-a-large-number-using-and-%C3%97
# Input to this program is made as arguments, where the first argument indicates what program length to start from, and 

import time
find = 2**1279 - 1
def get_value(prog: list):
	s = [1]
	for i in prog.copy():
		if len(i[0]) == 1:
			aa = i[0].pop()
			i[0].add(aa)
			if i[1]:
				s.append(s[aa] * s[aa])
			else:
				s.append(s[aa] + s[aa])
		else:
			bb = i[0].pop()
			cc = i[0].pop()
			i[0].add(bb)
			i[0].add(cc)
			if i[1]:
				s.append(s[bb] * s[cc])
			else:
				s.append(s[bb] + s[cc])
		if s[-1] <= s[-2]:
			return 0 # PRUNE YOU MONKEY!!!
	return s[-1]
def generate_all_poss2(findd: int, step_count: int, require_match: bool, cutoff_point=None):
	if cutoff_point is None:
		cutoff_point = step_count
	if step_count <= 1:
		yield ([({0}, 0)], 2)
	else:
		for prog in map(lambda x: x[0], generate_all_poss2(findd, step_count - 1, False, cutoff_point)):
			a = filter(lambda x: x[1]**(2**(cutoff_point - step_count)) >= findd and x[1] + cutoff_point - step_count <= findd, (((pp:=prog + [({i,j}, k)]), (ppv:=get_value(pp))) for i in range(step_count) for j in range(step_count) for k in range(2) if not (k and 0 in (i,j)) and not ({i,j}, k) in prog))
			dup = []
			for i in a:
				if i[0] not in dup:
					dup.append(i[0])
					if not require_match or i[1] == findd:
						yield i

c = 2
s = False
start_time = time.time()
while not s:
	for i in generate_all_poss2(find, c, True):
		print(i)
		s = True
		break
	if not s:
		print("no solution for", c, "steps")
		print("Total time taken:", time.time() - start_time)
	else:
		print("solution found!")
		print("Total time taken:", time.time() - start_time)
	c += 1
