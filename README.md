## Biostratigraphy By ML


### Train a machine learning algorithm to perform biostratigraphic interpretations on data from Volve.

Biostratigraphic data typically consists of counts of different fossil species. Using knowledge of the historical prevelance of certain species it is used to inform geoscientists about the probable period of deposition.

Included in Equinor's release of data from the Volve field there are 7 wells with biostratigraphic data available. Of these, 5 have biostratigraphic interpretations which can be used as labels to train a machine learning algorithm to make its own interpretations. In this project we will test our ability to automatically generate interpretations on known wells and attempt generalization to the uninterpreted wells.

---

Wells with fossil counts _and_ biostratigraphic interpretation:

  * 15_9-F-1
  * 15_9-F-1 A
  * 15_9-F-1 B
  * 15_9-F-11 A
  * 15_9-F-11 B

Wells with fossil counts _only_:

  * 15_9-F-4
  * 15_9-F-10
