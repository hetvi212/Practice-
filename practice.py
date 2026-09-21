import pandas as pd 
mydataset={"cars":["BMW","VOLVO","FORD"],
           "passing":[3,4,5]
           }
var=pd.DataFrame(mydataset)
print(var)
print(pd.__version__)