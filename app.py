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


if (click):
    st.write(model.predict())