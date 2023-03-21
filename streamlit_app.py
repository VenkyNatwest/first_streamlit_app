import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My parents new healthy diner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text( '🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text(  '🐔 Hard-Boiled Free-Range Egg')
streamlit.text( '🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list=pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list=my_fruit_list.set_index('Fruit')
selected_fruits=streamlit.multiselect('pick some fruits : ', list(my_fruit_list.index),['Avocado','Cantaloupe'])
fruits_to_show=my_fruit_list.loc[selected_fruits]
streamlit.dataframe(fruits_to_show)

def get_fruityvice_data(this_fruit_data):
     fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
     fruityvise_normalised=pandas.json_normalize(fruityvice_response.json())
     return fruityvise_normalised
  

streamlit.header('Fruityvise fruit advice')
try:
  fruit_choice=streamlit.text_input('What fruit would you like nformation about ?')
  if not fruit_choice:
     streamlit.error('Please select a fruit')
  else:
      streamlit.dataframe(get_fruityvice_data(fruit_choice))
except URLError as e:
    streamlit.error()

def get_fruit_load_list():
     with my_cnx.cursor() as my_cur:
          my_cur.execute("select * from fruit_load_list")
     return  my_cur.fetchall()

if streamlit.button('Click to load fruits'):
     my_data_row = get_fruit_load_list()
     streamlit.header("The fruit load list contains:")
     streamlit.dataframe(my_data_row)

streamlit.stop()
streamlit.header('Fruityvise fruit advice')
fruit_to_add=streamlit.text_input('What fruit would you like to add?','jack fruit')
my_cur.execute("insert into FRUIT_LOAD_LIST values ('from streamlit')")
streamlit.write('Thanks for adding', fruit_to_add)


