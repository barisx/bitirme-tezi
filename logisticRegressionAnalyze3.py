import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

data = pd.read_csv("StudentsPerformance.csv", header = 0)
data.dropna()
print(data.shape)
print(list(data.columns))
data.columns = ['cinsiyet','etnik','ailenin eğitim seviyesi','öğle yemeği','dershane','matematik','okuma','yazma']

print(data.info())

print(data.head())
test  = pd.read_csv("test.csv", header = 0)
y_train = pd.DataFrame(data["math score"])
x_train = data.drop(["gender","race/ethnicity","parental level of education","lunch","test preparation course"],1)
x_test = test.drop(["gender","race/ethnicity","parental level of education","lunch","test preparation course"],1)











