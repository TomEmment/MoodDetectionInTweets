import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB, GaussianNB
from sklearn import svm
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.metrics import average_precision_score
from sklearn.linear_model import LogisticRegression

dataframe = pd.read_csv("MasterExtraClean.csv")
#read 10,11,16

y = dataframe["Label"]
x = dataframe["Text"]



x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.15, random_state=23)

cv = CountVectorizer()

features = cv.fit_transform(x_train)
features_test = cv.transform(x_test)

model = LogisticRegression(C=0.05).fit(features, y_train)
print("Accuracy for logistic regression: ", model.score(features_test,y_test))
print("Accuracy on training logistic regression: ", model.score(features,y_train))


