from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import OrdinalEncoder


import pandas as pd
import numpy as np



def handle_missing_data(df,column=[],imputation=[]):
    '''
    df : DataFrame
    column: Columns that contain missing values
    imputation: Imputation for the mentioned columns. Length should be same as that of column parameter.
                Values to be given : ['mean', 'median', 'most_frequent', 'constant','drop']
    
    '''
    data=df.copy()
    d = {i:j for i,j in zip(data.columns,range(len(data.columns)))}
    for i,j in zip(column,imputation):
        if j=='drop':
            data.dropna(subset=[i],inplace=True)
            print("Dropped rows with missing values in '{}'".format(i))
        else:
            imputer= SimpleImputer(missing_values=np.nan,strategy=j)
            data.iloc[:,d[i]:d[i]+1]=imputer.fit_transform(data.iloc[:,d[i]:d[i]+1])
            print("Replaced missing values in '{}' with '{}' value.".format(i,j))
    return data
        
def encode_categorical_data(df,col_for_one_hot_encoding=[],col_for_ordinal_encoding=[],drop=False):
    
    '''
    df : DataFrame
    col_for_one_hot_encoding: Columns that need to be encoded using One Hot Encoding
    col_for_oridnal_encoding: Columns that need to be encoded using Ordinal Encoding
    drop: Drop original columns = False (default)
    '''

    oe_style = OneHotEncoder()
    ord_enc  = OrdinalEncoder()

    data=df.copy()    
    oe_results = oe_style.fit_transform(data[col_for_one_hot_encoding])
    data = data.join(pd.DataFrame(oe_results.toarray(), columns=oe_style.categories_))
    
    
    for i in col_for_ordinal_encoding:
        data[i+'_encoded']=ord_enc.fit_transform(data[[i]])
    
    if drop==True:
        data.drop(columns=col_for_one_hot_encoding+col_for_ordinal_encoding,inplace=True)
        
    return data



        
        
                
                
                
    
    