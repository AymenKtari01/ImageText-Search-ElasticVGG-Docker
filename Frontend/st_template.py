import streamlit as st


def header():
    header = f"""
        <h1 >
           🔍 Find by Text, Explore by Image🖼️
        </h1>"""
    return st.markdown(header, unsafe_allow_html=True)
def footer():
    footer = f"""
        <p style="margin-left:12em;"><b>Done by : Anas Ben Amor & Aymen Ktari</b></p>
    """
    return st.markdown(footer, unsafe_allow_html=True)