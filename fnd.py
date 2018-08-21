
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score
from sklearn.externals import joblib
from sklearn import linear_model
def fake_news():
    df=pd.read_csv('/home/san_16398/Desktop/cleaned.csv')

    df_x =df["Message"]
    df_y=df["label"]

    tfidf=TfidfVectorizer(min_df=1,stop_words='english')
    X_train, X_test, y_train, y_test = train_test_split(df_x,df_y)
    # X_train, X_test, y_train, y_test = train_test_split(df_x, df_y, test_size=0.2, random_state=0)
   # print(type(X_test))

    y_train=y_train.astype('int')
    y_test=y_test.astype('int')
    #print(X_train.tolist())


    x_traintf =tfidf.fit_transform(X_train.tolist())
    x_testtf=tfidf.transform(X_test.tolist())

    model=svm.LinearSVC()
    model.fit(x_traintf,y_train)
    joblib.dump(model,'model.pkl')
    joblib.dump(tfidf,'transformer.pkl')

    # pred = model.predict(x_testtf)
    # print(pred)
    # acc=accuracy_score(y_test,pred)
    # print(acc)
    # return pred
fake_news()

