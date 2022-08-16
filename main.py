import streamlit as st
import pandas as pd
import numpy as np

st.title('Main form')
import streamlit as st

with st.form(key='form1'):
    cusind = st.selectbox('How was the behavior of the customer?',
                              ('very bad', 'bad', 'average',
                               'cooperative', 'very cooperative'))
    cusknow = st.radio("Was customer able properly explain his/her problem?", options=('yes', 'no'))
    probval = st.radio("Was problem/compliant valid?", options=('yes', 'no'))
    st.markdown('Problem details')
    st.markdown("    ")
    probtype = st.radio("Was this a new problem??", options=('no', 'yes', 'maybe'))
    probkey = st.text_input("Give keywords about the problem")
    st.markdown("    ")
    st.markdown("About our predefined approach towards problems")
    apptoprob = st.radio("Was our approach (towards problem) satisfactory to customer?",
                         options=('yes', 'no', 'maybe'))
    st.markdown("    ")
    st.markdown("About our predefined approach towards customer")
    apptocus = st.radio("Was our approach (towards customer) satisfactory to customer?",
                        options=('yes', 'no', 'maybe'))
    feed = st.text_area(
        "Tell anything about this call to the manager/senior NOTE: This can be considered in your monthly evalution")

    submit_button = st.form_submit_button()
d = ({'cusind': cusind, 'cusknow': cusknow, 'probval': probval, 'probtype': probtype, 'probkey': probkey,
      'apptoprob': apptoprob, 'apptocus': apptocus, 'Employees_note': feed})
if submit_button == True:
    df = pd.read_csv("C:\\Users\\Sahaj's PC\\PycharmProjects\\pythonProject4\\data.csv")
    df = df.append(d, ignore_index=True)
    df = df.rename(columns = {' apptocus':'apptocus'})
    st.markdown('<h3>Thank you for your feedback!</h3>', unsafe_allow_html=True)

    # st.write(df)
    # open('data.csv', 'w').write(df.to_csv('data.csv', index=False))

    df.to_csv('data.csv',index=False)
else:
    st.markdown("Click submit to save form responses.")
