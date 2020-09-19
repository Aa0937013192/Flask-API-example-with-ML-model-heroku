import pickle
import gzip

with gzip.open('app/model/xgboost-iris.pgz', 'r') as f:
    xgboostModel = pickle.load(f)
    print(xgboostModel)

def test():
    return "This is model.py"

def predict(input):
    predicted=xgboostModel.predict(input)[0]
    print(predicted)
    return predicted