import streamlit as st
# Insert a Title in Page
st.title("Practice a Login Page")
# Heading of the page
st.header("Login/SignUp")
# Set a Text
st.text("Please write valid user name and password if already SignUp or go to SignUp if not done Yet")
# Add a Selection Box
st.selectbox("Select an option",['Login','SignUp'])
#Enter in inputbox
UserName = st.text_input("User Name", "")
st.write("Your User Name is ",UserName )
#Enter Password
Password = st.text_input("Password", type="password")
#Add Button
st.button("Login")
# Add a Check Box
st.checkbox("Forget Password.")


