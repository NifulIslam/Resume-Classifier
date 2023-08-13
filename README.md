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
Replace _**your_folder_location**_ with the path to the folder containing the resumes you want to classify.

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

