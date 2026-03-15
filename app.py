import streamlit as st
import pickle
import pandas as pd

# load trained pipeline
pipe = pickle.load(open('finally.pkl','rb'))

st.title("IPL Win Predictor")

teams = [
'Sunrisers Hyderabad',
'Mumbai Indians',
'Royal Challengers Bangalore',
'Kolkata Knight Riders',
'Kings XI Punjab',
'Chennai Super Kings',
'Rajasthan Royals',
'Delhi Capitals'
]

cities = [
'Hyderabad','Bangalore','Mumbai','Kolkata','Delhi','Chennai',
'Jaipur','Cape Town','Port Elizabeth','Durban','Centurion',
'East London','Johannesburg','Kimberley','Bloemfontein',
'Ahmedabad','Cuttack','Nagpur','Dharamsala','Visakhapatnam',
'Pune','Raipur','Ranchi','Abu Dhabi','Sharjah','Mohali',
'Bengaluru'
]

col1,col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Batting Team',sorted(teams))

with col2:
    bowling_team = st.selectbox('Bowling Team',sorted(teams))

city = st.selectbox('Match City',sorted(cities))

target = st.number_input('Target Score')

col3,col4,col5 = st.columns(3)

with col3:
    score = st.number_input('Current Score')

with col4:
    overs = st.number_input('Overs Completed')

with col5:
    wickets = st.number_input('Wickets Out')

if st.button('Predict Probability'):

    runs_left = target - score
    balls_left = 120 - (overs*6)
    wickets_remaining = 10 - wickets

    crr = score / overs
    rrr = (runs_left*6) / balls_left

    input_df = pd.DataFrame({
        'batting_team':[batting_team],
        'bowling_team':[bowling_team],
        'city':[city],
        'runs_left':[runs_left],
        'balls_left':[balls_left],
        'wickets':[wickets_remaining],
        'total_runs_x':[target],
        'crr':[crr],
        'rrr':[rrr]
    })

    result = pipe.predict_proba(input_df)

    loss = result[0][0]
    win = result[0][1]

    st.header(batting_team + " Win Probability: " + str(round(win*100)) + "%")
    st.header(bowling_team + " Win Probability: " + str(round(loss*100)) + "%")