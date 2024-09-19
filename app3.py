import streamlit as st
import pandas as pd
import random
import google.generativeai as genai

# Configure the Gemini API key
genai.configure(api_key="AIzaSyCF6KRkaDlUAhziufh6-qfpWEQd0uptb0M")


# Function to simulate AI predictions using Gemini's API
def ai_predict(query):
    model = genai.GenerativeModel('gemini-1.0-pro-latest')
    response = model.generate_content(query)
    return response.text


# Sample data generation for M-Sand related features
def generate_sample_data():
    data = {
        "Material Stage": ["Foundation", "Pillars", "Roof", "Finishing"],
        "M-Sand Quantity (tons)": [random.randint(50, 100) for _ in range(4)],
        "Delays (days)": [random.randint(1, 10) for _ in range(4)],
        "Budget Overrun (%)": [random.uniform(0.05, 0.15) for _ in range(4)]
    }
    return pd.DataFrame(data)


# Streamlit App UI
st.title("M-Sand Construction Management Platform")

# Sidebar for feature selection
st.sidebar.title("AI Features")
selected_feature = st.sidebar.selectbox(
    "Choose a feature:",
    ("Predictive Analytics", "AI-Powered Resource Allocation",
     "M-Sand Mix Optimization", "AI-Based Cost Forecasting")
)

st.sidebar.subheader("Sample Data")
sample_data = generate_sample_data()
st.sidebar.write(sample_data)

# Predictive Analytics
if selected_feature == "Predictive Analytics":
    st.header("Predictive Analytics")
    st.subheader("Forecast Material Requirements, Delays, and Budget Overruns")

    # User input for material stage to predict
    material_stage = st.selectbox("Choose Material Stage", ["Foundation", "Pillars", "Roof", "Finishing"])
    project_size = st.slider("Select Project Size (units)", 10, 500, 100)
    delay_risk = st.selectbox("Choose Delay Risk", ["Low", "Medium", "High"])

    if st.button("Predict"):
        query = f"Predict material requirements, delays, and budget overruns for a {project_size}-unit project in the {material_stage} stage with {delay_risk} risk."
        result = ai_predict(query)
        st.subheader("AI Prediction")
        st.write(result)

    st.write("Sample Data Overview:")
    st.write(sample_data)

# AI-Powered Resource Allocation
elif selected_feature == "AI-Powered Resource Allocation":
    st.header("AI-Powered Resource Allocation")
    st.subheader("Optimize Allocation of Resources Based on AI")

    # Input parameters for resource allocation
    project_type = st.selectbox("Choose Project Type", ["Residential", "Commercial", "Industrial"])
    labor_availability = st.slider("Labor Availability (percentage)", 0, 100, 75)
    equipment_status = st.selectbox("Equipment Availability", ["Available", "Limited", "Unavailable"])

    if st.button("Optimize Resources"):
        query = f"Optimize resource allocation for a {project_type} project with {labor_availability}% labor availability and {equipment_status} equipment status."
        result = ai_predict(query)
        st.subheader("AI Recommendation")
        st.write(result)

# AI-Powered M-Sand Mix Optimization
elif selected_feature == "M-Sand Mix Optimization":
    st.header("AI-Powered M-Sand Mix Optimization")
    st.subheader("Get Real-Time M-Sand Mix Ratio Recommendations")

    # Input parameters for M-Sand mix optimization
    environment_type = st.selectbox("Choose Environment Type", ["Coastal", "Urban", "Rural"])
    project_height = st.slider("Building Height (floors)", 1, 100, 20)
    material_quality = st.selectbox("M-Sand Quality", ["High", "Medium", "Low"])

    if st.button("Get Mix Recommendations"):
        query = f"Recommend the best M-Sand mix ratio for a {project_height}-floor building in a {environment_type} environment with {material_quality} M-Sand quality."
        result = ai_predict(query)
        st.subheader("AI Recommendation")
        st.write(result)

# AI-Based Cost Forecasting
elif selected_feature == "AI-Based Cost Forecasting":
    st.header("AI-Based Cost Forecasting")
    st.subheader("Accurate Cost Forecasts Using Historical Data")

    # Input parameters for cost forecasting
    budget = st.number_input("Enter Current Budget (in lakhs)", min_value=50, max_value=10000, value=100)
    project_duration = st.slider("Select Project Duration (months)", 1, 60, 24)
    risk_factor = st.selectbox("Risk Factor", ["Low", "Moderate", "High"])

    if st.button("Forecast Costs"):
        query = f"Forecast the project cost for a project with a budget of {budget} lakhs, duration of {project_duration} months, and {risk_factor} risk factor."
        result = ai_predict(query)
        st.subheader("AI Forecast")
        st.write(result)

# Footer
st.sidebar.title("Project Overview")
st.sidebar.write("""
This platform provides AI-powered tools to improve M-Sand construction workflows. 
Use the features on the left to explore how AI can optimize resources, forecast costs, 
recommend M-Sand mixes, and predict delays and budget overruns.
""")
