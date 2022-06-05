# ECS 171 Project Team 19 - ML Approaches for Predicting the Outcome of Football Plays

# 🏈 Description of Project

The goal of this project is to build a machine learning solution to predict the outcome of a football play, based on 8 attributes related to game play.

# 📈 Dataset Used

['NFL Play by Play 2009-2018 (v5)'](https://www.kaggle.com/datasets/maxhorowitz/nflplaybyplay2009to2016) from Kaggle

# 💻Run Project Locally

## Dependencies: 
Data Preprocessing and ML Model Dependencies:

- Pandas
- Numpy
- seaborn
- matplotlib
- sklearn
- cvxpy

Frontend Dependencies:

- pickle
- Python 3.9
- [Flask](https://phoenixnap.com/kb/install-flask)



## 📊 Run Data Preprocessing Code:

1.  Ensure original dataset ['NFL Play by Play 2009-2018 (v5).csv'](https://www.kaggle.com/datasets/maxhorowitz/nflplaybyplay2009to2016) is downloaded and is located in  the ```Data_Preprocessing_Code``` directory.
2. Run ```ECS171project_final_data_preprocessing.ipynb```
   - This will generate a new csv file, ```NFL_data_super_cleaned.csv``` in the ```Data_Preprocessing_Code``` directory.

## 🧑‍💻 Run ML Model Code:

1. Move ```NFL_data_super_cleaned.csv``` (generated during preprocessing) into the ```ML_Models``` directory.
2. Pick a model to run!


## 🖥️ Run Interactive Frontend:

#### 1. Frontend Environment Setup:

Two directories contain the website user interface. "NFLPrediectService"(this the backend service including a python api), and "NFL_Score_Predict" (this is the front-end ).

1. You need an IDE and Python 3.9 to use the service (for example, Pycharm).
2. Add Python configuration to your IDE.
3. Ensure Flask is installed.

#### 2. Run Frontend:

1. Move dataset ```NFL_data_super_cleaned.csv``` to ```NFLPredictService``` directory.
2. Run the notebook ```Generate_SVM_Model.ipynb``` (takes 2-8 minutes to run).
   This will generate 2 new files in the  ```NFLPredictService``` directory: 
   1. ```finalized_svm_model.sav``` (Pickle archive of the trained SVM model).
   2. ```scaler.pkl``` (Pickle archive of the scaler used by the SVM model).

3. Go to the directory ```NFL_Score_Predict``` and run ```predict.html```.
   This should start a server and give you the option to open the Frontend in a browser. From there, you can input your own football plays into the form on the "Predict" tab, and see what the model predicts the outcome of the play will be.

# ✍️ Contributors

* [nnathalied](https://github.com/nnathalied)
* [SleepySeaOtter](SleepySeaOtter)
* [ZubayrMohammad](https://github.com/ZubayrMohammad)
* [hjoh2](https://github.com/hjoh2)
* [rookieCoderLin](https://github.com/rookieCoderLin)
* [amashiana](https://github.com/amashiana)
* [Nsingh13](https://github.com/Nsingh13)
