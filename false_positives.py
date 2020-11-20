import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

def false_positives():

    st.header("False Positives")

    st.write("False positives are in the news again. False positives in medical tests are not well understood, even by industry professionals. The maths behind it is very simple, it’s just not immediately intuitive. It involves nothing more complex than addition and multiplication. ")
    st.write("With a couple of examples you'll likely be ahead of most doctors. We’ll start with a simple general example before taking a look at two topical examples; Covid testing and mammogram screening.")

    st.write("Imagine a scenario: during a population wide screening a patient has just tested positive for a rare disease. One in a hundred people have the disease. The test is 95% accurate - it catches the disease 95% of the time. The test occasionally gets false positives. Someone who doesn’t have the disease will test positive 5% of the time. How worried should we be for our patient? How likely is it that they actually have the disease? Take a second to come up with a approximate number. ")
    st.write("The answer is we’re not very worried. Our patient is far more likely to be a false positive than a true positive. How does this happen? The answer is mainly because the disease is so rare. 99% of the population don’t have the disease. Finding a false positives in the 99% of the population that don't have the disease is more likely than finding the 1% of people who have the disease.")
    st.write("We’ll be using interactive visualisations to explain this. So don’t worry too much about the maths just yet. ")
    st.write("TP stands for True Positive. The test correctly determines the person has the disease.")
    st.write("FP stands for False Postive. It’s an erroneous positive, the test has incorrectly marked someone as having the disease. ")
    st.write("In our example about 1 person in 100 will be marked as a True Positive. And about 5 people will be False Positives. So out of the 6 people marked as positive, only 1 of the 6 have the disease. 1 / 6 is 16%. The test is 95% accurate but a single positive test implies only a 16% chance of actually having the disease. It’s not a number that we would immediately expect. ")

    example_expander = st.beta_expander('Here’s the full maths:')
    with example_expander:
        st.write("TP: 95% * 1%  = .95    ")
        st.write("FP:  5% * 95% = 4.95")
        st.write("TP / (TP + FP)   ")
        st.write(".95 / ( 4.95 + .95) = 16%")

    st.header("Interactive Example:")
    st.write("This visualisation is set to the numbers in the example but feel free to change some of the numbers to see how they affect the result.")
    ex_pop_rate = st.slider('Population with disease', min_value=0.01, value=1.00, max_value=100.00, format="%f %%", key=0)
    ex_true_rate = st.slider('True Positive Rate', min_value=0.01, value=95.00, max_value=100.00, format="%f %%",  key= 1)
    ex_false_rate = st.slider('False Positive Rate', min_value=0.00, value=5.00, max_value=100.00, format="%f %%",  key=2)

    key = 1
    second_test = False
    example = True
    cals(ex_pop_rate, ex_true_rate, ex_false_rate,second_test,key,example)
    example = False



    st.header("Covid Testing")

    st.write("The accuracy of the test is just one part of the equation. The infection rate matters too. Fewer infected people means more opportunities "
             "to have a false positive. Therefore the way the test is organised is an important factor. In cancer screening the population as a whole is "
             "tested. This increases possibility of false positives as most people won’t have the disease.")
    st.write("For Covid, population-wide testing is rare. Testing is concentrated on high-risk categories such as those showing symptoms or were in close contract to other cases. "
             "The population rate currently in Ireland is estimated at 14 cases per 1000 people or 1.4%.")

    st.write("The Positivity Rate is the percentage of tests that are positive. Given that testing is being performed on sections of the population that are at risk, "
             "we would expect the Positivty Rate to be a multiple of the population rate. The Positive Rate in Ireland for the last 7 days is 3.5%. ")
    st.write("For this example we'll use an estimate of the test positivty rate rather than the population rate.")


    st.header("False Positive Rates")


    st.write("There are different estimates of the false positive rate of PCR tests for Covid. "
             "The Chair of Ireland’s COVID-19 Expert Advisory Group, Dr De Gascun estimated that for Ireland’s testing system the True Positve Rate is close to 100% and the highest possible percentage of "
             "false positives is [0.2%](https://www.newstalk.com/news/coronavirus-testing-false-positives-1082333).")
    st.write("[Lancet’s preliminary estimates](https://www.thelancet.com/journals/lanres/article/PIIS2213-2600(20)30453-7/fulltext) for swab tests in the UK are between 0.8% and 4%.")
    st.write("I have no expertise in the area. I'm just giving you a tool to examine these numbers. The selection box below will allow you to examine each of the "
             "different false positive esimates.")

    dict_estimates = {'Lancet Min': 0.8,
                      'Lancet’s Max':4.0,
                      'Irish Estimated Figures': 0.4
                      }

    study = st.selectbox("Estimate:", ['Lancet Min','Lancet’s Max','Irish Estimated Figures'], key=None)

    false_rate = dict_estimates[study]

    ex_pop_rate = st.slider('Estimate of the sample infection rate:', min_value=0.01, value=3.50, max_value=100.00, format="%f %%", key=3)
    ex_true_rate = st.slider('True Positive Rate', min_value=0.01, value=99.00, max_value=100.00, format="%f %%",  key= 4)
    ex_false_rate = st.slider('False Positive Rate', min_value=0.00, value=false_rate, max_value=100.00, format="%f %%",  key=5)

    key = 5
    second_test = False
    cals(ex_pop_rate, ex_true_rate, ex_false_rate,second_test,key,example)

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


    st.header("False-Positive Mammography Screening")
    st.write("At first glance not screening for breast or prostate cancer may seem paradoxical. But in low risk age groups, the risks of false "
             "positives may outweigh the gains of testing. False positives can cause undue mental anguish and unwarrented medical interventions."
             "Mayo Clinic radiologist Dr. Amy Conners stated that 'We know that  5-12 percent of those screened will have a positive result: About 0.5 percent have cancer (which is a true-positive), "
             "while the rest fall into the false-positive category.'")



    ex_pop_rate = st.slider('Sample with disease:', min_value=0.001, value=0.5, max_value=100.0000, format="%f %%", key=6)
    ex_true_rate = st.slider('True Positive Rate', min_value=0.01, value=99.99, max_value=100.0000, format="%f %%",  key= 7)
    ex_false_rate = st.slider('False Positive Rate', min_value=0.0000, value=11.5, max_value=100.0000, format="%f %%",  key=8)

    key = 6
    second_test = False
    cals(ex_pop_rate, ex_true_rate, ex_false_rate,second_test,key,example)

    st.header("A Second Positive Test Example")

    st.write("In this example we will include a second test. An accurate second postive test increases the probabilty of the result being a true positive.")
    st.write("An accurate second positive test can dramatically increase the probabilty that we're dealing with a false positive.")
    st.write("If the two tests are indepndent the conditional probabilty of two false positives is quite low for an accurate test.")

    ex3_pop_rate = st.slider('Population with disease', min_value=1, value=10, max_value=100, format="%i %%",key=7)
    ex3_true_rate = st.slider('True Positive Rate', min_value=1, value=95, max_value=100, format="%i %%",key =8)
    ex3_false_rate = st.slider('False Positive Rate', min_value=0, value=5, max_value=100, format="%i %%",key = 9)

    key = 3
    second_test = True
    cals(ex3_pop_rate, ex3_true_rate, ex3_false_rate,second_test,key,example)


    st.header("Study Example")
    st.write("At this stage you likely have a better understanding than many doctors.  [Gerd Gigerenzer](https://www.bbc.com/news/magazine-28166019) used to give statistics workshops to gynaecologists. At the beginning"
             " he would pose a question. This was a question given to 160 doctors:")
    st.write("A test for breast cancer is 90% accurate in identifying patients who actually have breast cancer, and has a 9% false positive rate for patients without breast cancer.")
    st.write("The incidence of breast cancer in the population is 1%. What is the probability that a person who tests positive for breast cancer actually has the disease?")
    st.write("Again, take a second to come up with an approximate number.")
    st.write("You'll likely do better than the professions who were given this question.")
    st.write("It may be easier to think in terms of frequencies. In a group of 100 women, 1 will have the disease. The test has a 90% chance of finding this.")
    st.write("For each of the 99 women in the group that don't have the disease there is a 9% chance that they'll get a false positive.")
    st.write("The professionals were given four options. How many women who test positive actually have breast cancer? What is the best approximation?")
    st.write("a) 9 in 10")
    st.write("b) 8 in 10")
    st.write("c) 1 in 10")
    st.write("d) 1 in 100")

    my_expander = st.beta_expander('Answer')
    with my_expander:
        st.write("Only 21% of the group of the professionals got the correct answer c) 1 in 10. That's a lower score than if they had guessed randomly.")
    ex2_pop_rate = st.slider('Population with disease', min_value=1, value=1, max_value=100, format="%i %%", key=9)
    ex2_true_rate = st.slider('True Positive Rate', min_value=1, value=90, max_value=100, format="%i %%",  key= 10)
    ex2_false_rate = st.slider('False Positive Rate', min_value=0, value=9, max_value=100, format="%i %%",  key=11)

    key = 2
    second_test = False
    cals(ex2_pop_rate, ex2_true_rate, ex2_false_rate,second_test,key,example)







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

    TP = (pop_rate * true_rate) / 10
    FP = ((100 - pop_rate) / 10) * false_rate
    FN = ((pop_rate) * (100 - true_rate)) / 10
    TN = (100 - pop_rate) * (100 - false_rate) / 10

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
    st.plotly_chart(fig_pop)



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
    st.plotly_chart(fig_tp)

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
    fig_fp.update_yaxes(visible=False)

    st.plotly_chart(fig_fp)

    st.dataframe(df.round(0))
    st.plotly_chart(fig)


    return

