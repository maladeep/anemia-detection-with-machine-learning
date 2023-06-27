import streamlit as st
import pandas as pd
import sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score, accuracy_score, classification_report # for computing various performance metrics for classification models
import pickle

# Load the trained model
model_path = 'random_forest_model.pkl'  # Path to your trained model
model = pickle.load(open(model_path, 'rb'))

# Define the function to preprocess input data
def preprocess_data(hemoglobin, gender, mcv):
    # Convert gender to numeric value
    gender_mapping = {'Male': 0, 'Female': 1}
    gender = gender_mapping.get(gender, 0)  # Default to 0 if gender is not found

    # Ensure non-negative values for hemoglobin and MCV
    hemoglobin = max(hemoglobin, 0)
    mcv = max(mcv, 0)

    # Create a dataframe with the input data
    data = {'Gender': [gender], 'Hemoglobin': [hemoglobin], 'MCV': [mcv]}
    df = pd.DataFrame(data)

    return df

# Define the function to predict anemia
def predict_anemia(hemoglobin, gender, mcv):
    # Preprocess the input data
    df = preprocess_data(hemoglobin, gender, mcv)

    # Predict anemia using the trained model
    prediction = model.predict(df)

    # Return the prediction
    return prediction[0]

# Create the Streamlit app
def main():
    # Set the title and description
    
    st.subheader("Predict and Classify Anemia Based on Input Data")
    st.write("Anemia is a medical condition characterized by a deficiency of healthy red blood cells in the body or a reduction in the amount of hemoglobin in the blood. Hemoglobin is the protein in red blood cells responsible for carrying oxygen throughout the body. Anemia can occur due to various reasons such as a lack of iron or other essential nutrients, chronic diseases, genetic conditions, blood loss, or a malfunction in the bone marrow.")
    st.write("Symptoms of anemia include fatigue, weakness, shortness of breath, dizziness, pale skin, irregular heartbeat, and headaches. Treatment for anemia depends on the underlying cause, but it may involve dietary changes, supplements, medication, or, in severe cases, blood transfusions.")

    st.write("It is important to identify and treat anemia promptly, as it can lead to complications such as heart problems, impaired cognitive function, and delayed growth and development in children.")
    
    # Display average range table
    st.write("**Average Range of Hemoglobin and MCV (in units):**")
    average_range = {'Gender': ['Male', 'Female'],
                     'Hemoglobin': ['12.0 - 15.0 g/dL', '11.5 - 14.5 g/dL'],
                     'MCV': ['80.0 - 95.0 fL', '82.0 - 98.0 fL']}
    df_range = pd.DataFrame(average_range)
    st.table(df_range)

    # Add a divider
    st.markdown("<hr>", unsafe_allow_html=True)

    # Create input fields for user input
    st.markdown("**Enter the required informationv**")
    gender = st.radio("Select Gender", ['Male', 'Female'], index=0)
    hemoglobin = st.number_input("Enter Hemoglobin (g/dL)", value=12.0, min_value=0.0, step=0.1)
    
    mcv = st.number_input("Enter MCV (fL)", value=90.0, min_value=0.0, step=0.1)





    # Check if the user has entered valid values
    if st.button("Detect"):
        if hemoglobin >= 0 and mcv >= 0:
            # Call the predict_anemia function to get the prediction
            prediction = predict_anemia(hemoglobin, gender, mcv)

            # Map the prediction to the corresponding label
            prediction_label = 'Anemic' if prediction == 1 else 'Non Anemic'

            # Display the prediction
            st.write("The person is likely to be", prediction_label)

            # Check for microcytic anemia
            if mcv < 80.0:
                st.write("Type is likely to be microcytic anemia")

            # Check for macrocytic anemia
            if mcv > 100.0:
                st.write("Type is likely to be macrocytic anemia")
                st.write("Plese consult your Doctor is likely to be macrocytic anemia")
        else:
            st.warning("Please enter valid values.")

    st.info("Please note that the predictions provided by this app are based on machine learning algorithms and should be used for informational purposes only. It is important to consult with a qualified healthcare professional or doctor for accurate diagnosis and medical advice regarding anemia or any other health condition.")       

    # Add a divider
    st.markdown("<hr>", unsafe_allow_html=True)


    if st.button("How this was prepared?"):

        st.write("The dataset consists of 1421 samples with six attributes: gender, hemoglobin, mean corpuscular hemoglobin (MCH), mean corpuscular hemoglobin concentration (MCHC), mean corpuscular volume (MCV), and result .")
        st.write("On conducting six different supervised learning algorithms, Random Forest was found to outperform the others. Hence, this app is built using Random Forest for anemia prediction.")
        st.markdown("<p style='text-align: left;'> Get complete code at <a href='https://github.com/maladeep/palmerpenguins-streamlit-eda'>GitHub Repo </a>  </p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'> Brought to you with ❤ by <a href='https://github.com/maladeep'>Mala Deep</a>  </p>", unsafe_allow_html=True)
        


