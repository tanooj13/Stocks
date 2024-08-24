import pickle
import streamlit  as st




option = st.selectbox(
    "Enter company:",
    ("google", "apple", "microsoft"),
    index=None,
    
)

click = st.button("predict", type="primary")


with open('model.pkl','rb') as f:
    model = pickle.load(f)

X = [[ 230,  230, 230 ,165428800  , 0.    ,      0. , 240 , 220 , 1.        ]]
if (click):
    st.write("Model Predicted:")
    st.write(model.predict(X))
else:st.write("Select a company")
