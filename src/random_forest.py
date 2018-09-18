import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt

data = pd.read_csv("../../output/test.csv")
data["code"] = pd.factorize(data['label'])[0]
data['is_train'] = np.random.uniform(0, 1, len(data)) <= 0.5
train, test = data[data['is_train'] == True], data[data['is_train'] == False]

features = data.columns[1:-4]

clf = RandomForestClassifier(n_jobs=2, random_state=0)
clf.fit(train[features], train['code'])
preds = clf.predict(test[features])

cm = confusion_matrix(test['code'], preds, labels=None, sample_weight=None)
print(cm)


plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
plt.savefig("../../output/cm.png")