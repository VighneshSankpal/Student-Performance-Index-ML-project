import pandas as pd
import os
import sys
from dataclasses import dataclass
from sklearn.model_selection import train_test_split
@dataclass
class DataIngetionConfig:
    train_data_path: str= os.path.join("artifacts",'train.csv') 
    test_data_path: str= os.path.join("artifacts",'test.csv') 
    raw_data_path: str= os.path.join("artifacts",'raw.csv') 


class DataIngetion():
    def __init__(self):
        self.ingetion_config = DataIngetionConfig()
        

    def initiate_data_ingetion(self):
        try:
            DATA_PATH='Student_Performance.csv'

            df = pd.read_csv(DATA_PATH)

            #Create the Artifact directory.            
            os.makedirs(os.path.dirname(self.ingetion_config.train_data_path),exist_ok=True)

            # Save the raw_data.csv file . 
            df.to_csv(self.ingetion_config.raw_data_path,index=False,header=True)

            train_data, test_data = train_test_split(df, test_size=0.25,random_state=64)

            # Save train.csv file
            train_data.to_csv(path_or_buf=self.ingetion_config.train_data_path,index=False,header=True)

            # Save test.csv file
            test_data.to_csv(path_or_buf = self.ingetion_config.test_data_path,index=False,header=True)


            return (
                self.ingetion_config.train_data_path,
                self.ingetion_config.test_data_path
            )

        except Exception as e:
            print("Exception occur in data_ingetion_loading.")
            print(e)


