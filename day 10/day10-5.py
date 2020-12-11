from pprint import pprint

# input data
input_file = 'day10.txt'
with open(input_file) as f:
    inp = f.readlines()
# process input
inp = sorted([int(n) for n in inp])

# Part 1
print('Part 1')
diffs = {1: 0, 2: 0, 3: 1}
diffs[inp[0]] += 1
for i in range(len(inp)-1):
    diffs[inp[i+1]-inp[i]] += 1
print('{} diffs of 1 jolt, {} diffs of 2 jolts, {} diffs of 3 jolts. Answ: {}'.format(
        diffs[1], diffs[2], diffs[3], diffs[1]*diffs[3])
)

inp = [0,] + inp
dp = {inp[-1]: 1}
# Use DP for faster solution
def find_next(idx):
    if dp.get(inp[idx]):
        return dp[inp[idx]]
    val = sum([find_next(idx+i) if idx+i < len(inp) and inp[idx+i] <= inp[idx] + 3 else 0 for i in [1,2,3]])
    dp[inp[idx]] = val
    return val

# Part 2
print('Part 2')
print('{} distinct arrangements.'.format(find_next(0)))
