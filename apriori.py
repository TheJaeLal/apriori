def prune(item_set,threshold):
	#Remove items/sets whose frequency/count/support is less than threshold
	return [item for item in item_set if item_set[item] >= threshold]

def combine_sets(frequent_items):
	#Make sets using the sets/items from this list
	new_item_set = list()

	for i in range(len(frequent_items)):
		for j in range(i+1,len(frequent_items)):
			new_set = frequent_items[i].union(frequent_items[j])		
			new_item_set.append(new_set)

	return new_item_set

def get_count(new_item_set,database):	
	#Calculate the count/frequency of the new sets in the database
	item_set = dict()

	for item in new_item_set:
		for entry in database:
			if item.issubset(entry):
				if item in item_set:
					item_set[item] += 1
				else:
					item_set[item] = 1
	return item_set

#**********Main Starts here***************
database = [(1,3,4),(2,3,5),(1,2,3,5),(2,5)]

threshold = 2


#Database is a list of sets/frozenset
database = [frozenset(entry) for entry in database]

# for d in database:
# 	print(d)
#######Database ready###############


#Initial set of size 1

#******************************************#

item_set = dict()

###########Occurences/Frequency Calculation###########3
for entry in database:
	for item in entry:
		item = frozenset([item])
		if item in item_set:
			item_set[item]+=1
		else:
			item_set[item]=1

for item in item_set:
	print(item,':',item_set[item])	


#############Create a list of elements/sets whose support is greater than threshold#################
frequent_items = prune(item_set,threshold)

print('frequent_items')
for f in frequent_items:
	print(f)

######Stop if you only have 1 set/item left in frequent items##############
if len(frequent_items)==1:
	print('Game Over')
	#return

########Make sets using the sets/items from this list############# 

new_item_set = combine_sets(frequent_items)
print(new_item_set)		

#######Count their occurences##############

item_set = get_count(new_item_set,database)
print(item_set)
