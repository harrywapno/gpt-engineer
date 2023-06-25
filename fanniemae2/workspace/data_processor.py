import pandas as pd
import numpy as np

class DataProcessor:
    def __init__(self):
        pass
    
    def read_and_preprocess_data(self):
        # Read the data from the CSV files
        del1_df = pd.read_csv('Del1.csv')
        del2_df = pd.read_csv('Del2.csv')
        
        # Merge the dataframes
        merged_df = pd.concat([del1_df, del2_df], axis=0)
        
        # Drop unnecessary columns
        merged_df.drop(['Unnamed: 0', 'Loan ID', 'Monthly Reporting Period'], axis=1, inplace=True)
        
        # Convert categorical variables to numerical
        merged_df['Prepay'] = np.where(merged_df['Prepay'] == 'Y', 1, 0)
        merged_df['Credit Event'] = np.where(merged_df['Credit Event'] == 'Y', 1, 0)
        merged_df['Removal'] = np.where(merged_df['Removal'] == 'Y', 1, 0)
        
        # Split the data into training and test sets
        X_train = merged_df.iloc[:5000, :-1].values
        y_train = merged_df.iloc[:5000, -1].values
        X_test = merged_df.iloc[5000:, :-1].values
        y_test = merged_df.iloc[5000:, -1].values
        
        return X_train, y_train, X_test, y_test
