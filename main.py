import pandas as pd
import streamlit as st
import sqlite3
from datetime import date, datetime
import seaborn as sn
import matplotlib.pyplot as plt
import csv

# Configuração da página
st.set_page_config(
    page_title="Dashboard Sorveteria",
    page_icon="🍨",
    layout="wide"
)

