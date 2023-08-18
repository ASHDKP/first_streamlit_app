import streamlit
import pandas
import requests
import snowflake.connector

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

#New section to display FruityVice API results
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice :
      streamlit.error("Please select a fruit to get information")

  else :
      streamlit.write('The user entered ', fruit_choice)
      fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
      fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
      streamlit.dataframe(fruityvice_normalized)
except URLError as e :
  streamlit.error()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)



my_cnx1 = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur1 = my_cnx1.cursor()
my_cur1.execute("SELECT * from fruit_load_list")
my_data_row1 = my_cur1.fetchall()
streamlit.header("The fruit list contains")
streamlit.dataframe(my_data_row1)

fruit_choice_final = streamlit.text_input('What fruit would you like to add? ','Enter Here')
streamlit.write('Thank you for adding ', fruit_choice_final)



