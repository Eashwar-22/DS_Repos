# EDA Class

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pandas_profiling import ProfileReport

sns.set_theme(style="white", context="talk")

'''
Typical EDA Workflow

1. missing values
2. all numerical variables
3. distribution of numerical variables
4. categorical variables
5. cardinality of categorical variables
6. outliers
7. relationship beteween independent & dependent feature(target)



'''








class EDA_Summary:
        
        def __init__(self, 
                     df,
                     target=None,
                     discrete_threshold=20,
                     temporal_features = [],
                     id_features= []
                    ):
            
            self.target=target
            self.df = df.copy()
            self.discrete_threshold = discrete_threshold
            self.temporal_features = temporal_features
            self.id_features = id_features
            self.get_numerical_features(print_col=False)
        
        def plot_(self,df,kind="scatter",x=None,y=None,hue=None,title=None,figsize=(4,4),bins=10,multiple='layer'):
            '''
            kind = scatter|bar|count|joint
            multiple = layer|stack  (only for histplot)
            bins =  (only for histplot)
            
            '''
            f, ax = plt.subplots(figsize=figsize)
            if kind=="scatter": #bivariate
                sns.scatterplot(x=x,y=y,hue=hue,data=df,ax=ax)
            elif kind=="bar": #bivariate
                sns.barplot(x=x,y=y,data=df,hue=hue,ax=ax)
            elif kind=="count": #univariate
                sns.countplot(x=x,y=y,data=df,hue=hue,ax=ax)
            elif kind=="joint": #bivariate
                sns.jointplot(x=x,y=y,data=df,hue=hue,ax=ax)
            elif kind=='line':
                sns.lineplot(x=x,y=y,data=df,hue=hue,ax=ax)   
            
            elif kind=='hist':
                sns.histplot(data=df,x=x,hue=hue,ax=ax,bins=bins,multiple=multiple)
            elif kind=="heatmap": #multivariate?
                sns.heatmap(data=df,ax=ax)
      
                
            if title is not None:
                p=title
            else:
                p=str(y) + " vs " + str(x)
                p=p.replace('None vs','')
                p=p.replace('vs None','')
                p=p.replace('None',kind)
            ax.set_title(p)
        
        def feature_type(self,df,col):
            
            if col in self.id_features:
                return "id"
            elif col in self.temporal_features:
                return "temporal"
            elif df[col].dtypes!='O' and len(df[col].unique())<self.discrete_threshold:
                return "discrete"
            elif df[col].dtypes!='O' and len(df[col].unique())>=self.discrete_threshold:
                return "continuous"

            else:
                return "Unknown"
            
            
            
        
        
        def get_missing_features(self,df,print_col=False,view_heatmap=False):
            missing_features = [f for f in df.columns if df[f].isnull().sum()>0]
            data = df.copy()
            if print_col:
                for i in missing_features:
                    print(i," : ",round(100*df[i].isnull().mean(),2),"% missing")
            if view_heatmap:
                self.plot_(df=df[missing_features].isnull(),kind='heatmap')
            return missing_features
        
            
        def missing_value_dependency(self,data,target):
            '''
            Dependency of missing values with median of target
            '''
            missing_features = self.get_missing_features(data)
            for i in missing_features:    
                data[i] = np.where(data[i].isnull(),1,0)
                t = data.groupby(i)[target].median().reset_index()
                self.plot_(t,x=i,y=target,kind='bar',title="Median of {t} vs Missing {i}".format(t=target,i=i))
        
      
            
        def get_numerical_features(self,print_col=False):

            '''
            Describes Feature types given in data

            '''
            dataframe=self.df.copy()
            self.numerical = [f for f in dataframe.columns if dataframe[f].dtypes!='O' and\
                              f not in self.temporal_features + self.id_features]
            df = dataframe[self.numerical].copy()  #all numerical variables

            self.discrete_features = [f for f in df.columns if len(df[f].unique())<self.discrete_threshold]
            self.continuous_features = [f for f in df.columns if f not in \
                                        self.temporal_features + self.id_features + self.discrete_features]
            self.other_features = [f for f in dataframe.columns if f not in self.numerical and \
                                   f not in self.temporal_features + self.id_features]
            self.binary_features = [f for f in dataframe.columns if dataframe[f].nunique()==2]
            self.discrete_features_all = [f for f in dataframe.columns if len(dataframe[f].unique())<self.discrete_threshold and \
                                          f not in self.temporal_features + self.id_features]
            

            if print_col:
                func = lambda name,col1,col2: \
                print(name + " : {col1} ------- {x} %      ".format(col1=col1,x=round(100*len(col1)/len(col2),2)))

                print("\n")
                func("Numerical Columns",list(self.numerical),list(dataframe.columns))
                func("Discrete Numeric Columns",self.discrete_features,list(dataframe.columns))
                func("Continuous Numeric Columns",self.continuous_features,list(dataframe.columns))
                print("\n")
                func("Binary Columns",self.binary_features,list(dataframe.columns))
                print("\n")
                func("Other Columns",self.other_features,list(dataframe.columns))
                for i in self.other_features:
                    print(i," Cardinality ",round(dataframe[i].nunique()*100/len(dataframe[i].dropna()),2), "%")

            
        def discrete_target_plot(self,target):
            '''
            Displays countplot between a target variable(x axis) and the remaining discrete variables (including categorical)
            Do not use if discrete_threshold is very high (>=20)
            '''

            discrete_features = self.discrete_features
            features = [x for x in discrete_features if x!=target]
            print("Target Feature : ",target)
            print("Features Reviewed : ", features)
            
            for i in features:
                temp = self.df.groupby(i)[target].median().reset_index()
                self.plot_(df=temp,kind='bar',x=i,y=target,figsize=(10,10))
        
        def continuous_hist_plot(self):
            continuous_features = self.continuous_features
            print("Continuous Features : ",continuous_features)
            
            for i in continuous_features:
                self.plot_(df=self.df,kind='hist',x=i,figsize=(6,6))
                

           

