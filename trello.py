import pdb
import requests
import pprint

Key = "0921aebd7b396482a18647f3aadd8360"
Token = "9eb30e398b251cc85c1d9699203b65e33b8b84430b219643c6ec510412848c6c"
Board_ID = "600ab283e04b565bfdd9ee26"
to_do_list = "600ab283e04b565bfdd9ee28"
in_progress_list = "600ab283e04b565bfdd9ee29"
complete_list = "600ab283e04b565bfdd9ee2a"

get_cards_url = f"https://api.trello.com/1/boards/{Board_ID}/cards"

query = {
    "key": Key,
    "token": Token,
}

cards = requests.get(get_cards_url, params=query).json()
for card in cards: 
    if card["name"] == "Module 2":
        id = card["id"]
        url = f"https://api.trello.com/1/cards/{id}"
        data = {"idList": in_progress_list}
        response = requests.put(url, data=data, params=query)