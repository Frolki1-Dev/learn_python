from sklearn.linear_model import LogisticRegression

X = [
    [50],
    [60],
    [70],
    [20],
    [10],
    [30]
]

y = [
    1,
    1,
    1,
    0,
    0,
    0
]

model = LogisticRegression(C=100000)
model.fit(X, y)

print(model.predict_proba([
    [35],
    [9],
    [44]
]))
