# AI-Powered_Medical_Diagnosis
This project is python project and it's use various python libraries file also.

Sure! Here's the provided text converted into Markdown format:

```markdown
# AI-Powered Medical Diagnosis System

This project implements an AI-powered system for the prediction of various diseases using machine learning models. The system includes models for Diabetes, Heart Disease, Parkinson's Disease, Lung Cancer, and Hypothyroidism (Thyroid Disease). It is designed to help healthcare professionals and individuals quickly assess the risk of these diseases based on inputted health data.

## Features

- **Diabetes Prediction**: Predicts whether an individual is diabetic based on features such as glucose level, BMI, and age.
- **Heart Disease Prediction**: Predicts the likelihood of heart disease using factors like cholesterol levels, exercise-induced angina, and maximum heart rate.
- **Parkinson's Disease Prediction**: Uses voice-related features to determine if an individual is likely to have Parkinson's disease.
- **Lung Cancer Prediction**: Predicts the risk of lung cancer based on factors like smoking, shortness of breath, and age.
- **Hypothyroidism (Thyroid Disease) Prediction**: Predicts whether a person is likely to have hypothyroidism based on thyroid-related features like TSH, TT4, and T3 levels.

## Technologies Used

- **Python**: Programming language used for backend development and machine learning.
- **Streamlit**: Framework for building the interactive web interface.
- **Scikit-learn**: Library used for building machine learning models.
- **Pickle**: Used to save and load the trained models.
- **Pandas and NumPy**: For handling data and performing numerical operations.

## Prerequisites

Ensure you have the following installed:
- Python 3.x
- pip (Python package installer)

## Libraries

Install the necessary Python libraries using the following commands:

```bash
pip install streamlit
pip install scikit-learn
pip install pandas
pip install numpy
pip install pickle-mixin
```

## Setup Instructions

Follow these steps to set up and run the project:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Kuldeep1436/AI-Powered_Medical_Diagnosis
   ```

2. **Navigate to the project folder**:
   ```bash
   cd AI-Medical-Diagnosis
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit application**: To start the application, run the following command:
   ```bash
   streamlit run app.py
   ```

5. **Access the application**: Once the app is running, open your browser and go to:
   ```
   http://localhost:8501
   ```

Here, users can input necessary health details and get disease predictions for Diabetes, Heart Disease, Parkinson's Disease, Lung Cancer, and Hypothyroidism.

## Model Details

### 1. Diabetes Prediction Model
This model predicts whether a person is diabetic based on features such as the number of pregnancies, glucose level, blood pressure, skin thickness, insulin level, BMI, age, and diabetes pedigree function.

### 2. Heart Disease Prediction Model
The heart disease prediction model uses various factors like age, sex, chest pain type, serum cholesterol level, resting blood pressure, fasting blood sugar, maximum heart rate, and more to predict the likelihood of heart disease.

### 3. Parkinson's Disease Prediction Model
This model predicts whether an individual has Parkinson's disease based on voice-related features like MDVP (mean voice perturbation), shimmer, jitter, and other voice characteristics.

### 4. Lung Cancer Prediction Model
This model predicts the likelihood of lung cancer based on factors like smoking status, chest pain, shortness of breath, fatigue, anxiety, age, and other risk factors.

### 5. Hypothyroidism (Thyroid Disease) Prediction Model
The thyroid disease model predicts whether a person has hypothyroidism using features like age, sex, TSH levels, T3 levels, TT4 levels, and more.

All these models have been trained using well-curated datasets, saved, and are being loaded via pickle in the app for inference.

## Screenshots

1. **Diabetes Prediction**  
   This screenshot shows the input fields for diabetes prediction, where users can input parameters such as glucose level, BMI, blood pressure, etc.
   
2. **Heart Disease Prediction**  
   This screenshot shows the input fields for heart disease prediction. The user can input parameters such as age, chest pain type, cholesterol level, and others.

3. **Parkinson's Disease Prediction**  
   This screenshot shows the input fields for Parkinson's disease prediction, where the user enters voice-related features like MDVP, jitter, shimmer, and more.

4. **Lung Cancer Prediction**  
   This screenshot shows the input fields for lung cancer prediction, where users can provide information like smoking status, chest pain, shortness of breath, and others.

5. **Hypothyroidism Prediction**  
   This screenshot shows the input fields for hypothyroidism prediction, where the user enters age, sex, TSH levels, T3 levels, etc.

**Note**: All screenshots are stored in the `Screenshots` folder.

## GitHub Repository

You can find the complete source code for this project in this GitHub repository:

[AI-Medical-Diagnosis Repository](https://github.com/Kuldeep1436/AI-Powered_Medical_Diagnosis)

## Future Work

- **Additional Disease Models**: Add more models for other diseases such as cancer, stroke, kidney disease, etc.
- **Improved Accuracy**: Train the models with larger and more diverse datasets to improve prediction accuracy.
- **User Authentication**: Implement user authentication to provide personalized disease predictions.
- **Data Visualization**: Add visualizations to represent prediction results and show important health metrics graphically.
- **Deployment**: Deploy the app to cloud platforms such as Heroku or AWS for broader access.

