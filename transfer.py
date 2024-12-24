import requests
from bs4 import BeautifulSoup
from store import insert_player
from authentication import authenticate

def find_player_list(search_term):

    url= f'https://www.transfermarkt.com/schnellsuche/ergebnis/schnellsuche?query={search_term}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    players = soup.find_all('table', class_='inline-table')

    return players

def extract_player_data(players):
    # extracts player names, clubs, and links from the fetched player list.
    fetched_names = []
    home_url = "https://www.transfermarkt.com"

    for name in players:
        # Extracting player name
        player_name_elem = name.find('td', class_='hauptlink')
        if 'title' in player_name_elem.a.attrs:
            player_name = player_name_elem.a['title']       # Using title attribute for accurate player data pull
            player_link = home_url + player_name_elem.a['href']  
        else:
            continue
        # extracting club info
        club_elem = name.find_all('td')[-1] # club info is in the last 
        if club_elem:
            club = club_elem.text.strip()
        else:
            club = "Unknown Club"
        
        if "retired" in club.lower():
            fetched_names.append({"player_name": player_name, "club": "Retired", "link": player_link})
            break
        else:
            fetched_names.append({"player_name": player_name, "club": club,  "link": player_link})
    return fetched_names

def select_player(fetched_names):
    # allows user to select player from the fetched list   
    if len(fetched_names) == 1:
        print(f"Only one player found: {fetched_names[0]['player_name']}, Club: {fetched_names[0]['club']}\n")
        while True:
            confirm = input("Do you want more information about this player? (yes/no)\n").strip().lower()
            if confirm == 'yes':
                return fetched_names[0]  # Automatically select the first player
            elif confirm == 'no':
                print("Exiting the program.")
                exit()
            else:
                print("Invalid input! Please enter 'yes' or 'no'.")
    else:
        while True:
            for index, name in enumerate(fetched_names, start=1):
                if "retired" in name['club'].lower():
                    print(f"{index}. {name['player_name']} is retired!!")
                else:
                    print(f"{index}. {name['player_name']}\n Club: {name['club']}\n")
            
            try:
                player_select = int(input("Enter the player number you want the information about\n"))
                
                if player_select < 1 or player_select > len(fetched_names):
                    print(f"Invalid number!! Please enter a valid number between 1 and {len(fetched_names)}\n")
                else:
                    player_index = player_select - 1
                    return fetched_names[player_index]   
            except (IndexError,ValueError):
                print(f"Please Enter number between 1 and {len(fetched_names)}\n ")
                

def fetch_player_details(selected_player):
  #fetches new information about selected players from their profile link
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    }
    player_detail_response = requests.get(selected_player['link'], headers=headers)
    player_detail_soup = BeautifulSoup(player_detail_response.text, 'html.parser')

    market_value_elem = player_detail_soup.find('a',class_='data-header__market-value-wrapper')
    market_value = market_value_elem.text.strip().split('Last update:')[0].strip() if market_value_elem else "Market value not available"
    # if market_value_elem:
    #     market_value = market_value_elem.text.strip()
    # # Removing "Last update:" and any text after it
    #     market_value = market_value.split('Last update:')[0].strip()
    # else:
    #     market_value = "Market value not available"
    

    club_elem = player_detail_soup.find_all('span', class_=['info-table info-table--right-space','info-table__content info-table__content--bold info-table__content--flex'])
    club = club_elem[1].text.strip() if len(club_elem) > 1 else "Club not available!"

    age_elem = player_detail_soup.find('span',itemprop='birthDate', class_='data-header__content')
    age = age_elem.text.strip() if age_elem else "Age is not available!"

    position_elem = player_detail_soup.find('dd', class_=['detail-position__inner-box','detail-position__position'])
    position = position_elem.text.strip() if position_elem else "Position not available!"

    return {
        "name": selected_player['player_name'],
        "club": selected_player['club'],
        "market_value": market_value,
        "age": age,
        "position": position,
        "profile_link": selected_player['link']
    }

def main():
    # main function used for player search and data handling    
    while True:
        search_term = input("Which player do you want to search for\n").lower()
        players = find_player_list(search_term)

        if len(players) < 1:
            print(f"Sorry, no players found with the name '{search_term}'")
        else:
            print(f"Players found with the name similar to the '{search_term}'\n")
            break
    fetched_names = extract_player_data(players)

    if not fetched_names:
        print("no players to select so, exiting the program.")
        return   
    selected_player = select_player(fetched_names)
    if not selected_player:
        print("No player selected. Exiting.")
        return
    
    player_data = fetch_player_details(selected_player)
    if player_data:
        print(f"\nYou selected: {player_data['name']}")
        print(f"Market Value: {player_data['market_value']}")
        print(f"Club: {player_data['club']}")
        print(f"Date of birth/Age: {player_data['age']}")
        print(f"Position: {player_data['position']}")
        print(f"Profile Link: {player_data['profile_link']}\n")
        insert_player(player_data)

if __name__ == "__main__":
    if authenticate():
        main()
    else:
        print("You have been Denied by our host to enter this program")







