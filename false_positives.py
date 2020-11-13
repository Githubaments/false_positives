import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

def false_positives():
    pop_rate = st.sidebar.slider('Population with disease', min_value=1, value=40, max_value=100, format="%i %%")
    true_rate = st.sidebar.slider('True Positive Rate', min_value=1, value=100, max_value=100, format="%i %%")
    false_rate = st.sidebar.slider('False Positive Rate', min_value=0, value=5, max_value=100, format="%i %%")

    a = true_rate * pop_rate
    b = false_rate * (100 - pop_rate)
    false_pos = a / (a + b)

    a2 = true_rate * true_rate * pop_rate
    b2 = false_rate * false_rate * (100 - pop_rate)
    false_pos2 = a2 / (a2 + b2)

    TP = (pop_rate * true_rate) / 100
    FP = ((100 - pop_rate) / 100) * false_rate
    FN = ((pop_rate) * (100 - true_rate)) / 100
    TN = (100 - pop_rate) * (100 - false_rate) / 100
    
    
    my_expander = st.beta_expander()
    my_expander.write('Sensitivity vs specificity')
    clicked = my_expander.button('Click me!')


    st.write(
        "Given a test that is %i%% accurate, in a population wide test a positive result implies an actual %.0f%% chance of having the disease. "
        "A second positive test implies a %.2f%% chance of having the disease."
        % (true_rate, false_pos * 100, false_pos2 * 100))

    d = {'Infected': [TP, FN, TP + FN], 'Uninfected': [FP, TN, FP + TN], 'Total': [TP + FP, FN + TN, TP + FP + FN + TN]}
    df = pd.DataFrame(data=d, index=['Test Positive', 'Test Negative', 'Total'])

    st.dataframe(df.round(0))

    if (st.button('Show more decimal places')):
        st.write(df.style.format("{:.2f}"))

    # if(st.button('Chart')):
    data = df.iloc[0:2, 0:2]
    fig = px.bar(data, labels={'value': 'Percentage of Pop', 'index': ''})
    st.plotly_chart(fig)

    # add_selectbox = st.sidebar.selectbox(
    #     "Pick a variable to compare against the rest",
    #     ("Population with disease", "True Positive Rate", "False Positive Rate"))
    # st.write(add_selectbox)

    df_chart2 = pd.DataFrame(index=(np.arange(1, 101)))
    df_chart2['Pop with Disease'] = np.arange(1, 101)
    df_chart2['False Positives'] = ((100 - df_chart2['Pop with Disease']) / 100) * false_rate
    df_chart2['Probability that postive test = have disease'] = ((true_rate * df_chart2['Pop with Disease']) / (
                true_rate * df_chart2['Pop with Disease'] + false_rate * (100 - df_chart2['Pop with Disease']))) * 100
    df_chart2['Probability that 2nd postive test = have disease'] = (true_rate * true_rate * df_chart2[
        'Pop with Disease'] / (true_rate * true_rate * df_chart2['Pop with Disease'] + false_rate * false_rate * (
                100 - df_chart2['Pop with Disease']))) * 100
    
    st.subheader("Variable Comparision")

    fig3 = px.line(df_chart2, title="Population with Disease", labels={'value': ' ', 'index': ''})
    fig3.update_xaxes(showspikes=True)
    fig3.update_yaxes(showspikes=True)
    st.plotly_chart(fig3)

    df_chart3 = pd.DataFrame(index=(np.arange(1, 101)))
    df_chart3['True Positive Rate'] = np.arange(1, 101)
    df_chart3['False Positives'] = ((100 - pop_rate) / 100) * false_rate
    df_chart3['Probability that postive test = have disease'] = ((df_chart3['True Positive Rate'] * pop_rate) / (
                (df_chart3['True Positive Rate'] * pop_rate) + (false_rate * (100 - pop_rate)))) * 100
    df_chart3['Probability that 2nd postive test = have disease'] = ((df_chart3['True Positive Rate'] * df_chart3[
        'True Positive Rate'] * pop_rate) / ((df_chart3['True Positive Rate'] * df_chart3[
        'True Positive Rate'] * pop_rate) + ((false_rate * false_rate) * (100 - pop_rate)))) * 100

    fig4 = px.line(df_chart3, title="True Positive Rate", labels={'value': ' ', 'index': ''})
    fig4.update_xaxes(showspikes=True)
    fig4.update_yaxes(showspikes=True)
    st.plotly_chart(fig4)

    df_chart = pd.DataFrame(index=(np.arange(1, 101)))
    df_chart['False Positive Rate'] = np.arange(1, 101)
    df_chart['False Positives'] = ((100 - pop_rate) / 100) * df_chart['False Positive Rate']
    df_chart['Probability that postive test = have disease'] = (a / (
                a + (df_chart['False Positive Rate'] * (100 - pop_rate)))) * 100
    df_chart['Probability that 2nd postive test = have disease'] = (a2 / (
                a2 + ((df_chart['False Positive Rate'] * df_chart['False Positive Rate']) * (100 - pop_rate)))) * 100

    fig2 = px.line(df_chart, title="False Positive Rate", labels={'value': ' ', 'index': ''})

    fig2.update_xaxes(showspikes=True)
    fig2.update_yaxes(showspikes=True)
    st.plotly_chart(fig2)

    return

false_positives()