# Run the app
if __name__ == '__main__':
    main()



# import streamlit as st
# import pandas as pd
# import pickle

# # Load the trained model
# model_path = 'random_forest_model.pkl'  # Path to your trained model
# model = pickle.load(open(model_path, 'rb'))

# # Define the function to preprocess input data
# def preprocess_data(hemoglobin, gender, mcv):
#     # Convert gender to numeric value
#     gender_mapping = {'Male': 0, 'Female': 1}
#     gender = gender_mapping.get(gender, 0)  # Default to 0 if gender is not found

#     # Create a dataframe with the input data
#     data = {'Gender': [gender], 'Hemoglobin': [hemoglobin], 'MCV': [mcv]}
#     df = pd.DataFrame(data)

#     return df

# # Define the function to predict anemia
# def predict_anemia(hemoglobin, gender, mcv):
#     # Preprocess the input data
#     df = preprocess_data(hemoglobin, gender, mcv)

#     # Predict anemia using the trained model
#     prediction = model.predict(df)

#     # Return the prediction
#     return prediction[0]

# # Create the Streamlit app
# def main():
#     # Set the title and description
#     st.title("Anemia Detection")
#     st.write("This app helps detect anemia based on input values of hemoglobin, gender, and MCV.")
#     # Add a divider
#     st.markdown("<hr>", unsafe_allow_html=True)
#     st.write("The dataset consists of 1421 samples with six attributes: gender, hemoglobin, mean corpuscular hemoglobin (MCH), mean corpuscular hemoglobin concentration (MCHC), mean corpuscular volume (MCV), and result.")
#     st.write("On conducting six different supervised learning algorithms, Random Forest was found to outperform the others. Hence, this app is built using Random Forest for anemia prediction.")

    
#     # Display average range table
#     st.write("Average Range of Hemoglobin and MCV (in units):")
#     average_range = {'Gender': ['Male', 'Female'],
#                      'Hemoglobin': ['12.0 - 15.0 g/dL', '11.5 - 14.5 g/dL'],
#                      'MCV': ['80.0 - 95.0 fL', '82.0 - 98.0 fL']}
#     df_range = pd.DataFrame(average_range)
#     st.table(df_range)

#     # Create input fields for user input
#     st.header("Enter the required information:")
#     hemoglobin = st.number_input("Hemoglobin (g/dL)", value=12.0, min_value=0.0, step=0.1)
#     gender = st.selectbox("Gender", ['Male', 'Female'], index=0)
#     mcv = st.number_input("MCV (fL)", value=90.0,min_value=0.0, step=0.1)


#     # Check if the user has entered valid values
#     if st.button("Detect"):
#         if hemoglobin and gender and mcv:
#             # Call the predict_anemia function to get the prediction
#             prediction = predict_anemia(hemoglobin, gender, mcv)

#             # Map the prediction to the corresponding label
#             prediction_label = 'Anemic' if prediction == 1 else 'Non Anemic'

#             # Display the prediction
#             st.write("The person is likely to be", prediction_label)
#         else:
#             st.warning("Please enter valid values.")
      

# # Run the app
# if __name__ == '__main__':
#     main()
