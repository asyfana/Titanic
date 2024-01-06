import pandas as pd
import numpy as np
import streamlit as st
import warnings

warnings.filterwarnings("ignore")

st.sidebar.title("Menu Utama")
formside = st.sidebar.form("side_form")
choose = formside.radio("pilih menu",["Titanic Data ehe", "Survived","Chart"], index=None)
formside.form_submit_button("Submit")
df = pd.read_csv("titanic.csv")

if (choose == "Titanic Data ehe"):
    st.title("Data")
    df
elif (choose == "Survived"):
    container = st.container(border=True)
    col1, col2 = container.columns([2, 2])
    col1.subheader("Titanic Dynamic List of Passenger, Age and Fare")
    col2.subheader("Choose information to display")


    df2 = df[["survived","age", "fare"]]
    # col1.dataframe(df2)
    # df2
    age = col2.slider("Slider for survivor age", 0, 100, 25)
    sv = col2.radio("Choose: ", ["Survived","Not Survived"])
    if sv=="Survived":
        svstatus = 1
    if sv=="Not Survived":
        svstatus = 0
    # with st.expander("See explanation"):
    # st.write("Age Display more or equal", age," \n ", df2.loc[(df2['survived']==svstatus) & (df2['age']>= age)])
    col1.write(df2.loc[(df2['survived']==svstatus) & (df2['age']>= age)])
    chart_data = (df2.loc[(df2['survived']==svstatus) & (df2['age']>= age)])
    col2.line_chart(chart_data)

elif (choose == "Chart"):
    chart_data = df[["survived","age","fare"]].head()
    st.line_chart(chart_data)
    st.bar_chart(chart_data)

#st.sidebar.title('Menu Farhana')
#st.title('Ini main page')
#choose = st.sidebar.radio("sila pilih", [":blue[Coklat]","***Biskut***","Teh"], index=None)

#if choose:
#    st.write(choose)
  
#df = pd.DataFrame(np.random.randn(10, 20), columns=("col %d" % i for i in range(20)))

#st.dataframe(df)


# df = pd.read_csv('titanic.csv')
# df3 = df[["survived","age"]].head() #shows first 5 rows 
# # print(df2.to_string(index=False)) #hide index
# # print(df2)
# df3



