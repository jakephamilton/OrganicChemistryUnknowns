import sqlite3 

#Reading in database
con = sqlite3.connect('Organic_Uknowns.db')
cur = con.cursor ()

#Checking first input if compound is solid
solid = input('is the compound a solid? Y or N')
if solid == "Y":
  #Setting variables to user input
  melting_point = input ('what is the melting point? enter numerical value')
  boiling_point = ""

else:
  melting_point = ""
  boiling_point = input (' what is the boiling point? enter numerical value')
    
  select, split

#Initializing functional group list
functional_groups = ['amine', 'amide', 'alkane', 'alkene', 
                      'alcohol', 'benzene', 'sulfur', 'aldehyde',
                      'ketone', 'ether', 'ester', 'nitro', 'nitroso',
                      'carboxylic acid', 'acyl chloride', 'phenol',
                      'azo', 'azoxy', 'nitrile', 'nitrite', 'oxime',
                      'phosphorous']
                      
unknown_groups = {}
#Setting variables to user input
for x in functional_groups:
  unknown_groups[x] = input('does the compound contain {0}? Y or N'.format(x))

#Selecting melting point from group list
cur.execute:("select * from Organic_Uknowns where melting_point == input", {"input": 25})

#Selecting boiling point from group list  
cur.execute:("select * from Organic_Uknowns where boiling_point == input", {"input": 25})

#Selecting functional groups from group list
cur.execute:("select * from Organic_Uknowns where functional_groups=: x", {"x": 0})   
  
    
    

    


