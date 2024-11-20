from collections import Counter

input_file = "input.txt"
with open(input_file) as f:
    input_data = f.read().strip()

most_common_chr = [Counter(msg).most_common() for msg in zip(*input_data.splitlines())]

print("Part 1 : " + "".join(x[0][0] for x in most_common_chr))
print("Part 2 : " + "".join(x[-1][0] for x in most_common_chr))
