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
  
  
  
  
    
    

    


