import os 

DATA_DIR = 'data'
DATA_FILENAME = 'dataset.csv'
DATA_FILEPATH = os.path.join(DATA_DIR, DATA_FILENAME)

APP_DIR = 'app'
MODEL_DIR_NAME = 'models'
MODEL_NAME = 'model.joblib'
MODEL_DIR = os.path.join(APP_DIR, MODEL_DIR_NAME)
MODEL_FILEPATH = os.path.join(MODEL_DIR, MODEL_NAME) 