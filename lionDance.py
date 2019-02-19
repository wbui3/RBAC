# Reading the URA.txt file
userRoleAssign = {}                         
with open ('URA.txt') as ufile:             # For the URA txt file, each name will be the key and 
    for line in ufile:                      # each role will be the value 
        x = line.split()
        user = x[0]
        role = x[1]
        userRoleAssign[user] = role 
#print (userRoleAssign)                    # this just proves the file was placed into a dictionary

# Now we read the PRA.txt file
General = {}                               # Due to the nature of python dictionaries, each  
Captain = {}                               # role in the PRA file will have its own dictionary, 
Senior = {}                                # with "action" being the key and "object" being the value
Recruit = {} 
with open ("PRA.txt") as pfile:
    for line in pfile:
        x = line.split()
        if x[0] == "General":
            action = x[1]
            obj = x[2]
            General[action] = obj
        elif x[0] == "Captain":
            action = x[1]
            obj = x[2]
            Captain[action] = obj
        elif x[0] == "Senior":
            action = x[1]
            obj = x[2]
            Senior[action] = obj
        elif x[0] == "Recruit":
            action = x[1]
            obj = x[2]
            Recruit[action] = obj
#print (General)
#print (Captain)
#print (Senior)
#print (Recruit)