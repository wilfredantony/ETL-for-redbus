# ETL-for-redbus
Redbus Bus details Extraction

EXTRACTION:
  - Scrapped the data from the Redbus website using selenium.
  - Sourced 10 State Transport Bus details which includes Government and Private buses.
  - Created for loops to navigate to the pages, click  to the specific route and clicking the view buses options in a page that has bus details and for extracting the bus details.
  - Included while loop to scroll the page.
  - Added if else conditions if the buses are not availabe on the dates.
  LIMITATIONS:
    - A for loop can be build for the links so that it reduces the time and won't have to repeat the programe again and again.
    - Instead of creating a list in the same cell we can create it on another cell and append the extracted to the list.
   
      
TRANSFORMATION:
  -Cleaned the data using pandas.
    - Collected the data in a list and converted the same data to a Dataframe.
    - Created an individual CSV file for each State.
    - Merged every state transport dataframe into one.
    - Changed the type for the respective columns.

LOADING:
  - Created a database in Postgres using Python.
  - Created a table and pushed the Dataframe into postgres.

UI-CREATION:(Using STREAMLIT)
  - Created an User Interface to view the collected data.
  - Connected the UI and Database.
  - Using UI we can select the specific bus in the available buses for a selected route.

  
    
    
