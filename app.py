import streamlit as st
import requests

st.title("Market Intelligence Dashboard")

query = st.text_input("Enter keyword")

if st.button("Search"):

    try:
        url = f"http://127.0.0.1:8000/search?q={query}"
        response = requests.get(url, timeout=5)

        st.write("Status Code:", response.status_code)

        if response.status_code == 200:
            data = response.json()
            st.write(data)
        else:
            st.error("API error: " + str(response.status_code))

    except Exception as e:
        st.error("Connection Error:")
        st.write(e)