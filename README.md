# Classification of images with Clear cell renal cell carcinoma using Keras
My own project for classification of histological images with clear cell renal cell carcinoma.

![main](https://user-images.githubusercontent.com/55003096/172024737-cc26f37b-e8d8-4bf0-9036-2ff3b1426806.png)

Steps :
1. Obtaining Whole-slide images (WSI) — preparing a dataset.
2. Image annotation.
3. Getting a prepared dataset (Train, Validation and Test)
4. Training models
5. Testing models

## Dataset
For the project, I chose a collection of slides of histological images stained with hematoxylin and eosin with clear cell renal cell carcinoma of the project of the National Cancer Institute of the USA “Clinical Proteomic Tumor Analysis Consortium, CPTAC) Clear Cell Renal Cell Carcinoma (CPTAC-CCRCC ). The data is available on the Cancer Imaging Archive (TCIA) website https://wiki.cancerimagingarchive.net/display/Public/CPTAC-CCRCC.

## WSI annotations
I annotated WSI by myself , using QuPath 0.3.2.
Initially, I defined 5 classes :
1.Blood
2. Clear cell renal cell carcinoma(CCRCC)
3. Fat
4. Kidney
5. Stroma. It is a connective tissue that is not a specific element and can occur in both normal tissue and tumor. This also includes the walls of vessels, etc.

![classes](https://user-images.githubusercontent.com/55003096/172024831-499a6eb4-7cd5-4423-86f1-81bad5325409.png)

Slides were annotated with QuPath : large zones belonging to a class were marked, and then with the help of the built-in functionality of the program, these zones were divided into tiles, on which neural networks were subsequently trained.

![qupath_1](https://user-images.githubusercontent.com/55003096/172024856-313efd51-43af-4c1a-9023-9f2bb642cc9b.png)

![qupath_2](https://user-images.githubusercontent.com/55003096/172024861-16b19ff3-bcb0-40c9-8297-cacef3e95fe1.png)

## Getting a prepared dataset (Train, Validation and Test)

The coordinates of objects with class labels were exported in JSON (Pretty JSON) format, and then images in .jpeg format and 256x256 pixels resolition were extracted from the slides using the OpenSlide library in Python. No methods of augmentation or normalization of coloring were not applied to the images.

https://github.com/bluewhale28/Classification-of-images-with-clear-cell-renal-cell-carcinoma-using-Keras/blob/main/CCRCC_Classification_Extraction_tiles.ipynb

![qupath_1](https://user-images.githubusercontent.com/55003096/172025007-420849b4-ade8-4f7c-8a81-7a2b3fa82e82.png)

![qupath_2](https://user-images.githubusercontent.com/55003096/172025012-2fb82835-5c97-468f-a301-6927bf5ef75f.png)


## Training models
Three models implemented on Keras were used for training:
1. InceptionV3
2. EfficientNetV2S
3. ResNet101V2

![models](https://user-images.githubusercontent.com/55003096/172024941-42d9ac64-874d-4505-8090-47292aea0fb8.png)

https://github.com/bluewhale28/Classification-of-images-with-clear-cell-renal-cell-carcinoma-using-Keras/blob/main/CCRCC_classification_Train.ipynb

Loss function-categorical crossentropy

Metrics : Accuracy score, ROC_AUC, PR_AUC, Precision, Recall

## Results

![results](https://user-images.githubusercontent.com/55003096/172024957-d9b21bfd-80c2-43c8-80af-f97b70ed7293.png)
