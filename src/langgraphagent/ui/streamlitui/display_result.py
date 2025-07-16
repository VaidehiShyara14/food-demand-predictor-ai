import streamlit as st

def show_result(response: str):
    st.success("Prediction Complete")
    st.markdown(response)
