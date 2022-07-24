import pandas as pd
import streamlit as st
import plotly.express as px
import math
from collections import Counter
import plotly.graph_objects as go
from math import log10
from pandas.api.types import is_numeric_dtype

def benfords(df):
    st.subheader("Select target column 👇:")    
    target_column = st.selectbox("", df.columns, index = len(df.columns) - 1)
    
    fig = None
    df_digit = pd.DataFrame()
    if is_numeric_dtype(df[target_column]) == True:
        # keep track of list of first digits
        digits = []
        df[target_column] = df[target_column].fillna(0)
        # loop through all daily cases and extract first digit (skip first row NaN)
        for amount in df[target_column][1:]:
            first_digit = int(str(amount)[0])
            digits.append(first_digit)

        # setup dataframe with first digit frequency and Benford expected frequency
        df_digit['Number'] = [digit for digit in range(1,10)]
        df_digit['Count'] = [Counter(digits)[number] for number in df_digit['Number']]
        df_digit['Frequency'] = [float(count) / (df_digit['Count'].sum()) for count in df_digit['Count']]
        df_digit['Benford'] = [log10(1 + 1 / float(d)) for d in range(1,10)]

        st.subheader("Trend of target column")
        fig = go.Figure()
        fig.add_trace(go.Bar(x=df_digit.Number, 
                            y=df_digit.Frequency, 
                            name='Actual'))
        # fig.update_yaxes(type='Frequency')
        fig.add_trace(go.Scatter(x= df_digit.Number, 
                                y=df_digit.Benford, 
                                mode = 'lines+markers', 
                                name='Benford'))
        fig.update_xaxes(title_text="Digits")
        fig.update_yaxes(title_text="Frequency")
        
    else:
        print(f'The selected column is not numeric!{target_column}')
        st.error('The selected column is not numeric!')

    return fig, df_digit


def chi_square_test(data_count, expected_counts):
  """Return boolean on chi-square test (8 DOF & P-val=0.05)."""
  chi_square_stat = 0; # chi-square test statistic
  for data, expected in zip(data_count, expected_counts):
    chi_square = math.pow(data - expected, 2)
    chi_square_stat += chi_square / expected

  return chi_square_stat