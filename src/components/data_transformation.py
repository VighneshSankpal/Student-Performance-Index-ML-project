import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler,OneHotEncoder,FunctionTransformer
import os
import joblib
from dataclasses import dataclass

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path :str = os.path.join("artifacts",'preprocessor.pkl')
    
class DataTransformation:
    def __init__(self):
        self.transformation_config= DataTransformationConfig()
    
    def _to_lower_case(self,X):
        return np.char.lower(X.astype(str))
    def _get_column_transformer_obj(self):
        try:
            # We Separet the dataset into two types as,
            #  1. Numeric columns
            #  2. categorical column

            # Pipeline for Numeric type features.
            num_pipeline = Pipeline(steps= [('impute',SimpleImputer(strategy='median')),
                                            ('scaled',StandardScaler())                                    
                                    ])
            
            # Pipeline for Categorical type features.
            cat_pipeline = Pipeline(steps=[('impute',SimpleImputer(strategy='most_frequent')),
                                           ('lowercase',FunctionTransformer(self._to_lower_case,validate=False)),
                                           ('encoder',OneHotEncoder(handle_unknown='error',sparse_output=False)),
                                           
                                    ])
            # Intigrate this pipeline in column transformer 

            # Numeric features
            numerical_columns = ['Hours Studied', 'Previous Scores', 'Sleep Hours', 'Sample Question Papers Practiced']

            # Categorical features
            categorical_columns =['Extracurricular Activities']    
            
            # preprocessor object

            preprocessor = ColumnTransformer(transformers=[('num_col',num_pipeline,numerical_columns),
                                                           ('cat_col',cat_pipeline,categorical_columns)
                                                           ])
            

            return preprocessor           

            

        except Exception as e:
            print("Exception Occur in Preprocessor obj method.")
            print(e)
        
    
    def save_preprocessor_object(self):
        '''
        Save the object in pickle format and return the path
        '''
        path = os.path.join('artifacts','preprocessor.pkl')
        print("Check exist or not....")
        if os.path.isfile(path):
            print("Pre-processor Model already Exist.")
        
        else:
            print("Preprocessor Object saved successfully!")
            joblib.dump(filename=path,value=self._get_column_transformer_obj())

        return path


