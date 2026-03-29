# https://codegolf.stackexchange.com/questions/287678/generate-a-large-number-using-and-%C3%97
# Input to this program is made as arguments, where the first argument indicates what program length to start from, and 

import time
find = 2**1279 - 1

def flatten(g):
	for i in g:
		for j in i:
			yield j

def generate_all_poss3(findd: int, step_count: int, require_match: bool, cutoff_point=None):
    if cutoff_point is None:
        cutoff_point = step_count
    if step_count <= 1:
        yield [1, 2]
    else:
        for vals in generate_all_poss3(findd, step_count - 1, False, cutoff_point):
            a = filter(lambda x: x[-1]**(2**(cutoff_point - step_count)) >= findd and x[-1] + cutoff_point - step_count <= findd, flatten((vals + [v] for i in range(j, len(vals)) if (v:=(vals[i] * vals[j]) if k else (vals[i] + vals[j])) > vals[-1]) for j in range(len(vals)) for k in range(2)))
            dup = set()
            for i in a:
                if tuple(i) not in dup:
                    dup.add(tuple(i))
                    if not require_match or i[-1] == findd:
                        yield i

c = 2
s = False
start_time = time.time()
while not s:
	for i in generate_all_poss3(find, c, True):
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
