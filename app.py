# -*- coding: utf-8 -*-
"""
Created on Thu May 18 14:51:25 2023

@author: ROHIT
"""

import streamlit as st
import pickle
from PIL import Image


load = open('mod.pkl', 'rb')
model = pickle.load(load)

#st.image("C:\Users\ROHIT\Desktop\1 Poject\image.jpg")
image = Image.open('image.jpg')
st.image(image, caption='Boom Bikes')
st.title('Bike Sharing Company Predictor ')


def predict(season, year, month, holiday, weekday, workingday,
            weathersit, temp, atemp, hum, windspeed):
    pred= model.predict([[season, year, month, holiday, weekday, workingday,
                weathersit, temp, atemp, hum, windspeed]])
    return pred

def start():
    season = st.selectbox('Which season is it?', ('Fall', 'Summer', 'Spring', 'Winter'))
    year = st.selectbox('Which year?', ('2018','2019'))
    month = st.select_slider('Month?', ('January', 'February','March','April','May','June','July','August','September','October','November','December'))
    holiday =st.selectbox('Is it Holiday?', ('Holiday','not holiday'))
    weekday =st.selectbox('Which day is it?', ('monday','tuesday','wednesday','thursday','friday','saturday','sunday'))
    workingday =st.selectbox('Was it working day?',('Working day','Non-Working day'))
    weathersit =st.selectbox('How is the Weather?',('clear','misty','light snow'))
    temp =st.number_input('What is the temp?',min_value=2.42,max_value=35.32)
    atemp =st.number_input('What do you feel the temperature is?',min_value=3.95, max_value=42.04)
    hum =st.number_input('How humid it is?',min_value=0.0,max_value=97.25)
    windspeed =st.number_input('How much is the windspeed?',min_value=1.5,max_value=34.0)
    
 
    
    if st.button('Predict'):
        result = predict(season, year, month, holiday, weekday, workingday,
                    weathersit, temp, atemp, hum, windspeed)
        st.success('How many customer will rent a bike? : {} '.format(result) )
        
if __name__== '__main__':
    start()
    