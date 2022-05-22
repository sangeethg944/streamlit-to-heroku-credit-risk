import streamlit as st
import joblib
import xgboost
import pandas as pd
import numpy as np

st.title("Credit Risk Prediction")
model = joblib.load('71_acc_xgboost_model.joblib')


def predicting_risk(d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15, d16, d17, d18, d19, d20):
    if d3 == '1':
        d3 = 1
    elif d3 == '2':
        d3 = 2
    elif d3 == '3':
        d3 = 3
    else:
        d3 = 4

    if d8 == 'Moderate':
        d8 = 0
    elif d8 == 'No checking account':
        d8 = 1
    elif d8 == 'little':
        d8 = 2
    else:
        d8 = 3

    if d9 == 'Existing credits paid back duly':
        d9 = 0
    elif d9 == 'Critical account':
        d9 = 1
    elif d9 == 'Delay in paying off in the past':
        d9 = 2
    elif d9 == 'No credits taken':
        d9 = 3
    else:
        d9 = 4

    if d10 == 'Radio/Television':
        d10 = 0
    elif d10 == 'Education':
        d10 = 1
    elif d10 == 'Furniture/Equipment':
        d10 = 2
    elif d10 == 'Car (new)':
        d10 = 3
    elif d10 == 'Car (used)':
        d10 = 4
    elif d10 == 'Business':
        d10 = 5
    elif d10 == 'Domestic appliances':
        d10 = 6
    elif d10 == 'Repairs':
        d10 = 7
    elif d10 == 'Others':
        d10 = 8
    else:
        d10 = 9

    if d11 == 'Little':
        d11 = 0
    elif d11 == 'No savings account':
        d11 = 1
    elif d11 == 'Quite Rich':
        d11 = 2
    elif d11 == 'Rich':
        d11 = 3
    else:
        d11 = 4

    if d12 == 'Professional':
        d12 = 0
    elif d12 == 'Expert':
        d12 = 1
    elif d12 == 'Master':
        d12 = 2
    elif d12 == 'Unemployed':
        d12 = 3
    else:
        d12 = 4

    if d13 == 'female : single':
        d13 = 0
    elif d13 == 'female : divorced':
        d13 = 1
    elif d13 == 'male : single':
        d13 = 2
    elif d13 == 'male : divorced':
        d13 = 3
    else:
        d13 = 4

    if d14 == 'None':
        d14 = 0
    elif d14 == 'Guarantor':
        d14 = 1
    else:
        d14 = 2

    if d15 == 'Real estate':
        d15 = 0
    elif d15 == 'Building society savings agreement/ Life Insurance':
        d15 = 1
    elif d15 == 'Unknown / No property':
        d15 = 2
    else:
        d15 = 3

    if d16 == 'None':
        d16 = 0
    elif d16 == 'Bank':
        d16 = 1
    else:
        d16 = 2

    if d17 == 'own':
        d17 = 0
    elif d17 == 'For Free':
        d17 = 1
    else:
        d17 = 2

    if d18 == 'Skilled employee':
        d18 = 0
    elif d18 == 'Unskilled':
        d18 = 1
    elif d18 == 'Qualified employee':
        d18 = 2
    else:
        d18 = 3

    if d19 == 'No':
        d19 = 0
    elif d19 == 'Yes':
        d19 = 1

    if d20 == 'Yes':
        d20 = 0
    elif d20 == 'No':
        d20 = 1

    arr = [d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15, d16, d17, d18, d19, d20]
    arr = np.array(arr)
    input_ = arr.reshape(1, -1)

    prediction = model.predict(input_)
    return prediction[0]


with st.form(key='credit_risk_form', clear_on_submit=True):
    duration = st.number_input(label='Duration of Holding the account(in months)', step=1)
    cred_amt = st.number_input(label='Credit Amount', min_value=0, step=10)
    inst_rate = st.selectbox(label='Installment rate', options=('1', '2', '3', '4'))
    resid_years = st.number_input(label='Stayed in the Present Residence(in years)', step=1)
    age = st.number_input(label='Age',step=10)
    num_credits = st.number_input(label='No of credits', min_value=0, step=1)
    num_people = st.number_input(label='No of people liable to pay for maintenance', min_value=0)
    check_amt = st.selectbox(label='Checking Amount', options=('Moderate', 'No checking account', 'little', 'Rich'))
    cred_hist = st.selectbox(label='Credit history', options=('Existing credits paid back duly', 'Critical account',
                                                              'Delay in paying off in the past', 'No credits taken',
                                                              'All credits paid back duly'))
    purpose = st.selectbox(label='Purpose of credit taken',
                           options=('Radio/Television', 'Education', 'Furniture/Equipment', 'Car (new)',
                                    'Car (used)', 'Business', 'Domestic appliances', 'Repairs', 'Others',
                                    'Retraining'))
    sav_amt = st.selectbox(label='Savings Amount',
                           options=('Little', 'No savings account', 'Quite Rich', 'Rich', 'Moderate'))
    employ = st.selectbox(label='Level of employment',
                          options=('Professional', 'Expert', 'Master', 'Unemployed', 'Amateur'))
    pers_stat = st.selectbox(label='Personal status',
                             options=('female : single', 'female : divorced', 'male : single', 'male : divorced',
                                      'male : married'))
    debt_guar = st.selectbox(label='Debtor/Guarantor', options=('None', 'Guarantor', ' Co-Applicant'))
    property = st.selectbox(label='Any property owned',
                            options=('Real estate', 'Building society savings agreement/ Life Insurance',
                                     'Unknown / No property', 'Car or other'))
    inst_plan = st.selectbox(label='Installment payment plan', options=('None', 'Bank', 'Stores'))
    house = st.selectbox(label='Current housing', options=('Own', 'For Free', 'Rent'))
    job_type = st.selectbox(label='Type of job',
                            options=('Skilled employee', 'Unskilled', 'Qualified employee', 'Unemployed'))
    tel = st.selectbox(label='Is telephone available?', options=('No', 'Yes'))
    NRI = st.selectbox(label='Whether NRI or not', options=('Yes', 'No'))

    if st.form_submit_button(label='Predict'):
        result = predicting_risk(duration,cred_amt,inst_rate,resid_years, age, num_credits,num_people, check_amt,
                                 cred_hist, purpose, sav_amt,employ,pers_stat,debt_guar,property,inst_plan,house,job_type,tel,NRI)
        if result == 1:
            st.success('The customer is not expected to have credit risk')
        else:
            st.success('The customer is expected to have credit risk')


# arr = [duration, cred_amt, inst_rate, resid_years, age, num_credits, num_people, check_amt, cred_hist,
#        purpose, sav_amt, employ, pers_stat, debt_guar, property, inst_plan, house, job_type, tel, NRI]
# input_ = arr.reshape(1, -1)
#
# prediction = model.predict(input_)


