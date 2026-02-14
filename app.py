import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

st.set_page_config(
    page_title="Pakistan Population Diagnostic System 🇵🇰",
    page_icon="🇵🇰",
    layout="wide"
)

DATA_FILE = "pakistan_population.csv"

@st.cache_data
def load_data():
    if not os.path.exists(DATA_FILE):
        st.error("Dataset file not found")
        return pd.DataFrame()

    df = pd.read_csv(DATA_FILE)

    if "Male Population" not in df.columns:
        df["Male Population"] = df["Total Population"] - df["Female Population"]

    df["Annual Growth Rate (%)"] = df["Total Population"].pct_change() * 100
    df.fillna(0, inplace=True)

    return df


def save_data(df):
    df.to_csv(DATA_FILE, index=False)
    st.cache_data.clear()


df = load_data()

st.sidebar.title("Navigation 🇵🇰")

page = st.sidebar.selectbox(
    "Choose Page",
    ["Dashboard", "Search", "Add", "Update", "Delete", "Charts"]
)

if page == "Dashboard":

    st.title("Pakistan Population Dashboard 🇵🇰")

    if not df.empty:

        latest = df["Total Population"].iloc[-1]
        first = df["Total Population"].iloc[0]
        growth = latest - first
        avg = df["Annual Growth Rate (%)"].mean()

        col1, col2, col3 = st.columns(3)

        col1.metric("Latest Population", f"{latest:,.0f}")
        col2.metric("Total Growth", f"{growth:,.0f}")
        col3.metric("Average Growth Rate", f"{avg:.2f}%")


        st.dataframe(df)


elif page == "Search":

    st.title("Search")

    year = st.number_input("Enter year", 1960, 2100, 2020)

    result = df[df["Year"] == year]

    if not result.empty:
        st.dataframe(result)
    else:
        st.warning("No data found")


elif page == "Add":

    st.title("Add Record")

    year = st.number_input("Year", 1960, 2100)
    total = st.number_input("Total Population")
    female = st.number_input("Female Population")
    urban = st.number_input("Urban Population")
    rural = st.number_input("Rural Population")

    if st.button("Add"):

        male = total - female

        new = pd.DataFrame({
            "Year":[year],
            "Total Population":[total],
            "Female Population":[female],
            "Urban Population":[urban],
            "Rural Population":[rural],
            "Male Population":[male]
        })

        df2 = pd.concat([df,new])

        save_data(df2)

        st.success("Added")


elif page == "Update":

    st.title("Update")

    year = st.number_input("Year to update",1960,2100)

    if year in df["Year"].values:

        row = df[df["Year"]==year].iloc[0]

        total = st.number_input("Total Population",value=int(row["Total Population"]))
        female = st.number_input("Female Population",value=int(row["Female Population"]))

        if st.button("Update"):

            df.loc[df["Year"]==year,"Total Population"]=total
            df.loc[df["Year"]==year,"Female Population"]=female
            df.loc[df["Year"]==year,"Male Population"]=total-female

            save_data(df)

            st.success("Updated")


elif page == "Delete":

    st.title("Delete")

    year = st.number_input("Year to delete",1960,2100)

    if st.button("Delete"):

        df2 = df[df["Year"]!=year]

        save_data(df2)

        st.success("Deleted")


elif page == "Charts":

    st.title("Charts")

    st.line_chart(df.set_index("Year")["Total Population"])

    fig,ax=plt.subplots()

    ax.bar(df["Year"],df["Total Population"])

    st.pyplot(fig)