def cals(pop_rate,true_rate,false_rate,second_test,key,example):

    a = true_rate * pop_rate
    b = false_rate * (100 - pop_rate)
    false_pos = (a / (a + b) ) * 100

    a2 = true_rate * true_rate * pop_rate
    b2 = false_rate * false_rate * (100 - pop_rate)
    false_pos2 = a2 / (a2 + b2)

    TP = (pop_rate * true_rate) / 10
    FP = ((100 - pop_rate) / 10) * false_rate
    FN = ((pop_rate) * (100 - true_rate)) / 10
    TN = (100 - pop_rate) * (100 - false_rate) / 10

    precision  = get_precision(pop_rate,true_rate,false_rate)

    if second_test == True:
        st.write(
            "Given a test that is %i%% accurate, in a population wide test, a positive result implies an actual %.0f%% chance of having the disease. "
            "A second positive test implies a %.2f%% chance of having the disease."
            % (true_rate, false_pos, false_pos2 * 100))
    else:
        st.write( f"Given a test that is {true_rate:.{precision}f}% accurate, with a {pop_rate:.{precision}f}% infection rate, a positive result implies an actual "
                  f" {false_pos:.{precision}f} % chance of having the disease. ")

    if example == True:
        TP = TP /10
        FP = FP /10
        TN = TN /10
        FN = FN /10

    d = {'Infected': [TP, FN, TP + FN], 'Uninfected': [FP, TN, FP + TN], 'Total': [TP + FP, FN + TN, TP + FP + FN + TN]}
    df = pd.DataFrame(data=d, index=['Test Positive', 'Test Negative', 'Total'])

    st.dataframe(df.round(0))

    if (st.button('Show more decimal places',key=key)):
        st.write(df.style.format("{:.2f}"))

    # if(st.button('Chart')):
    data = df.iloc[0:2, 0:2]
    fig = px.bar(data, labels={'value': 'Percentage of Pop', 'index': ''})
    fig.update_yaxes(visible=False)

    st.plotly_chart(fig)

    return

def get_precision(pop_rate,true_rate,false_rate):

    if (int(pop_rate) + int(true_rate) + int(false_rate)) - (pop_rate + true_rate + false_rate) == 0:
        precision = 0
    else:
        a = len(str(pop_rate).split('.')[1])
        b = len(str(true_rate).split('.')[1])
        c = len(str(false_rate).split('.')[1])
        precision = (min(a,b,c))

    return precision


false_positives()
