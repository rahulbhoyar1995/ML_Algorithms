import pandas as pd 
import numpy as np

class RegressionModel:
    """
    This is simple Regression Model used for predicting the Box Office
    Collection of Hollywood movies based on certain predictors
    """
    test_data = ""
    train_data = ""
    
    def creating_dataframe(self, csv_file_location : str) -> pd.DataFrame:
        df = pd.read_csv(csv_file_location)
        return df
    
    @classmethod
    def creating_training_data(cls, df):
        
    
    
test_df = RegressionModel().creating_dataframe("/Users/rahulbhoyar/Desktop/Rahul_PC/projects/ML_Algorithms/1_Regression_Problem/datasets/movie_dataset.csv")
print(test_df)
