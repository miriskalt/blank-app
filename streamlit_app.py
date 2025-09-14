import pandas as pd
import streamlit as st

st.set_page_config(page_title="DS Example", page_icon="🎈")


@st.cache_data
def load_data():
    df = pd.DataFrame([1,2,3,4])
    # df = pd.read_csv("data/movies_genres_summary.csv")
    return df


df = load_data()


st.title("🎈 A Data Science Demo Project using Streamlit")
st.title("This is a sample project using human data")

st.write(
    "This is the demo for an interactive website. This is a sample project on human data showcasing the features readiness, stress and overall scores defined by FitBit. Enjoy."
)

st.subheader("Linegraph of single feature over entire timespan")
st.write("The following interactive linegraph visualizes the selected features over the entire timespan of the dataset")

st.pills("")

