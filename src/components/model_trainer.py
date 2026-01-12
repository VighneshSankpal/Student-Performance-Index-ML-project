import os
import joblib
import pandas as pd
import numpy as np

# import ML models
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from dataclasses import dataclass

# model evaluation
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

@dataclass 
class ModelTrainerConfig:
    trainer_path :str = os.path.join('artifacts','model.pkl')

class ModelTrainer:
    def __init__(self):
        self.trainerConfig = ModelTrainerConfig()
    
    def _train_model(self,train_data_path,test_data_path ,preprocessor_path):
        try:
            preprocessor = joblib.load(preprocessor_path)
            print("Before drop.")
            train_data = pd.read_csv(train_data_path)
            test_data = pd.read_csv(test_data_path)
            # Train data
            X_train = train_data.drop('Performance Index',axis=1)
            y_train = train_data['Performance Index'].values

            # Test Data
            X_test = test_data.drop('Performance Index',axis=1)
            y_test = test_data['Performance Index'].values

            model = Pipeline(steps=[('preprocessor',preprocessor),('model',LinearRegression())])

            model.fit(X_train,y_train)

                
            y_pred = model.predict(X_test)



            mae = mean_absolute_error(y_test,y_pred)
            mse = mean_squared_error(y_test,y_pred)
            r2 = r2_score(y_test,y_pred)
            

            print("MAE :",mae)
            print("MSE :",mse)
            print("R2 Score :",r2)
            
    
    


            return model
            

        except Exception as e:
            print("Exception occures in model_trainer file.")
            raise e

    
    def create_model_obj(self,train_data_path,test_data_path,preprocessor_path):
        '''
        Trained Model and save it in pickle file. 
        
        train_data: Dataframe, data for train the model
        preprocessor_path: the address of the preprocessor object where saved. 
        '''

        if os.path.isfile(self.trainerConfig.trainer_path):
            print("Model Already Exist")
            return self.trainerConfig.trainer_path
        else:

            joblib.dump(value=self._train_model(train_data_path,test_data_path,preprocessor_path),
                        filename=self.trainerConfig.trainer_path
                       )
            
            print("Model Build and Save Successfully!")
            return self.trainerConfig.trainer_path
