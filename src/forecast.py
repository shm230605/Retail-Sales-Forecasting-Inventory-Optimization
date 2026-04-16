def forecast(model, df):
    X = df[["lag_1", "lag_7", "rolling_mean_7", "rolling_std_7", "day_of_week"]]
    df["forecast"] = model.predict(X)
    return df