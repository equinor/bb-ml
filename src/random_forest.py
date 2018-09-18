import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

data = pd.read_csv("../../output/test.csv")
data["code"] = pd.factorize(data['label'])[0]
data['is_train'] = np.random.uniform(0, 1, len(data)) <= 0.5
train, test = data[data['is_train'] == True], data[data['is_train'] == False]

print(test.head())

features = data.columns[1:-4]
print(features)

y = train['code']

print(y)

clf = RandomForestClassifier(n_jobs=2, random_state=0)
clf.fit(train[features], y)

preds = clf.predict(test[features])
print(preds)

y_test = test['code']

cm = pd.crosstab(y_test, preds, rownames=['Actual Period'], colnames=['Predicted Period'])

print(cm)
