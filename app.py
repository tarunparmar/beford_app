import pandas as pd
import streamlit as st
import plotly.express as px
import streamlit as st
import functions


def main():
    st.title("Application of Benford's Law to any dataset")

    menu = ["Titanic_data","Census_2009b_data","Banking_data","User_data"]
    choice = st.sidebar.selectbox("Select Dataset",menu)

    if choice == "Titanic_data":
        st.subheader("Titanic data")

        df = pd.read_csv('titanic.csv')
        st.dataframe(df)
        fig, df_digit = functions.benfords(df)
        if fig:
            st.caption("Benford's Law applied to selected Column")
            st.plotly_chart(fig)
            st.caption("Chart Data")
            st.dataframe(df_digit) 
            chi_square_stat = functions.chi_square_test(df_digit['Frequency'],df_digit['Benford'])

            st.caption("\nChi Squared Test Statistic = {:.3f}".format(chi_square_stat))
            st.caption("Critical value at P-value of 0.05 is 15.51")
            st.caption("The Observed and the expected distributions are the same : ")
            st.caption(chi_square_stat < 15.51)   

    elif choice == "Census_2009b_data":
        st.subheader("Census_2009b data")
        
        df = pd.read_csv('census_2009b.csv')
        st.dataframe(df)
        fig, df_digit = functions.benfords(df)
        if fig:
            st.caption("Benford's Law applied to selected Column")            
            st.plotly_chart(fig)
            st.caption("Chart Data")
            st.dataframe(df_digit) 
            chi_square_stat = functions.chi_square_test(df_digit['Frequency'],df_digit['Benford'])

            st.caption("\nChi Squared Test Statistic = {:.3f}".format(chi_square_stat))
            st.caption("Critical value at P-value of 0.05 is 15.51")
            st.caption("The Observed and the expected distributions are the same : ")
            st.caption(chi_square_stat < 15.51)   

    elif choice == "Banking_data":
        st.subheader("Bank Marketing Campaign data")
        
        df = pd.read_csv('bank_marketing_data.csv')
        st.dataframe(df)
        fig, df_digit = functions.benfords(df)
        if fig:
            st.caption("Benford's Law applied to selected Column")            
            st.plotly_chart(fig)
            st.caption("Chart Data")
            st.dataframe(df_digit) 
            chi_square_stat = functions.chi_square_test(df_digit['Frequency'],df_digit['Benford'])

            st.caption("\nChi Squared Test Statistic = {:.3f}".format(chi_square_stat))
            st.caption("Critical value at P-value of 0.05 is 15.51")
            st.caption("The Observed and the expected distributions are the same : ")
            st.caption(chi_square_stat < 15.51)   

    elif choice == "User_data":
        st.subheader("User uploaded dataset")
        data_file = st.file_uploader("Upload CSV",type=["csv"])

        if data_file is not None:

            file_details = {"filename":data_file.name, "filetype":data_file.type,
                            "filesize":data_file.size}

            st.write(file_details)
            df = pd.read_csv(data_file)
            fig, df_digit = functions.benfords(df)
            if fig:
                st.caption("Benford's Law applied to selected Column")
                st.plotly_chart(fig)
                st.caption("Chart Data")
                st.dataframe(df_digit) 
                chi_square_stat = functions.chi_square_test(df_digit['Frequency'],df_digit['Benford'])

                st.caption("\nChi Squared Test Statistic = {:.3f}".format(chi_square_stat))
                st.caption("Critical value at P-value of 0.05 is 15.51")
                st.caption("The Observed and the expected distributions are the same : ")
                st.caption(chi_square_stat < 15.51)   

if __name__ == '__main__':
	main()