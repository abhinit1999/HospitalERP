import streamlit as st
import requests


# Title of the app
st.title("User Registration Form")
name = st.text_input("Name")
email= st.text_input("Email")
phone = st.text_input("Phone")
password = st.text_input("Password",type="password")


# button to send user data into DB

if st.button("Save"):
    user_data={
        "name":name,
        "email":email,
        "phone":phone,
        "password":password

    }

    # sending user data to backend

    res = requests.post("http://127.0.0.1:8000/newuser",json=user_data)

    if res.status_code==200:
        st.success("Registration Successfull")
    else:
        st.error("Something went wrong")

    


# Display All records
if st.button("All Records"):
    res = requests.get("http://127.0.0.1:8000/records")
    # st.write(f"Status code: {res.status_code}")
    st.text(res.text)

    # if res.ok:
    #     try:
    #         data = res.json()
    #     except ValueError:
    #         # Not JSON, show raw text
    #         st.text(res.text)
    #     else:
    #         # If it's a list of dicts, show as a table, otherwise show JSON
    #         if isinstance(data, list) and len(data) > 0 and isinstance(data[0], dict):
               
    #             st.dataframe(pd.DataFrame(data))
    #         else:
    #             st.json(data)
    # else:
    #     st.error(f"Request failed: {res.status_code}")


   