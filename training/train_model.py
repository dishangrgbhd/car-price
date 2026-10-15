import pandas as pd
import numpy as np
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from training.train_utils import DATA_FILEPATH, MODEL_FILEPATH, MODEL_DIR


df = pd.read_csv(DATA_FILEPATH)

df = df.drop(columns = ['name', 'model', 'edition'])
df['style'] = np.where(df['year'] < 2010, "Classic", "Modern")
df = df.drop(columns = ['year'])
df = df.drop_duplicates()


X = df.drop(columns = ['selling_price'])
y = df['selling_price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

num_cols = X_train.select_dtypes(include = 'number').columns.tolist()
cat_cols = [col for col in X_train.columns if col not in num_cols]

num_pipe = Pipeline(steps = [
    ('imputer', SimpleImputer(strategy = 'median')),
    ('scaler', StandardScaler())
])

cat_pipe = Pipeline(steps = [
    ('imputer', SimpleImputer(strategy = 'constant', fill_value = 'missing')),
    ('encoder', OneHotEncoder(handle_unknown = 'ignore', sparse_output = False))
])

preprocessor = ColumnTransformer(transformers = [
    ('num', num_pipe, num_cols),
    ('cat', cat_pipe, cat_cols)
])

regressor = RandomForestRegressor(n_estimators = 20, max_depth = 4, random_state = 42)

rf_model = Pipeline(steps = [
    ('prep', preprocessor),
    ('reg', regressor)
])
rf_model.fit(X_train, y_train)

os.makedirs(MODEL_DIR, exist_ok=True)
joblib.dump(rf_model, MODEL_FILEPATH)
