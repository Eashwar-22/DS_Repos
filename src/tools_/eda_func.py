import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas_profiling.profile_report as pr

sns.set_theme(style="white", context="talk")


def GetProfile(df,title="Title",output_filename="eda_report",theme="dark"):
    x = profile_report(title=title,
                       sort="ascending",
                       style={'style':{'theme: null'
                                        'logo': ""
                                        'primary_color': "#337ab7"}})
    y = x(y)
    return y

def get_missing_features(df,
                         target=None,
                         plot_=False):
    missing_features = [f for f in df.columns if df[f].isnull().sum()>0]
    data = df.copy()
    for i in missing_features:
        print(i," : ",round(100*df[i].isnull().mean(),2),"% missing")


    if plot_:
        for i in missing_features:    
            data[i] = np.where(data[i].isnull(),1,0)
            t = data.groupby(i)[target].median().reset_index()
            sns.barplot(x=t[i], y=t[target], palette="rocket")
            plt.title(i)
            plt.show()
    return missing_features

def get_numerical_features(dataframe,
                           discrete_threshold=20,
                           temporal_key = [],
                           id_key= []):
    features = [f for f in dataframe.columns if dataframe[f].dtypes!='O']
    df = dataframe[features].copy()
    temporal_features = [f for f in df.columns if f in temporal_key]
    id_features = [f for f in df.columns if f in id_key]
    discrete_features = [f for f in df.columns if len(df[f].unique())<discrete_threshold and f not in temporal_features+id_features]
    continuous_features = [f for f in df.columns if f not in temporal_features+id_features+discrete_features]
    
    p = lambda x,y,z: print(x,len(y),"/",len(z)," features --> ",round(100*len(y)/len(z),2),"%")
    p("Numerical Features",df.columns,dataframe.columns)
    p("Temporal Features",temporal_features,df.columns)
    p("ID Features",id_features,df.columns)
    p("Discrete Features",discrete_features,df.columns)
    p("Continuous Features",continuous_features,df.columns)

    return temporal_features,id_features,discrete_features,continuous_features







