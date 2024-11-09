import numpy as np
import streamlit as st
import pickle


# load the saved model
loaded_model=pickle.load(open('C:/Users/HP/OneDrive/Documents/ML Deployment/trained_model.sav','rb'))

# create a function for prediction

def diabetes_prediction(input_data):
    input_data_as_array=np.asarray(input_data)
    # Now reshape the input data as a numpy array, because we are dealing with one instances of our dataset
    reshaped_input_data_as_array=input_data_as_array.reshape(1,-1) 
    prediction=loaded_model.predict(reshaped_input_data_as_array)
    print(prediction)
    if (prediction==0):
        return ('the patient is not Diabetic')
    else:
        return ('the patient is Diabetic')
        

def main():
    # Now here, the streamlit is used to make app and user interfaces 
    # use streamlit to give title to our web page
    st.title('Diabetes Prediction Web App')
    # Now get input from user
    #Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age
    
    # Arrange the inputs sequence in a systematic order for better view
    col1,col2,col3=st.columns(3)
    
    with col1:
        Pregnancies=st.text_input('Number of Pregnancies')
    
    with col2:
        Glucose_Level=st.text_input('Glucose Level')
    
    with col3:
        Blood_Pressure=st.text_input('Blood Pressure')
    
    with col1:
        Skin_Thickness=st.text_input('Skin Thickness')
    
    with col2:
        Insulin=st.text_input('Insulin')
    
    with col3:
        BMI=st.text_input('BMI')
    
    with col1:
        DiabetesPedigreeFunction=st.text_input('DiabetesPedigreeFunction')
    
    with col2:
        Age=st.text_input('Age')
        
        
    # code for prediction
    diagnosis=''
    
    # create a buttton for prediction
    if st.button('Diabetes Test Result'):
        diagnosis=diabetes_prediction([Pregnancies,Glucose_Level,Blood_Pressure,Skin_Thickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
        
    st.success(diagnosis)
    

if __name__=='__main__':
    main()
        
    
    


     
    
