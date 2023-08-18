import streamlit
import pandas
import requests

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")


streamlit.title("My Parent's New healthy Diner")
streamlit.text("🥣 Omega 3 & blueberry Oatmeal")
streamlit.text("🥗  Kale, Spinach Smoothie")
streamlit.text("🐔 Hard-boiled Free Range Egg")
streamlit.text("🥑Avocado Toast🍞")
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)


streamlit.header("Fruityvice Fruit Advice!")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#Normalize the JSON response
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# Convert the nnormalized response into a dataframe 
streamlit.dataframe(fruityvice_normalized)




