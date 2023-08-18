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

#create reusable code block

def get_fruityvice_data (this_fruit_choice) :
      streamlit.write('The user entered ', this_fruit_choice)
      fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
      fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
      return fruityvice_normalized

def get_fruit_load_list ():
      with  my_cnx1.cursor() as my_cur1 :
            my_cur1.execute("SELECT * from fruit_load_list")
            my_data_row1 = my_cur1.fetchall()
            return my_data_row1

def insert_row_snowflake(fruit_sent) :
      with  my_cnx1.cursor() as my_cur1 :
            my_cur1.execute("insert into fruit_load_list values('" + fruit_sent   + "')")
            my_data_row1 = my_cur1.fetchall()
            return "Thank you for adding " + fruit_sent

#New section to display FruityVice API results
streamlit.header("View our Fruit list . Add your favourites ")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice :
      streamlit.error("Please select a fruit to get information")

  else :
      back_from_function=get_fruityvice_data(fruit_choice)
      streamlit.dataframe(back_from_function)
    
except URLError as e :
  streamlit.error()


if streamlit.button('Get Fruit  List') :
      my_cnx1 = snowflake.connector.connect(**streamlit.secrets["snowflake"])
      my_data_rows = get_fruit_load_list ()
      my_cnx1.close()
      streamlit.dataframe(my_data_rows)

fruit_choice_final = streamlit.text_input('View our Fruit list . Add your favourites  ','Enter Here')
if streamlit.button('Add a Fruit to the List') :
      my_cnx1 = snowflake.connector.connect(**streamlit.secrets["snowflake"])
      back_from_function = insert_row_snowflake(fruit_choice_final)
      my_cnx1.close()
      streamlit.text(back_from_function)



