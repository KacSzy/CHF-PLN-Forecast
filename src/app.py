import streamlit as st
import datetime
import plotly.graph_objects as go

from future_func import predict_future_chf

st.title("CHF/PLN Exchange Rate Forecaster")

col1, col2, col3 = st.columns(3)
with col1:
    current_day = datetime.datetime.now().day
    day = st.number_input("Day", min_value=1, max_value=31, value=current_day)
with col2:
    current_month = datetime.datetime.now().month
    month = st.number_input("Month", min_value=1, max_value=12, value=current_month)
with col3:
    current_year = datetime.datetime.now().year
    year = st.number_input("Year", min_value=current_year, max_value=current_year + 10, value=current_year)

if st.button("Predict Exchange Rate"):

    last_known_value = 4.53065

    try:
        with st.spinner("Calculating prediction..."):
            prediction = predict_future_chf(day=day, month=month, year=year)

        if isinstance(prediction, str):
            st.warning(prediction)
        else:
            st.success(f"Predicted CHF/PLN rate: {prediction:.4f}")

            fig = go.Figure()
            fig.add_trace(go.Indicator(
                mode="number+delta",
                value=prediction,
                delta={'reference': last_known_value, 'relative': True},
                title={"text": "Predicted Rate"},
                domain={'x': [0, 1], 'y': [0, 1]}))

            st.plotly_chart(fig)

    except Exception as e:
        st.error(f"An error occurred. Please check your inputs and try again.\n \n{str(e)}")
