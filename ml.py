import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

imputer = SimpleImputer()

def get_model(imputer=imputer):

    # Load the data
    X = pd.read_csv('cleaned_x.csv')
    y = pd.read_csv('cleaned_y.csv')['Escherichia coli']

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state=101)

    X_train = imputer.fit_transform(X_train)

    # Train the model
    model = RandomForestRegressor(random_state=101)
    model.fit(X_train, y_train)

    # print(model.score(imputer.transform(X_test), y_test))

    return model

def prepare_data(values, imputer=imputer):
    df = pd.DataFrame([values], columns=['Dissolved oxygen (DO)', 'Nitrate', 'Orthophosphate',
       'Specific conductance', 'Temperature, water', 'Total suspended solids',
       'Turbidity', 'pH'], index=None)
    # return df
    # print(df)
    transformed = imputer.transform(df)
    # print(transformed)
    return transformed

# def predict(values, model):
#     return model.predict(values)

model = get_model(imputer)
values = [1.06900000e+01, 1.41000000e-01, 1.70000000e-01, 2.70500000e+02, 1.31000000e+01, 1.07142857e+01, 3.05000000e+00, 7.54000000e+00]
# values = prepare_data(values, imputer)
# print(model.predict(values))

def predict(values):
    data = prepare_data(values)
    return model.predict(data)

# print(predict(values))