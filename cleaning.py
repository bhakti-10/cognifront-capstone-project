import pandas as pd 
import numpy as np

def cleanDF(df):
    intlist = ['1','2','3','4','5']
    df=df.rename(columns={'approx_cost(for two people)':'cost','listed_in(type)':'type','listed_in(city)':'city'})
    print('Removing Duplicates...',end='')
    df.drop_duplicates(inplace=True)
    print('Done')
    #Removing Commas
    print('Cleaning "cost" feature...',end='')
    remove_commas=lambda x: int(x.replace(',','')) if type(x)==np.str and x!=np.nan else x
    df['cost']=df['cost'].apply(remove_commas)
    df['cost']=df['cost'].fillna(df['cost'].mean())
    print('Done')

    print('Cleaning target feature...',end='')
    remove_slashes=lambda x: round(float(x.split('/')[0])) if type(x)==np.str and x[0] in intlist and x !=np.nan else np.nan
    df['rate']=df['rate'].apply(remove_slashes)
    df['rate']=df['rate'].fillna(round(df['rate'].mean()))
    print('Done')

    print('Removing null values...',end='')
    df.dropna(how='any',inplace=True)
    print('Done')
    
    return df
