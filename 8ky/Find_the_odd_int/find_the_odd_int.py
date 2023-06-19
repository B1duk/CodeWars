from collections import Counter
def find_it(seq):
    counter=Counter(seq)
    for num in counter:
        if counter[num]%2!=0:
            return num
        else:
            continue
