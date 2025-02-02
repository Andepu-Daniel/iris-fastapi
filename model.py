from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train)

with open('model.pkl', 'wb') as f:
    pickle.dump(model, f, protocol=4)