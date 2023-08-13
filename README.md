# Resume Classifier

This project is a Resume Classifier that organizes resumes based on their content.

## Getting Started

Follow these steps to get the project up and running:

1. Clone the repository:
   ```bash
   git lfs clone git@github.com:NifulIslam/Resume-Classifier.git
2. Navigate to the project directory:
   ```bash
   cd Resume-Classifier
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
4. Run the script:
   ```bash
   python script.py your_folder_location
Replace _**your_folder_location**_ with the path to the folder containing the resumes you want to classify. These commands will create folders for the corresponding resume type and will make a copy of the resumes in each folder. Moreover, it will generate a _categorized_resumes.csv_ file that contains the file corresponding to the category. 

# Data Preprocessing

Before building our classifier, we conducted some essential data preprocessing steps to ensure the quality of the input data. Here's an overview of the preprocessing process:

## Data Distribution

We started by analyzing the data distribution to understand the balance between the classes. The image below presents the data distribution:

![Data Distribution](https://github.com/NifulIslam/Resume-Classifier/blob/master/images/occurences.png)

Since the data distribution is mostly balanced, there is no need for further balancing techniques.

## Resume Length Analysis

Next, we visualized the length of each resume in our dataset to get an idea of the distribution. The image below shows the distribution of resume lengths:

![Resume Length Distribution](https://github.com/NifulIslam/Resume-Classifier/blob/master/images/resume_length.png)

Since there are some outliers in the data, we decided to use the mean plus three times the standard deviation of the length as the vocabulary size for our vectorization techniques.

## Train Test Split
The dataset has been divided into three parts - train, test and validation - with a ratio of 70:20:10.

## Vectorization

We used the TF-IDF (Term Frequency-Inverse Document Frequency) vectorization technique, to convert the textual data into a format suitable for machine learning and deep learning models.

## Model Performance on TF-IDF Dataset

We trained various machine learning and deep learning models on the TF-IDF vectorized dataset. The image below shows the accuracy of different models on the TF-IDF dataset:

![Model Accuracy on TF-IDF Dataset](https://github.com/NifulIslam/Resume-Classifier/blob/master/images/ml-accuracy.png)

These preprocessing steps ensure that the input data is well-prepared for training our resume classifier.


## Benchmark Study

The table below presents the results of the benchmark study:

| Preprocessing/Vectorization Type | Model                               | Accuracy      | Precision     | Recall        | F1-Score      | MCC           |
|---------------------------------|-------------------------------------|---------------|---------------|---------------|---------------|---------------|
| TFIDF                           | Logistic Regression                  | 0.7475        | 0.7779        | 0.7475        | 0.7382        | 0.7374        |
| TFIDF                           | Support Vector Machine               | 0.6667        | 0.7186        | 0.6667        | 0.6690        | 0.6523        |
| TFIDF                           | Decision Tree                        | 0.2374        | 0.2174        | 0.2374        | 0.2135        | 0.3187        |
| TFIDF                           | K Nearest Neighbors                 | 0.5152        | 0.5984        | 0.5152        | 0.5361        | 0.4955        |
| TFIDF                           | Random Forest                        | 0.6869        | 0.6768        | 0.6869        | 0.6573        | 0.6735        |
| TFIDF                           | Extra Trees                          | 0.6919        | 0.6924        | 0.6919        | 0.6688        | 0.6793        |
| TFIDF                           | Bagging Classifier                   | 0.7576        | 0.7847        | 0.7576        | 0.7516        | 0.7475        |
| TFIDF                           | Gradient Boosting                    | 0.7778        | 0.8086        | 0.7778        | 0.7781        | 0.7689        |
| **TFIDF with Stop Words Deletion**   | **Gradient Boosting**                    | **0.7980**        | **0.8292**        | **0.7980**        | **0.7983**        | **0.7899**        |
| TFIDF with Stop Words Deletion and Keeping Alphabets only | Gradient Boosting  | 0.7626   | 0.7935        | 0.7626        | 0.7662        | 0.7531        |
| Bag of Words                    | Gradient Boosting                    | 0.7828        | 0.8148        | 0.7828        | 0.7850        | 0.7741        |
| TFIDF with Stop Words Deletion   | Multi-layer Perceptron               | 0.6616        | 0.6616        | 0.6616        | 0.6678        | 0.6464        |
| TFIDF with Stop Words Deletion   | Multi-layer Perceptron with Dropout  | 0.6566        | 0.6928        | 0.6566        | 0.6560        | 0.6417        |
| TFIDF with Stop Words Deletion   | Bi-LSTM                             | 0.0303        | 0.0035        | 0.0303        | 0.0054        | 0.0072        |
| Auto Tokenizer                  | Bert(Full Trainable)                 | 0.0303        | 0.0009        | 0.0303        | 0.0018        | 0             |
| Auto Tokenizer                  | Bert(Pretrained)                    | 0.3889        | 0.4034        | 0.3889        | 0.3438        | 0.3645        |

Since Gradient Boosting paired with TFIDF with Stop Words Deletion produced the best performance, we choose it as the final classifier.
