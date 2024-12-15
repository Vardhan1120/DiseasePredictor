import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

# Load models
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))
breastcancer_model = pickle.load(open('brest_model.sav', 'rb'))

# Sidebar menu
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Home',
                            'Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction',
                            'Breast Cancer Prediction'],
                           menu_icon='hospital-fill',
                           icons=['house', 'activity', 'heart', 'person', 'activity'],
                           default_index=0)

# Homepage
if selected == 'Home':
    st.title("🏥 Multiple Disease Prediction System")
    
    st.markdown("""
    ## Welcome to the Advanced Health Prediction Platform
    
    This intelligent application leverages machine learning to provide preliminary health screenings for multiple critical conditions. 
    Our system uses sophisticated predictive models to assess potential health risks based on input medical parameters.
    
    ### Available Disease Predictions:
    
    1. **Diabetes Prediction**
       - Analyzes various health metrics to assess diabetes risk
       - Includes parameters like glucose levels, BMI, age, and more
    
    2. **Heart Disease Prediction**
       - Evaluates cardiovascular health indicators
       - Considers factors such as blood pressure, cholesterol, and heart rate
    
    3. **Parkinson's Disease Prediction**
       - Uses voice-related medical parameters
       - Employs advanced voice signal processing techniques
    
    4. **Breast Cancer Prediction**
       - Examines multiple tumor characteristics
       - Analyzes cell nucleus features and measurements
    
    ### Important Notes:
    
    🚨 **Disclaimer**: This is a screening tool and NOT a substitute for professional medical advice. 
    Always consult healthcare professionals for accurate diagnosis.
    
    ### How to Use:
    
    1. Select a specific disease prediction from the sidebar menu
    2. Enter the required medical parameters carefully
    3. Click the prediction button to get results
    
    """)
    
    # Optional motivational quote
    st.markdown("""
    > "Prevention is better than cure" - Desiderius Erasmus
    """)

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':

    st.title('Diabetes Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')

    diab_diagnosis = ''

    if st.button('Diabetes Test Result'):
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]
        user_input = [float(x) for x in user_input]
        diab_prediction = diabetes_model.predict([user_input])
        diab_diagnosis = 'The person is diabetic' if diab_prediction[0] == 1 else 'The person is not diabetic'

    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':

    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        Age = st.text_input('Age')

    with col2:
        Sex = st.selectbox('Sex', ('Male', 'Female'))

    with col3:
        CP = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    heart_diagnosis = ''

    if st.button('Heart Disease Test Result'):
        user_input = [Age, Sex, CP, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        user_input = [float(x) if i != 1 else 1.0 if x == 'Male' else 0.0 for i, x in enumerate(user_input)]
        heart_prediction = heart_disease_model.predict([user_input])
        heart_diagnosis = 'The person has heart disease' if heart_prediction[0] == 1 else 'The person does not have heart disease'

    st.success(heart_diagnosis)

# Parkinson's Prediction Page
if selected == 'Parkinsons Prediction':

    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    parkinsons_diagnosis = ''

    if st.button("Parkinson's Test Result"):
        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]
        user_input = [float(x) for x in user_input]
        parkinsons_prediction = parkinsons_model.predict([user_input])
        parkinsons_diagnosis = "The person has Parkinson's disease" if parkinsons_prediction[0] == 1 else "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)
    
# Breast Cancer Prediction Page
if selected == 'Breast Cancer Prediction':
    st.title('Breast Cancer Prediction using ML')
    # Input features
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        mean_radius = st.text_input('Mean Radius')

    with col2:
        mean_texture = st.text_input('Mean Texture')

    with col3:
        mean_perimeter = st.text_input('Mean Perimeter')

    with col4:
        mean_area = st.text_input('Mean Area')

    with col5:
        mean_smoothness = st.text_input('Mean Smoothness')

    with col1:
        mean_compactness = st.text_input('Mean Compactness')

    with col2:
        mean_concavity = st.text_input('Mean Concavity')

    with col3:
        mean_concave_points = st.text_input('Mean Concave Points')

    with col4:
        mean_symmetry = st.text_input('Mean Symmetry')

    with col5:
        mean_fractal_dimension = st.text_input('Mean Fractal Dimension')

    with col1:
        radius_se = st.text_input('Radius SE')

    with col2:
        texture_se = st.text_input('Texture SE')

    with col3:
        perimeter_se = st.text_input('Perimeter SE')

    with col4:
        area_se = st.text_input('Area SE')

    with col5:
        smoothness_se = st.text_input('Smoothness SE')

    with col1:
        compactness_se = st.text_input('Compactness SE')

    with col2:
        concavity_se = st.text_input('Concavity SE')

    with col3:
        concave_points_se = st.text_input('Concave Points SE')

    with col4:
        symmetry_se = st.text_input('Symmetry SE')

    with col5:
        fractal_dimension_se = st.text_input('Fractal Dimension SE')

    with col1:
        worst_radius = st.text_input('Worst Radius')

    with col2:
        worst_texture = st.text_input('Worst Texture')

    with col3:
        worst_perimeter = st.text_input('Worst Perimeter')

    with col4:
        worst_area = st.text_input('Worst Area')

    with col5:
        worst_smoothness = st.text_input('Worst Smoothness')

    with col1:
        worst_compactness = st.text_input('Worst Compactness')

    with col2:
        worst_concavity = st.text_input('Worst Concavity')

    with col3:
        worst_concave_points = st.text_input('Worst Concave Points')

    with col4:
        worst_symmetry = st.text_input('Worst Symmetry')

    with col5:
        worst_fractal_dimension = st.text_input('Worst Fractal Dimension')

    # Prediction
    cancer_diagnosis = ''

    if st.button("Breast Cancer Test Result"):
        user_input = [
            mean_radius, mean_texture, mean_perimeter, mean_area, mean_smoothness,
            mean_compactness, mean_concavity, mean_concave_points, mean_symmetry, mean_fractal_dimension,
            radius_se, texture_se, perimeter_se, area_se, smoothness_se,
            compactness_se, concavity_se, concave_points_se, symmetry_se, fractal_dimension_se,
            worst_radius, worst_texture, worst_perimeter, worst_area, worst_smoothness,
            worst_compactness, worst_concavity, worst_concave_points, worst_symmetry, worst_fractal_dimension
        ]
        user_input = [float(x) for x in user_input]
        cancer_prediction = breastcancer_model.predict([user_input])
        cancer_diagnosis = "The person has breast cancer" if cancer_prediction[0] == 1 else "The person does not have breast cancer"

    st.success(cancer_diagnosis)
