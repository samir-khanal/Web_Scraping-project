# Web_Scraping-project
Transfer Market (football) players information scraping project

## Football Player Info Scraper 🏆⚽

### Overview
This project allows users to search for football player information using web scraping from Transfermarkt. The data includes player names, club details, market value, age, position, and profile links.

### Features
- ✅ User Authentication (Username & Password Required)
- ✅ Search for Any Football Player
- ✅ Retrieve Detailed Player Information (Market Value, Club, Age, Position)
- ✅ Store Player Data in a Local Database (player_info.db)
- ✅ Secure Credential Management Using config.py

### Setup Instructions
1. Clone the Repository
    ```sh
    git clone https://github.com/samir-khanal/Web_Scraping-project.git
    cd Web_Scraping-project
    ```
2. Install Required Dependencies
    Ensure you have Python installed (≥3.7), then run:
    ```sh
    pip install -r requirements.txt
    ```
3. Configure Authentication
    For security reasons, credentials are not included in the repository.

    **Option 1: Using a config.py file**
    Copy the example configuration file:
    ```sh
    cp config.example.py config.py
    ```
    Open config.py and set your username & password:
    ```python
    APP_USERNAME = "testuser"
    APP_PASSWORD = "testpass"
    ```

    **Option 2: Using Environment Variables (Recommended for production)**
    Instead of using config.py, set credentials as environment variables:
    ```sh
    export APP_USERNAME="testuser"
    export APP_PASSWORD="testpass"
    ```
    (For Windows users, use `set` instead of `export`.)

### Running the Project
To start the program, run:
```sh
python transfer.py
