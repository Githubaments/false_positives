import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

def false_positives():

    st.header("False Positives")


    st.write("False positives in medical tests are in the news again. False positives in medical tests are not well understood, even by industry professionals. The maths behind it is very simple, it’s just not immediately intuitive. It involves nothing more complex than multiplying and adding numbers. ")
    st.write("With a couple of examples you'll likely be ahead of most medical professionals.")



    st.write("Imagine a scenario, a patient has just tested positive for a rare disease. One in a hundred people have the disease. The test is 95% accurate -it catches the disease 95% of the time. The test occasionally gets false positives. Someone who doesn’t have the disease will test positive 5% of the time . How worried should we be for our patient who just tested postive? Take a second to come up with a number. ")
    st.write("The answer is we’re not very worried. Our patient is far more likely to be a false positive than a true positive. How does this happen? The answer is mainly because the disease is so rare. 99% of the population don’t have the disease. Finding a false positives in the 99% of the population that don't have the disease is more likely than finding the 1% of people who have the disease.")
    st.write("We’ll be using interactive visualisations to explain this. So don’t worry too much about the maths just yet. ")
    st.write("TP stands for True Positive. The test correctly determines the person has the disease.")
    st.write("FP stands for False Postive. It’s an erroneous positive.")
    st.write("The test incorrectly marks someone as having the disease. So in our example about 1 person in 100 will be marked for having the disease. And about 5 people will be falsely marked as having the disease. So out of the 6 people marked as positive, only 1 of the six have the dease. 1 / 6 is 16%. A single positive test implies a 16% chance of actually having the disease. Even though our test is 95% accurate. It’s not a number that we would immediately expect. ")


    example_expander = st.beta_expander('Here’s the full maths:')
    with example_expander:
        st.write("TP: 95% * 1%  = .95    ")
        st.write("FP:  5% * 95% = 4.95")
        st.write("TP / (TP + FP)   ")
        st.write(".95 / ( 4.95 + .95) = 16%")

    st.header("Interactive Example:")
    st.write("This visualisation is set to the numbers in the example but feel free to change some of the numbers to see how they affect the result.")
    ex_pop_rate = st.slider('Population with disease', min_value=1, value=1, max_value=100, format="%i %%", key=0)
    ex_true_rate = st.slider('True Positive Rate', min_value=1, value=95, max_value=100, format="%i %%",  key= 1)
    ex_false_rate = st.slider('False Positive Rate', min_value=0, value=5, max_value=100, format="%i %%",  key=2)

    key = 1
    second_test = False
    cals(ex_pop_rate, ex_true_rate, ex_false_rate,second_test,key)

    st.header("Second Example")
    st.write("This was a question given to 160 gynaecologists")
    st.write("A test for breast cancer is 90% accurate in identifying patients who actually have breast cancer, and has a 9% false positive rate for patients without breast cancer.")
    st.write("The incidence of breast cancer in the population is 1%. What is the probability that a person who tests positive for breast cancer actually has the disease")
    st.write("Again, take a second to come up with an approximate number.")
    st.write("You'll likely do better than the medical professions who were given this question.")
    st.write("It may be easier to think in terms of frequencies. Of a group of 100 women, 1 will have the disease. The test has a 90% chance of finding this.")
    st.write("For each of the 99 women in the group that don't have the disease there is a 9% chance that they'll have a false positive.")
    st.write("The professionals were given four options. How many women who test positive actually have breast cancer? What is the best approximation?")
    st.write("a) 9 in 10")
    st.write("b) 8 in 10")
    st.write("c) 1 in 10")
    st.write("d) 1 in 100")

    my_expander = st.beta_expander('Answer')
    with my_expander:
        st.write("Only 21% of the group of the professionals got the correct answer c) 1 in 10. That's a lower score than if they had guessed randomly.")

    st.header("Second Interactive Example:")
    ex2_pop_rate = st.slider('Population with disease', min_value=1, value=1, max_value=100, format="%i %%", key=3)
    ex2_true_rate = st.slider('True Positive Rate', min_value=1, value=90, max_value=100, format="%i %%",  key= 4)
    ex2_false_rate = st.slider('False Positive Rate', min_value=0, value=9, max_value=100, format="%i %%",  key=5)

    key = 2
    second_test = False
    cals(ex2_pop_rate, ex2_true_rate, ex2_false_rate,second_test,key)

    st.header("Sensitivity and Specificity")
    st.write("Let’s talk about sensitivity and specificity. Sensitivity refers to how good the test is at catching actual positives. Sensitivity refers to how good it is at not producing false positives. "
             "There is a trade-off in these values. For example, a test could mark every result as a positive. That would give a high sensitivity but a low specificity. An airport scanner designed for high sensitivity, "
             "the cost of missing a true positive is high, while the cost of a false positive is low (hence why so many of us go through extra checks in airports). ")
    st.write("On the other hand, false positives in cancer screening have a high cost in terms of unwarranted turmoil and the possibility of unnecessary intervention. This is why care has to be taken in screening an asymptomatic population. ")

    st.subheader("Sensitivity ")
    st.write("Probability of being test positive when disease present.")
    st.write("Sensitivity = TP / (TP + FN)")
    st.write("TP = number of True Positive, FN = number of False Negatives")

    st.subheader("Specificity ")
    st.write("Probability of being test negative when disease absent.")
    st.write("Specificity = TN / (TN + FP)")
    st.write("TN = number of True Negatives, FP = number of False Positives.")

    st.header("Population Testing")
    st.write("Now it’s important to note that these results are in a population-wide test. It assumes testing  random sample of the population that may be asymptomatic. This is applicable to a test like cancer screening. With something like Covid population wide testing is rare. "
             "Slovakia is the only example. In most countries Covid testing is based on risk. While there may be a low population-wide rate of infection, we would expect a higher instance in the group being tested so false positives would be lower than in population-wide testing. ")

    st.header("Second Test Example")

    st.write("In this example we will include a second test. An accurate second postive test increases the probabilty of a true positive.")
    st.write("An accurate second positive test can dramtically increase the probabilty that we're dealing with a false positive.")
    st.write("The conditional probabilty of two false positives is quite low for an accurate test.")

    ex3_pop_rate = st.slider('Population with disease', min_value=1, value=10, max_value=100, format="%i %%",key=6)
    ex3_true_rate = st.slider('True Positive Rate', min_value=1, value=95, max_value=100, format="%i %%",key =7)
    ex3_false_rate = st.slider('False Positive Rate', min_value=0, value=5, max_value=100, format="%i %%",key = 8)

    key = 3
    second_test = True
    cals(ex3_pop_rate, ex3_true_rate, ex3_false_rate,second_test,key)


    st.header("Final Example")


    pop_rate = st.slider('Population with disease', min_value=1, value=40, max_value=100, format="%i %%")
    true_rate = st.slider('True Positive Rate', min_value=1, value=95, max_value=100, format="%i %%")
    false_rate = st.slider('False Positive Rate', min_value=0, value=5, max_value=100, format="%i %%")

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

    d = {'Infected': [TP, FN, TP + FN], 'Uninfected': [FP, TN, FP + TN], 'Total': [TP + FP, FN + TN, TP + FP + FN + TN]}
    df = pd.DataFrame(data=d, index=['Test Positive', 'Test Negative', 'Total'])



    data = df.iloc[0:2, 0:2]
    fig = px.bar(data, labels={'value': 'Percentage of Pop', 'index': ''})



    final_expander = st.beta_expander('Explanation')
    with final_expander:
        st.write("These charts are created to help you further understand how changing each variable affects the probabilities of a positive result being a true positive.")
        st.write("Each of the three variables charted in turn from 1 to 100, while the other two variables are set to the sliders above.")
        st.write(f"i.e. in this first chart, population with disease is plotted from 1 to 100, and True Positive rate is set to {true_rate}% and"
                 f" False Positive Rate is set to {false_rate}%. The probabilties of a positive test being true are then plotted.")

        st.write(f"In the second chart, True Positive Rate is plotted from 1 to 100, and Population with Disease is set to {pop_rate}% and"
                 f" False Positive Rate is set to {false_rate}%. The probabilties of a positive test being true are then plotted.")




    df_chart2 = pd.DataFrame(index=(np.arange(1, 101)))
    df_chart2['Pop with Disease'] = np.arange(1, 101)
    df_chart2['False Positives'] = ((100 - df_chart2['Pop with Disease']) / 100) * false_rate
    df_chart2['Probability that postive test = have disease'] = ((true_rate * df_chart2['Pop with Disease']) / (
                true_rate * df_chart2['Pop with Disease'] + false_rate * (100 - df_chart2['Pop with Disease']))) * 100
    df_chart2['Probability that 2nd postive test = have disease'] = (true_rate * true_rate * df_chart2[
        'Pop with Disease'] / (true_rate * true_rate * df_chart2['Pop with Disease'] + false_rate * false_rate * (
                100 - df_chart2['Pop with Disease']))) * 100

    fig_pop = px.line(df_chart2, title="Population with Disease", labels={'value': ' ', 'index': ''})
    fig_pop.update_xaxes(showspikes=True)
    fig_pop.update_yaxes(showspikes=True)
    st.plotly_chart(fig_pop,use_container_width=True)



    df_chart3 = pd.DataFrame(index=(np.arange(1, 101)))
    df_chart3['True Positive Rate'] = np.arange(1, 101)
    df_chart3['False Positives'] = ((100 - pop_rate) / 100) * false_rate
    df_chart3['Probability that postive test = have disease'] = ((df_chart3['True Positive Rate'] * pop_rate) / (
                (df_chart3['True Positive Rate'] * pop_rate) + (false_rate * (100 - pop_rate)))) * 100
    df_chart3['Probability that 2nd postive test = have disease'] = ((df_chart3['True Positive Rate'] * df_chart3[
        'True Positive Rate'] * pop_rate) / ((df_chart3['True Positive Rate'] * df_chart3[
        'True Positive Rate'] * pop_rate) + ((false_rate * false_rate) * (100 - pop_rate)))) * 100

    fig_tp = px.line(df_chart3, title="True Positive Rate", labels={'value': ' ', 'index': ''})
    fig_tp.update_xaxes(showspikes=True)
    fig_tp.update_yaxes(showspikes=True)
    st.plotly_chart(fig_tp,use_container_width=True)

    df_chart = pd.DataFrame(index=(np.arange(1, 101)))
    df_chart['False Positive Rate'] = np.arange(1, 101)
    df_chart['False Positives'] = ((100 - pop_rate) / 100) * df_chart['False Positive Rate']
    df_chart['Probability that postive test = have disease'] = (a / (
                a + (df_chart['False Positive Rate'] * (100 - pop_rate)))) * 100
    df_chart['Probability that 2nd postive test = have disease'] = (a2 / (
                a2 + ((df_chart['False Positive Rate'] * df_chart['False Positive Rate']) * (100 - pop_rate)))) * 100

    fig_fp = px.line(df_chart, title="False Positive Rate", labels={'value': ' ', 'index': ''})

    fig_fp.update_xaxes(showspikes=True)
    fig_fp.update_yaxes(showspikes=True)
    st.plotly_chart(fig_fp,use_container_width=True )

    st.dataframe(df.round(0))
    st.plotly_chart(fig,use_container_width=True )


    return

