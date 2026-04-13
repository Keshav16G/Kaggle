import streamlit as st 
import pandas as pd
import joblib

model = joblib.load('KNN_heart.pkl')