def read_from_file(fname):
	file = open(fname,'r')
	dataset = file.read().split('\n')
	dataset = [line.split(':')[1].split(',') for line in dataset if not (line.startswith('#') or line.strip()=="")]
	file.close()
	return dataset

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
input_file = 'input.dat'

database = read_from_file(input_file)

#Database is a list of sets/frozenset
database = [frozenset(entry) for entry in database]

for d in database:
	print(d)
	
item_set = dict()

#Get initial frequency Count for every item in database
for entry in database:
	for item in entry:
		item = frozenset([item])
		if item in item_set:
			item_set[item]+=1
		else:
			item_set[item]=1

print('***Initial Frequency Count***')
for item in item_set:
	print(item,':',item_set[item])	

print('Enter Support_Threshold: ')
threshold = int(input().strip())

while(True):
	#Create a list of elements/sets whose support is greater than threshold
	frequent_items = prune(item_set,threshold)

	print('\n****Frequent_items****')
	for f in frequent_items:
		print(f)

	#Stop if you only have 1 set/item left in frequent items
	if len(frequent_items)==1:
		break		

	#Make sets using the sets/items from this list 
	new_item_set = combine_sets(frequent_items)
	#print(new_item_set)		

	#Get the count/frequency of new items/sets in the database
	item_set = get_count(new_item_set,database)
	#print(item_set)

print('***************************************************************')
print('The most frequenty associated items are:')
for item in frequent_items:
	print(item,end=' ')
print('\n')