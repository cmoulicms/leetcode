# initialize the hash map

hashmap = {0:0, 2:3}

# insert the new key, value pair
hashmap[1] = 1
hashmap[1] = 2

# get the value of key
print("key: " + str(hashmap[1]))

# delete the key
del hashmap[2]

# check key exists
if 2 not in hashmap:
    print('key not found')

# iterate over the hashmap
for i in hashmap: 
    print("(" + str(i) + "," + str(hashmap[i]) + ")", end = " ")

# get keys
print(hashmap.keys())

# lenght of hashmap
print(len(hashmap))