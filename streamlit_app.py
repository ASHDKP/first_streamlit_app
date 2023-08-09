import streamlit
import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")


streamlit.title("My Parent's New healthy Diner")
streamlit.text("🥣 Omega 3 & blueberry Oatmeal")
streamlit.text("🥗  Kale, Spinach Smoothie")
streamlit.text("🐔 Hard-boiled Free Range Egg")
streamlit.text("🥑Avocado Toast🍞")
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
streamlit.dataframe(my_fruit_list)


