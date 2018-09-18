import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import itertools

def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')


data = pd.read_csv("../../output/test.csv")
data["code"] = pd.factorize(data['age'])[0]
data['is_train'] = np.random.uniform(0, 1, len(data)) <= 0.5
train, test = data[data['is_train'] == True], data[data['is_train'] == False]

features = data.columns[1:-7]

clf = RandomForestClassifier(n_jobs=2, random_state=0)
clf.fit(train[features], train['code'])
preds = clf.predict(test[features])


cm = confusion_matrix(test['code'], preds, labels=None, sample_weight=None)

classes = data['age'].sort_values().unique()

plot_confusion_matrix(cm, classes)

plt.savefig("../../output/cm.png")