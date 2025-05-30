# -*- coding: utf-8 -*-
"""Predict.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1w4-gjFEU6HzA5n60aBavHxbQF7VT4Bj5
"""

def predict_attrition(user_input_dict):
    import pandas as pd
    import joblib

    # Load model
    model = joblib.load("attrition_model.pkl")


    input_df = pd.DataFrame([user_input_dict])

    expected_columns = model.feature_names_in_
    input_df = input_df[expected_columns]

    # Prediksi
    prediction = model.predict(input_df)[0]
    return "Akan Keluar" if prediction == 1 else "Aman Bertahan"