import streamlit as st
import pandas as pd
import requests
import random
from PIL import Image

#Set Page Title
st.set_page_config(page_title="Login Page")

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

# Create DataFrame
df=pd.read_excel(io ="BreedStreamlit.xlsx" , engine='openpyxl')
st.dataframe(df)

# Selection Box with Dog Names
SelectDog = st.selectbox("Select Dog Type", options= df['Dog'])

# Find Dog breed of the selected Dog
filtered_df = df[df['Dog'] == SelectDog]
breed = filtered_df.iloc[0]['Breeds']
st.write(f"The dog breed for name '{SelectDog}' is: {breed}")

def get_random_dog_image_url(breed):
    url = f'https://dog.ceo/api/breed/{breed}/images/random/'
    response = requests.get(url)
    data = response.json()
    return data['message']

# Create a hyperlink 
with st.container():
    dog_info_link = 'https://dog.ceo/api/'
    st.write("[Dog Link >](https://dog.ceo/api/)")

 # Get a random dog image URL
image_url = get_random_dog_image_url(breed)
st.image(image_url, caption=f"Random {breed} Image", use_column_width=True)




