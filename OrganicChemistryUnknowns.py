import sqlite3 
con = sqlite3.connect('Organic_Uknowns.db')
cur = con.cursor ()

solid = input('is the compound a solid? Y or N')
if solid = "Y":
  melting_point = input ('what is the melting point? enter numeriacl value')
  boiling_point = ""

  else:
    melting_point = ""
    boiling_point = input (' what is the boiling point? enter numerical value')
    
  select statement, split lists

functional_groups = ['amine', 'amide', 'alkane', 'alkene', 
                      'alcohol', 'benzene', 'sulfur', 'aldehyde',
                      'ketone', 'ether', 'ester', 'nitro', 'nitroso',
                      'carboxylic acid', 'acyl chloride', 'phenol',
                      'azo', 'azoxy', 'nitrile', 'nitrite', 'oxime',
                      'phosphorous']
                      
unknown_groups = {}
for x in functional_groups:
  unknown_groups[x] x = input('does the compound contain {0}? Y or N'.format(x))
  
for row in cur.execute("select * from lang where melting_point >= numerical value", {"numerical value": } 
  
for row in cur.execute ("select * from lang where boiling_point >= numerical value", {"numerical value": }

for row in cur.execute ("select * from lang where functional_groups = x", {"x": 0}                                                                                    
    
```
Rows twenty-seven through thirty-one are an attempt to write the code that queries the sql database through python,
                        although they are incomplete. the equals sign & the greater than signs need edited
                        so that they retrieve compounds that are +/- the desired span of melting/boiling points.
                        Also the dictionary & the values x & zero inside the functional groups line of code are probably
                        incorrect & we need to make sure we write the correct values there.
                        Instructions on those three forLoops are located inside the website that teaches
                        querying sql data through python inside the box below the paragraph that begins by
                        saying *Instead, use the DB-API’s parameter substitution*
```  
  
  
    
    

    


