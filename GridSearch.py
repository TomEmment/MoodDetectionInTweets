import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB, GaussianNB
from sklearn import svm
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.metrics import average_precision_score
stopwords = stopwords.words('english')

dataframe = pd.read_csv("MasterExtraClean.csv")
#read 10,11,16

y = dataframe["Label"]
x = dataframe["Text"]



x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.15, random_state=23)

cv = CountVectorizer()

features = cv.fit_transform(x_train)
features_test = cv.transform(x_test)

svc = svm.SVC()

Grid = [{'kernel': ['linear','poly','rbf','sigmoid'], 'C':[0.01,0.05], 'probability':[True]}]

Model = GridSearchCV(estimator=svc, param_grid = Grid, return_train_score = True ).fit(features,y_train)

print(Model.cv_results_)
