import pickle
import os
import PyPDF2
import sys
import joblib
import shutil
import pandas as pd

#for reading full pdf content
def read_pdf(file_path):
    with open(file_path, "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        num_pages = len(pdf_reader.pages)
        full_text = ""
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            full_text += page.extract_text()
    return full_text

#loading model and vectorizer
model_path='models/gradient_boosting.sav'
vectorizer_paty="models/tfidf_vectorizer.pkl"
vectorizer = joblib.load(vectorizer_paty)
model=pickle.load(open(model_path, 'rb'))


location= sys.argv[1]  #location of the cv directory
files=[location+'/'+i for i in  os.listdir(location)] #saving the full location of the file
file_and_text={} #maps file name to file content
for file in files:
    file_and_text[file]=read_pdf(file)

result={}
#classify and paste cv to corresponding folder    
for file_name, file_content in file_and_text.items():
    X_test=vectorizer.transform([file_content]) #vectorizing the text
    y_pred=model.predict(X_test)[0]
    if (not( os.path.exists(y_pred) and os.path.isdir(y_pred)) ): #if directory does not exist, make the directory
        os.mkdir(y_pred)
    #copy the original file and paste to the corresponding directory
    try:
        shutil.copy(file_name, y_pred)
        file_name_split=file_name.split('/')[-1]
        result[file_name_split]=y_pred
    except:
        print("error copying file: "+ file_name)
    
result=pd.DataFrame(result.items(),columns=['filename','category'])
result.to_csv('categorized_resumes.csv',index=False)