def cals(pop_rate,true_rate,false_rate,second_test,key):

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


    if second_test == True:
        st.write(
            "Given a test that is %i%% accurate, in a population wide test, a positive result implies an actual %.0f%% chance of having the disease. "
            "A second positive test implies a %.2f%% chance of having the disease."
            % (true_rate, false_pos * 100, false_pos2 * 100))
    else:
        st.write(
            "Given a test that is %i%% accurate, in a population wide test with a %i%% infection rate, a positive result implies an actual %.0f%% chance of having the disease. "
            % (true_rate,pop_rate, false_pos * 100))


    d = {'Infected': [TP, FN, TP + FN], 'Uninfected': [FP, TN, FP + TN], 'Total': [TP + FP, FN + TN, TP + FP + FN + TN]}
    df = pd.DataFrame(data=d, index=['Test Positive', 'Test Negative', 'Total'])

    st.dataframe(df.round(0))

    if (st.button('Show more decimal places',key=key)):
        st.write(df.style.format("{:.2f}"))

    # if(st.button('Chart')):
    data = df.iloc[0:2, 0:2]
    fig = px.bar(data, labels={'value': 'Percentage of Pop', 'index': ''})
    st.plotly_chart(fig,use_container_width=True)

    if second_test == True
        


    return TP,FP,FN,TN,false_pos,false_pos2




false_positives()
