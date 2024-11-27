# Create a new dictionary 
d = dict() # or d = {} 

# Add a key - value pairs to dictionary 
d['xyz'] = 123
d['abc'] = 345
print (d) 
print (d.keys()) 
print (d.values()) 
for i in d : 
	print ("%s %d" %(i, d[i])) 
for index, key in enumerate(d): 
	print (index, key, d[key]) 
print ('xyz' in d) 
del d['xyz'] 
print ("xyz" in d)
