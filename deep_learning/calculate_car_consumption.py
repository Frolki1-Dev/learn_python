import pandas as pd
from sklearn.linear_model import LinearRegression


def mpg_to_l_per_100km(mpg):
    LITERS_PER_GALLON = 3.785411784
    KILOMETERS_PER_MILES = 1.609344

    return (100 * LITERS_PER_GALLON) / (KILOMETERS_PER_MILES * mpg)


df = pd.read_csv("../data/mpg-dataset.csv")

X = df[["cylinders", "horsepower", "weight"]]
y = mpg_to_l_per_100km(df["mpg"])

modal = LinearRegression()
modal.fit(X, y)

print(modal.predict([
    [8, 200, 2500]
]))
