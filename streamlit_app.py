import pandas as pd
import streamlit as st

st.set_page_config(page_title="DS Example", page_icon="🎈")


@st.cache_data
def load_data():
    df = pd.read_csv("sleep_stree_readiness.csv")
    return df


df = load_data()


st.title("🎈 A Data Science Demo Project using Streamlit")
st.title("This is a sample project using human data")

st.write(
    "This is the demo for an interactive website. This is a sample project on human data showcasing the features readiness, stress and overall scores defined by FitBit. Enjoy."
)



###### Section 1 single line plot
st.subheader("Linegraph of single feature over entire timespan")
st.write("The following interactive linegraph visualizes the selected features over the entire timespan of the dataset")

options = {"Deep Sleep in Minutes": 'deep_sleep_in_minutes', 
           "Overall Score": 'overall_score',
           "Readiness Score": 
           'readiness_score_value'}



plot_feature = st.pills("Selected Features", list(options.keys()),selection_mode="single", default="Deep Sleep in Minutes")
st.markdown(f"The plot now shows: {plot_feature}.")
st.line_chart(data=df, y=options[plot_feature], x="Date")


###### Section 2 all features over entire timespan
st.subheader("Linegraph of all features over entire timespan")
st.markdown(df.columns)
st.line_chart(data=df, y=df[value for value in list(options.values())], x="Date")
