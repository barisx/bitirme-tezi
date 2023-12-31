from sklearn.datasets import make_classification
from matplotlib import pyplot as plt
from sklearn.linear_model import LogisticRegression
import seaborn as sns
sns.set()
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import pandas as pd

x,y = make_classification(
	n_samples = 396,
	n_features = 33,
	n_classes = 2,
	n_clusters_per_class = 1,
	flip_y = 0.03,
	n_informative = 1,
	n_redundant = 0,
	n_repeated = 0)

plt.scatter(x,y,c=y,cmap = 'rainbow')
x_train, xtest, y_train, y_test = train_test_split(x,y,random_state = 1)
lr = LogisticRegression()

lr.fit(x_train, y_train)

print(lr.coef_)
print(lr.intercept_)

y_pred = lr.predict(x_test)
confusion_matrix(y_test, y_pred)

lr.predict_proba(x_test)

df = pd.DataFrame({'x': x_test[:,0], 'y': y_test})
df = df.sort_values(by='x')

from scipy.special import expit

sigmoid_fuction = expit(df['x'] * lr.coef_[0][0] + 
	lr.intercept_[0]).ravel()

plt.plot(df['x'], df['y'], c = df['y'], cmap = 'rainbow', edgecolors = 'b')

