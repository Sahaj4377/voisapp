import streamlit as st
import pandas as pd
import numpy as np

st.title('pickups')

with st.form(key='form1'):
    firstname = st.text_input("Firstname")
    lastname = st.text_input("lastname")
    dob = st.date_input("Date of Birth")
    submit_button = st.form_submit_button(label='Signup')
d = ({'firstname': firstname, 'lastname': lastname})
if submit_button == True:
    df = pd.read_csv("C:\\Users\\Sahaj's PC\\PycharmProjects\\pythonProject4\\data.csv")
    df = df.append(d,ignore_index=True)
    st.markdown('<h3>Thank you for your feedback!</h3>', unsafe_allow_html=True)

    st.markdown('Submitted responses:')
    st.write(df)
    open('data.csv', 'w').write(df.to_csv('data.csv', index=False))

else:
    st.markdown("Click submit to save form responses.")

'''df = pd.read_csv("C:\\Users\\Sahaj's PC\\PycharmProjects\\pythonProject4\\data.csv")


dict = {'firstname': ["sahaj","ganu"], 'lastname': ["cha","pandw"]}
    #df = pd.DataFrame({'firstname': [], 'lastname': []})


    #df.loc[len(df.index)] = [firstname,lastname]
df = df.append(dict,ignore_index=True)
df'''