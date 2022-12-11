# get common item in rucksacks - set intersection
# get priority of that item - index+1 of letter in alphabet list (lower-case + upper-case)
# put in list, then sum

import string
from collections import Counter

f=open('input_3_12')

latin_alphabet=list(string.ascii_letters)
list_priorities=[]
list_priorities_with_mult=[]
list_priorities_pt2=[]
list_lines=[line.strip() for line in f.readlines()]

for i_line,line in enumerate(list_lines):
    toys=line

    # part 1
    n_toys=len(toys)
    toys_compartment_1=toys[:int(n_toys/2)]
    toys_compartment_2=toys[int(n_toys/2):]
    common_toys=set(toys_compartment_1).intersection(set(toys_compartment_2)) # which are the common toys
    if len(common_toys)==0:
        pass
    else:
        for common_toy in common_toys:
            priority=latin_alphabet.index(common_toy)+1
            list_priorities.append(priority)
            # the part below is only if the same item on both sides had to be counted more than once for the priority count
            counter_compartment_1=Counter(toys_compartment_1) 
            counter_compartment_2=Counter(toys_compartment_2)
            mult=min(counter_compartment_1[common_toy],counter_compartment_2[common_toy])
            list_priorities_with_mult.append(mult*priority)
    
    # part 2
    if i_line%3==0:
        toys_elf_1=list_lines[i_line]
        toys_elf_2=list_lines[i_line+1]
        toys_elf_3=list_lines[i_line+2]
        common_toys_3_rucksacks=set(toys_elf_1).intersection(set(toys_elf_2),set(toys_elf_3))
        for common_toy in common_toys_3_rucksacks:
            priority_pt2=latin_alphabet.index(common_toy)+1
            list_priorities_pt2.append(priority_pt2)


sum_priorities=sum(list_priorities)
sum_priorities_with_mult=sum(list_priorities_with_mult)
sum_priorities_pt2=sum(list_priorities_pt2)
print(sum_priorities)
print(sum_priorities_with_mult)
print(sum_priorities_pt2)