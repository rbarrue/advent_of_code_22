f=open('input_1_12')
list_lines=f.readlines()
calories=0
calory_list=[]
for line in list_lines:
    if line=='\n':
        calory_list.append(calories)
        calories=0
    else:
        calories+=int(line)

# part 1
print(max(calory_list),calory_list.index(max(calory_list)))

# part 2
top_3_calories=sum(sorted(calory_list,reverse=True)[:3])
print(top_3_calories)