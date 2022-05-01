import sqlite3 
con = sqlite3.connect('Organic_Uknowns.db')
cur = con.cursor ()

solid = input('is the compound a solid? Y or N')
if solid == "Y":
  melting_point = input ('what is the melting point? enter numerical value')
  boiling_point = ""

else:
  melting_point = ""
  boiling_point = input (' what is the boiling point? enter numerical value')
    
  select, split

functional_groups = ['amine', 'amide', 'alkane', 'alkene', 
                      'alcohol', 'benzene', 'sulfur', 'aldehyde',
                      'ketone', 'ether', 'ester', 'nitro', 'nitroso',
                      'carboxylic acid', 'acyl chloride', 'phenol',
                      'azo', 'azoxy', 'nitrile', 'nitrite', 'oxime',
                      'phosphorous']
                      
unknown_groups = {}
for x in functional_groups:
  unknown_groups[x] = input('does the compound contain {0}? Y or N'.format(x))

  
for row in cur.execute:("select * from lang where melting_point=: input", {"input": +-25}) 
  
for row in cur.execute:("select * from lang where boiling_point=: input", {"input": +-25})

for row in cur.execute:("select * from lang where functional_groups=: x", {"x": 0})                                                                                  
    



    
```
Traceback (most recent call last):
  File "C:\Users\Jake Hamilton\Documents\OrganicChemistryUnknowns\OrganicChemistryUnknowns.py", line 28, in <module>
    for row in cur.execute:("select * from lang where melting_point=: input", {"input": +-25})
TypeError: 'builtin_function_or_method' object is not iterable


I edited some things inside this code that enabled it to run, but the error listed above comes up when you attempt to 
use the search engine. It refers to the fact that the corresponding values to the keys within the dictionaries arent
iterable. If the dictionaries were set up correctly, the program would likely be able to run properly
```  
  
    
    

    


