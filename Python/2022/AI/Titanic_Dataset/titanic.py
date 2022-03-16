# March 11, 2022
# Programmed by Parker Cranfield
#
# Built for my Introduction to Artificial Intelligence
#
# Useing the 'data-Titanic.xlsx' file, I made an ANN and a Decision Tree to predict who would survive and who wouldn't
#
# The included Jupyter Notebook file also has this code - and would be best if ran through Jupyter (more comments were made)
# -----------------------------

# Import for data cleaning and visualization
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Import sklearn to split the data
from sklearn.model_selection import train_test_split
# Get the ANN
from sklearn.neural_network import MLPClassifier
# Import metrics to find the stats about the accuracy
from sklearn import metrics
# Import Tree
from sklearn.tree import DecisionTreeClassifier

# Set data
titanic = pd.read_excel("data-Titanic.xlsx", index_col=0)
# print(titanic)

# Checks for empty data
# Print to check
titanic.isnull().sum()

# Removes all lines in the set that have null values for age
titanic = titanic.drop(titanic.index[titanic.Age.isnull()])

# Show that they are gone
# Print to check
titanic.isnull().sum()

# Set up survived table for later use
titanic_df_survived = titanic['Survived']

# Removed rubbish data - data useless to the models
titanic_df = titanic.drop(['Name', 'Ticket', 'Fare', 'Cabin', 'Embarked', 'Survived'], axis=1)
# print(titanic_df)

# Make Male & Female = 1's & 0's

gender_id = {
    'male': 1,
    'female': 0
}

titanic_df['Gender'] = [gender_id[i] for i in titanic_df['Gender'].values]

# New data
# print(titanic_df)

# ------------- Setup Data for Models -------------

x_train, x_test, y_train, y_test = train_test_split(titanic_df, titanic_df_survived, test_size = 0.1)

# ------------- ANN -------------
# Setup ANN
mlp = MLPClassifier(hidden_layer_sizes=(10), max_iter=15000)

# Set the data
mlp.fit(x_train, y_train)

# Calculate the results of the training data
y_pred = mlp.predict(x_train)

# Compares it with the results (y_train)
print('ANN training accuracy: ', metrics.accuracy_score(y_train, y_pred), '\n')
# The accuracy is ~81% - which is quite decent

# ------------- Decision Tree -------------
# Setup tree
t_model = DecisionTreeClassifier(max_depth = 4)
t_model.fit(x_train, y_train)
# See accuracy of training data
y_predict = t_model.predict(x_train)
print('Tree training accuracy: ', metrics.accuracy_score(y_train, y_predict), '\n')
# See accuracy of testing data
y_pred = t_model.predict(x_test)
print('Tree testing accuracy: \t', metrics.accuracy_score(y_test, y_pred))
# The trees results varied a lot more, and I would argue the ANN was a lot more precise with its predictions
# as its accuracy doesn't vary much, unlike the tree