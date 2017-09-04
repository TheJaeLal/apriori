from collections import Counter

database = [(1,3,4),(2,3,5),(1,2,3,5),(2,5)]
threshold = 2


database = [frozenset(x) for x in database]

#######Database ready###############



##Count occurrences

#item_set = []

#******************************************#

item_set = dict()
###########Occurences/Frequency Calculation###########3
for entry in database:
	for item in entry:
		if item in item_set:
			item_set[item]+=1
		else:
			item_set[item]=1

for item in item_set:
	print(item)
############Remove the items with support below threshold###########3
item_list = [frozenset([x]) for x in item_set]

for item in item_set:
	print(item)

for i in item_list:
	#print(i,':',item_set[i])
	if item_set[i] < threshold:
		del item_set[i]			

for i in item_set:
	print(i,':',item_set[i])


######Create new_item_set from current set######

item_list = list(item_set)

new_item_set = list()

for i in range(len(item_list)):
	for j in range(i+1,len(item_list)):
		new_set = item_list[i].union(item_list[j])		
		new_item_set.append(new_set)
		
print(new_item_set)		


