import streamlit as st
import pandas as pd
import requests
import random

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

# Given Link to search
dog_info_link = f"https://dog.ceo/dog-api/{SelectDog}"
st.markdown(f"The dog breed for name '{SelectDog}' is: [{breed}]({dog_info_link})")

# Retrieve random images using a dog image API
dog_images_url = f'https://dog.ceo/dog-api/breed/{SelectDog}/images/random' 
response = requests.get(dog_images_url)
data = response.json()
images = data['message']
images


# Display random images
for image in random.sample(images, k=min(3, len(images))):
    st.image(image, use_column_width=True, caption="Random Dog Image")
