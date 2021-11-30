from sklearn.linear_model import LinearRegression
from joblib import dump, load

X = float()  # some iterable of values
y = float()  # some iterable of values

model = LinearRegression()
model.fit(X, y)  # Looks for sum of distances should be shortest.

# y = a*x + b
b = model.intercept_
a = model.coef_

how_well_it_fits = model.score(X, y)
model.predict([[10]])

# save your model
dump(model, 'linear.joblib')

# load your model
model = load('linear.joblib')

