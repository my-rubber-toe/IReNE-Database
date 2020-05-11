# IReNE-Database

## Dependencies
    ```
        1. Python 3.8.0
        2. pip3 19.03
        3. Mongoengine 0.19.1
        4. Mongodb 4.2.5
    ```
## Download libraries
- To download the libraries needed, run requirements.txt as
    - `pip install -r requirements.txt` 

## Technical Documentation
- For a Technical documentacion of the main files of this repository, follow this path
    - `Documentation -> _build -> html -> index.html`
    - Run index.html in your browser

## How to initialize the database

1. First download the following mongodb library:
    - `npm install mongodb --save`
2. Run the init_db.js file where it will initialize db with its collections & restrictions.
    - `node init_db.js`
3. Open another terminal window and go back to the database repository.
4. Run predefined_data.py to fill the database with all the predefined data that it's going to have.
    - `python3 predefined_data.py`
5. Run mock_data.py to fill the database with mock data of collaborators & documents
    - `python3 mock_data.py`
