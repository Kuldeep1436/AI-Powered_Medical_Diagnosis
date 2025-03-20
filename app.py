import streamlit as st
import pickle
from streamlit_option_menu import option_menu
import time

# Change Name & Logo
st.set_page_config(page_title="Disease Prediction", page_icon="⚕️", layout="wide")

# Hiding Streamlit add-ons
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Adding Background Image
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
        html, body, [class*="css"] {
            font-family: 'Poppins', sans-serif;
        }
        .stApp {
            background: linear-gradient(to right, #2c3e50, #3498db);
            color: white;
        }
        .title {
            font-size: 28px;
            font-weight: bold;
            text-align: center;
            margin-bottom: 20px;
            color: #fff;
        }
        .btn-primary {
            background: #27ae60;
            color: white;
            padding: 12px;
            border-radius: 8px;
            border: none;
            font-size: 16px;
            width: 100%;
        }
        .btn-primary:hover {
            background: #2ecc71;
        }
        .sidebar .css-1d391kg {
            background: #34495e;
        }
    </style>
""", unsafe_allow_html=True)

# Load the saved models
models = {
 'diabetes': pickle.load(open('Models/diabetes_model.sav', 'rb')),
    'heart_disease': pickle.load(open('Models/heart_disease_model.sav', 'rb')),
    'parkinsons': pickle.load(open('Models/parkinsons_model.sav', 'rb')),
    'lung_cancer': pickle.load(open('Models/lungs_disease_model.sav', 'rb')),
    'thyroid': pickle.load(open('Models/Thyroid_model.sav', 'rb'))
}

# ---- Sidebar Navigation ----
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3774/3774299.png", width=100)  # Add a logo
    st.title("Disease Prediction")
    selected = option_menu(
        "Select Disease",
        ["Diabetes", "Heart Disease", "Parkinson's", "Lung Cancer", "Hypo-Thyroid"],
        icons=['activity', 'heart', 'brain', 'lungs', 'thermometer'],
        menu_icon="stethoscope",
        default_index=0
    )

# ---- Function for Input Fields ----
def display_input(label, key, tooltip="", type="text"):
    return st.number_input(label, key=key, help=tooltip, step=1) if type == "text" else st.text_input(label, key=key, help=tooltip)

# Diabetes Prediction Page
if selected == "Diabetes":
    st.markdown('<p class="title">Diabetes Prediction</p>', unsafe_allow_html=True)
    
    with st.expander("🔹 Enter Patient Details"):
        col1, col2 = st.columns(2)
        with col1:
            Pregnancies = display_input('Number of Pregnancies', 'Pregnancies')
            Glucose = display_input('Glucose Level', 'Glucose')
            BloodPressure =  display_input('Blood Pressure value', 'BloodPressure')
            SkinThickness = display_input('Skin Thickness value', 'SkinThickness')
        with col2:
            Insulin = display_input('Insulin Level', 'Insulin')
            BMI = display_input('BMI value', 'BMI')
            DiabetesPedigreeFunction = display_input('Diabetes Pedigree Function value', 'DiabetesPedigreeFunction')
            Age = display_input('Age of the Person', 'Age')

    if st.button("🔍 Predict Diabetes", key="diabetes", help="Click to predict diabetes"):
        with st.spinner("Analyzing... Please wait ⏳"):
            time.sleep(2)  # Simulate processing time
            prediction = models['diabetes'].predict([[Pregnancies, Glucose, BloodPressure,SkinThickness,Insulin, BMI,DiabetesPedigreeFunction, Age]])
            result = "✅ Not Diabetic" if prediction[0] == 0 else "⚠️ Diabetic"
            st.success(f"The person is: *{result}*")

# Heart Disease Prediction Page


if selected == "Heart Disease":
    st.markdown('<p class="title">Heart Disease Prediction</p>', unsafe_allow_html=True)

    with st.expander("🔹 Enter Patient Details"):
         col1, col2 = st.columns(2)
         with col1:
             age = display_input('Age', 'age')
             cp = display_input('Chest Pain types (0, 1, 2, 3)', 'cp')
             chol = display_input('Serum Cholesterol in mg/dl', 'chol')
             restecg = display_input('Resting Electrocardiographic results (0, 1, 2)',  'restecg')
             exang = display_input('Exercise Induced Angina (1 = yes; 0 = no)', 'exang')
             slope = display_input('Slope of the peak exercise ST segment (0, 1, 2)', 'slope')
             thal = display_input('Thal (0 = normal; 1 = fixed defect; 2 = reversible defect)', 'thal')
         with col2:
             sex = display_input('Sex (1 = male; 0 = female)', 'sex')
             trestbps = display_input('Resting Blood Pressure', 'trestbps')
             fbs = display_input('Fasting Blood Sugar > 120 mg/dl (1 = true; 0 = false)', 'fbs')
             thalach = display_input('Maximum Heart Rate achieved', 'thalach')
             oldpeak = display_input('ST depression induced by exercise',  'oldpeak')
             ca = display_input('Major vessels colored by fluoroscopy (0-3)', 'ca')

    if st.button("🔍 Predict Heart Disease", key="heart"):
        with st.spinner("Analyzing... Please wait ⏳"):
            time.sleep(2)
            prediction = models['heart_disease'].predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
            result = "✅ No Heart Disease" if prediction[0] == 0 else "⚠️ Has Heart Disease"
            st.success(f"The person: *{result}*")


# Parkinson's Prediction Page

if selected == "Parkinson's":
    st.markdown('<p class="title">Parkinson\'s Disease Prediction</p>', unsafe_allow_html=True)

    with st.expander("🔹 Enter Patient Details"):
        col1, col2 = st.columns(2)
        with col1:
            fo = display_input('MDVP:Fo(Hz)', 'fo')
            flo = display_input('MDVP:Flo(Hz)',  'flo')
            Jitter_Abs = display_input('MDVP:Jitter(Abs)',  'Jitter_Abs')
            PPQ =  display_input('MDVP:PPQ',  'PPQ')
            Shimmer = display_input('MDVP:Shimmer', 'Shimmer')
            APQ3 = display_input('Shimmer:APQ3', 'APQ3')
            APQ = display_input('MDVP:APQ', 'APQ')
            NHR = display_input('NHR',  'NHR')
            RPDE = display_input('RPDE',  'RPDE')
            spread1 = display_input('Spread1', 'spread1')
            D2 = display_input('D2',  'D2')

        with col2:
            fhi = display_input('MDVP:Fhi(Hz)', 'fhi')
            Jitter_percent = display_input('MDVP:Jitter(%)',  'Jitter_percent')
            RAP = display_input('MDVP:RAP',  'RAP')
            DDP = display_input('Jitter:DDP',  'DDP')
            Shimmer_dB = display_input('MDVP:Shimmer(dB)', 'Shimmer_dB')
            APQ5 = display_input('Shimmer:APQ5',  'APQ5')
            DDA = display_input('Shimmer:DDA', 'DDA')
            HNR = display_input('HNR',  'HNR')
            DFA = display_input('DFA',  'DFA')
            spread2 = display_input('Spread2', 'spread2')
            PPE = display_input('PPE',  'PPE')

    if st.button("🔍 Predict Parkinson's", key="parkinsons"):
        with st.spinner("Analyzing... Please wait ⏳"):
            time.sleep(2)
            prediction = models['parkinsons'].predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])
            result = "✅ No Parkinson's" if prediction[0] == 0 else "⚠️ Has Parkinson's"
            st.success(f"The person: *{result}*")

# Lung Cancer Prediction Page

if selected == "Lung Cancer":
    st.markdown('<p class="title">Lung Cancer Prediction</p>', unsafe_allow_html=True)

    with st.expander("🔹 Enter Patient Details"):
          col1, col2 = st.columns(2)
          with col1:
            GENDER = display_input('Gender (1 = Male; 0 = Female)', 'GENDER')
            SMOKING = display_input('Smoking (1 = Yes; 0 = No)',  'SMOKING')
            ANXIETY = display_input('Anxiety (1 = Yes; 0 = No)', 'ANXIETY')
            CHRONIC_DISEASE = display_input('Chronic Disease (1 = Yes; 0 = No)', 'CHRONIC_DISEASE')
            ALLERGY = display_input('Allergy (1 = Yes; 0 = No)', 'ALLERGY')
            ALCOHOL_CONSUMING = display_input('Alcohol Consuming (1 = Yes; 0 = No)',  'ALCOHOL_CONSUMING')
            SHORTNESS_OF_BREATH = display_input('Shortness Of Breath (1 = Yes; 0 = No)',  'SHORTNESS_OF_BREATH')
            CHEST_PAIN = display_input('Chest Pain (1 = Yes; 0 = No)', 'CHEST_PAIN')

          with col2:
            AGE = display_input('Age',  'AGE')
            YELLOW_FINGERS = display_input('Yellow Fingers (1 = Yes; 0 = No)', 'YELLOW_FINGERS')
            PEER_PRESSURE = display_input('Peer Pressure (1 = Yes; 0 = No)',  'PEER_PRESSURE')
            FATIGUE = display_input('Fatigue (1 = Yes; 0 = No)',  'FATIGUE')
            WHEEZING = display_input('Wheezing (1 = Yes; 0 = No)', 'WHEEZING')
            COUGHING = display_input('Coughing (1 = Yes; 0 = No)', 'COUGHING')
            SWALLOWING_DIFFICULTY = display_input('Swallowing Difficulty (1 = Yes; 0 = No)', 'SWALLOWING_DIFFICULTY')
   
    if st.button("🔍 Predict Lung Cancer", key="lung_cancer"):
        with st.spinner("Analyzing... Please wait ⏳"):
            time.sleep(2)
            prediction = models['lung_cancer'].predict([[GENDER, AGE, SMOKING, YELLOW_FINGERS, ANXIETY, PEER_PRESSURE, CHRONIC_DISEASE, FATIGUE, ALLERGY, WHEEZING, ALCOHOL_CONSUMING, COUGHING, SHORTNESS_OF_BREATH, SWALLOWING_DIFFICULTY, CHEST_PAIN]])
            result = "✅ No Lung Cancer" if prediction[0] == 0 else "⚠️ Has Lung Cancer"
            st.success(f"The person: *{result}*")

# Hypo-Thyroid Prediction Page
if selected == "Hypo-Thyroid":
    st.markdown('<p class="title">Hypo-Thyroid Prediction</p>', unsafe_allow_html=True)

    with st.expander("🔹 Enter Patient Details"):
        col1, col2 = st.columns(2)
        with col1:
            age = display_input('Age',  'age')
            on_thyroxine = display_input('On Thyroxine (1 = Yes; 0 = No)', 'on_thyroxine')
            t3_measured = display_input('T3 Measured (1 = Yes; 0 = No)',  't3_measured')
            tt4 = display_input('TT4 Level', 'tt4')
        with col2:
            sex = display_input('Sex (1 = Male; 0 = Female)', 'sex')
            tsh = display_input('TSH Level', 'tsh')
            t3 = display_input('T3 Level', 't3')
   
    if st.button("🔍 Predict Hypo-Thyroid", key="thyroid"):
        with st.spinner("Analyzing... Please wait ⏳"):
            time.sleep(2)
            prediction = models['thyroid'].predict([[age, sex, on_thyroxine, tsh, t3_measured, t3, tt4]])
            result = "✅ No Hypo-Thyroid" if prediction[0] == 0 else "⚠️ Has Hypo-Thyroid"
            st.success(f"The person: *{result}*")
