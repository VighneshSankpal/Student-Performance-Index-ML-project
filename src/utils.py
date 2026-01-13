from src.components.data_ingetion import DataIngetion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

import joblib
import pandas as pd




def start_process():
    '''
    This method start the project of data collection, preprocessing and model building.
    '''

    data_ingetion= DataIngetion()
    data_ingetion.initiate_data_ingetion()

    data_transformation = DataTransformation()

    modeltrainer= ModelTrainer()

    train_data_path =data_ingetion.ingetion_config.train_data_path
    test_data_path = data_ingetion.ingetion_config.test_data_path
    preprocessor_path= data_transformation.save_preprocessor_object()
    modeltrainer.create_model_obj(train_data_path=train_data_path,
                                test_data_path=test_data_path,
                                preprocessor_path=preprocessor_path)
    
    print("Model Process finish.")



class Model:
    def __init__(self):
        self.model =  joblib.load(ModelTrainer().trainerConfig.trainer_path)

def predict(data):
    '''
    This method predict the student performance index value. based on the inpute data
    parameters:
    data : inpute data of student
    '''
    print("Predict method call.")
    df= pd.DataFrame(data)

    print("Dataframe created.")
    print(df)
    MODEL = Model().model

    y_pred =  MODEL.predict(df)
    print("Prediction is")
    print(y_pred[0])
    y_pred = y_pred[0]
    if y_pred<0:
        y_pred=0
    elif y_pred>100:
        y_pred=100

    return round( y_pred,2)










    