import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

# Database connection details
host = "localhost"
user = "postgres"
password = "wilfred1999"  
db_name = "Redbus_Info"

# Create engine and session
engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}/{db_name}')
Session = sessionmaker(bind=engine)
session = Session()
st.set_page_config(layout="wide")

st.title("Available Bus Details")

# Sidebar filters
st.sidebar.header("Filters")

# Fetch unique route names from the database
try:
    routes = session.execute(text('SELECT DISTINCT route FROM "Bus_details"')).fetchall()
    routes = [r[0] for r in routes]
except Exception as e:
    st.error(f"Error fetching data from database: {e}")
    routes = []

# Filter options
selected_route = st.sidebar.selectbox("Route Name", ["All"] + routes)

# Fetch unique bus names based on the selected route
try:
    if selected_route == "All":
        buses = session.execute(text('SELECT DISTINCT name FROM "Bus_details"')).fetchall()
    else:
        buses = session.execute(text('SELECT DISTINCT name FROM "Bus_details" WHERE route = :route'), {'route': selected_route}).fetchall()
    buses = [b[0] for b in buses]
except Exception as e:
    st.error(f"Error fetching data from database: {e}")
    buses = []

selected_bus = st.sidebar.selectbox("Bus Name", ["All"] + buses)



min_price = st.sidebar.number_input("Minimum Price", min_value=0, value=0)
max_price = st.sidebar.number_input("Maximum Price", min_value=0, value=10000)
min_rating = st.sidebar.slider("Minimum Rating", 0.0, 5.0, 0.0, 0.1)
min_seats = st.sidebar.number_input("Minimum Seats Available", min_value=0, value=0)

# Build query
query = 'SELECT * FROM "Bus_details" WHERE 1=1'
if selected_route != "All":
    query += f" AND route = '{selected_route}'"
if selected_bus != "All":
    query += f" AND name = '{selected_bus}'"
if min_price > 0:
    query += f" AND price >= {min_price}"
if max_price < 10000:
    query += f" AND price <= {max_price}"
if min_rating > 0.0:
    query += f" AND rating >= {min_rating}"
if min_seats > 0:
    query += f" AND seats_available >= {min_seats}"


# Execute query and display data

with engine.connect() as connection:
    bus_details_df = pd.read_sql(query, connection)
    st.markdown(
        """<style>
        .dvn-scroller glideDataEditor{
            width: 100%;
            height: 200px;
            overflow-x: scroll;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.dataframe(bus_details_df,height=10000,width=10000)  # Adjust the width as needed

    

