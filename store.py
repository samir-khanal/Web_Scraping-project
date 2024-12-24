import sqlite3

def create_database():
    """
    Creates a SQLite database with a table to store players information.
    """
    conn = sqlite3.connect("player_info.db")
    cursor = conn.cursor()

# Create the players table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS players (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        club_name TEXT NOT NULL,
        market_value TEXT NOT NULL,
        age TEXT NOT NULL,
        position TEXT NOT NULL,
        profile_link TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

create_database()

def insert_player(player_data):
    """
    Inserts player data into the database.
    """
    conn = sqlite3.connect("player_info.db")
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT COUNT(*) FROM players WHERE name = ? AND club = ?
    """, (player_data['name'], player_data['club']))

    result = cursor.fetchone()
    if result[0] >0:
        print(f"The information of '{player_data['name']}' Already Exists in the database\n")
        conn.close()
        return

    cursor.execute("""
    INSERT INTO players (name, club, market_value, age, position, profile_link)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (
        player_data["name"],
        player_data["club"],
        player_data["market_value"],
        player_data["age"],
        player_data["position"],
        player_data["profile_link"]
    ))
    conn.commit()
    conn.close()
    print("Player data inserted successfully.")
