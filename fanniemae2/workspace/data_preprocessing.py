import pandas as pd
import numpy as np

class DataPreprocessing:
    def __init__(self, file1, file2):
        self.file1 = file1
        self.file2 = file2
    
    def load_data(self):
        df1 = pd.read_csv(self.file1)
        df2 = pd.read_csv(self.file2)
        return df1, df2
    
    def clean_data(self, df1, df2):
        # Drop any rows with missing values
        df1.dropna(inplace=True)
        df2.dropna(inplace=True)
        
        # Convert columns to appropriate data types
        df1['delinquency_rate'] = df1['delinquency_rate'].astype(float)
        df1['total_upb'] = df1['total_upb'].astype(float)
        df1['current'] = df1['current'].astype(int)
        df1['lag'] = df1['lag'].astype(int)
        
        df2['total_forb_as_percent'] = df2['total_forb_as_percent'].astype(float)
        df2['current'] = df2['current'].astype(int)
        df2['lag'] = df2['lag'].astype(int)
        
        return df1, df2
    
    def prepare_data(self, df1, df2):
        # Merge the two dataframes on the 'current' and 'lag' columns
        merged_df = pd.merge(df1, df2, on=['current', 'lag'])
        
        # Drop any unnecessary columns
        merged_df.drop(['current', 'lag'], axis=1, inplace=True)
        
        # Convert the merged dataframe to a numpy array
        data = merged_df.to_numpy()
        
        # Split the data into features and labels
        X = data[:, :-1]
        y = data[:, -1]
        
        return X, y
