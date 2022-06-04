# Classification-of-images-with-Clear-cell-renal-cell-carcinoma-using-Keras
Background
Renal cancer accounts for about 2% of all cancer diagnoses in the world. According to GLOBOCAN, about 400,000 cases in the world are diagnosed annually (about 2.2% of cancer diagnoses). The ratio of men to women is about 2:1. (you can read more about epidemiology here). Clear cell renal cell carcinoma is a type of cancer whose cells have a clear (hence the name) or eosinophilic (pink) cytoplasm. This is the most common type of kidney cancer in adults and accounts for 65–70% of all cases. Often associated with a mutation in the tumor growth suppressor (VHL) gene.

Dataset
Even taking into account the development of digital pathology and the ability to share slides, it is quite difficult to find in the public domain a sufficient number of images of a certain type of tumor (and not only a tumor) suitable for model training and validation.
For the project, I chose a collection of slides of histological images stained with hematoxylin and eosin with clear cell renal cell carcinoma of the project of the National Cancer Institute of the USA “Clinical Proteomic Tumor Analysis Consortium, CPTAC) Clear Cell Renal Cell Carcinoma (CPTAC-CCRCC ). The data is available on the Cancer Imaging Archive (TCIA) website.
I chose this dataset because of the large amount of available material (size — 190 GB) , which should not cause problems with the preparation of data for training, validation and test datasets, model training. Images are available for download in .svs format.
There are also clinical data of patients, genetic research results (e.g. VHL status). It was not used in my project, but it can be used in the future: for example, try to train a model predicting the status of the VHL gene according to the histological image.
I also want to note several disadvantages of the dataset at once:
A) WSI without annotations. Since I am a pathologist by education and the study of histological material is my work , I was annotating the slides on my own.
B) There are only good quality slides: there are almost no artifacts and uninformative images that are not rare in routine medical practice. This affects the results of the model (the results will be better than when using the model in real clinical practice).
