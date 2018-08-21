from sklearn.externals import joblib
from sklearn.feature_extraction.text import TfidfVectorizer


def fake_fake(headline):
    model = joblib.load('/home/san_16398/PycharmProjects/fakenewsdetector/model.pkl')
    tfidf = joblib.load('/home/san_16398/PycharmProjects/fakenewsdetector/transformer.pkl')
   # print([headline])
    x_testtf = tfidf.transform([headline])
    ans = model.predict(x_testtf)
    return ans