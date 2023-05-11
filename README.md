Wikidata
This project retrieves movie data from the Wikipedia API https://query.wikidata.org/sparql and saves it to a MySQL database. Finally, it displays all the movies in a simple web page.

To execute this project, it is necessary to have MySQL installed and follow these steps:

  1. Create a virtual environment by running the following command:
    
    python3.10 -m venv env

  2. Install the required packages:
    
    pip install -r requirements

  3. Run get_data.py to get the movie data. This file calls the class in db_communication.py:
    
    python get_data.py

  4. Once the movies are in the MySQL database, export the main.py file:
  
    export FLASK_APP=main.py

  5. Run the Flask application by executing the following command:
    
    flask run

