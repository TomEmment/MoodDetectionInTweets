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



model6 = svm.SVC(kernel = 'rbf',probability=True, C = 0.05)
model6.fit(features,y_train)
print("Accuracy for radial basis function kernal (0.05): ", model6.score(features_test,y_test))

print("Accuracy on training radial kernal (0.05): ", model6.score(features,y_train))





Message = ""
while Message != ("Exit" or "Stop" or "stop" or "exit" or "0"):
    Message = input("Enter a message to check: ")
    Check = word_tokenize(Message)
    Message = {w for w in Check if not w in stopwords}
    Message = " ".join(Message)
    Check = [Message] 
    Final = cv.transform(Check)
    print("Model predicition: ", model6.predict(Final),"Probability Happy/Sad:",model6.predict_proba(Final))

    
