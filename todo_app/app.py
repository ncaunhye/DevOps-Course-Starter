from flask import Flask, render_template, redirect, request
import todo_app.data.session_items as session_items
import requests
import os

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def index():
    todos=[]

#Fetch all to-do items (cards) for the specified board
    cards_url = f"https://api.trello.com/1/boards/{os.getenv('Trello_Board_ID')}/cards"

    query = {
        'key': os.getenv('Trello_API_Key'),
        'token': os.getenv('Trello_API_Token')
        }

    response = requests.get(
        cards_url,
        params=query
        )
    trello_data=response.json()
    for trello_card in trello_data: 
        todos.append({"id": trello_card["id"], "status": get_status(trello_card["idList"]), "title": trello_card["name"]})
    print(trello_data)
    return render_template('index.html', items = todos)


def get_status(id):
    query = {
        'key': os.getenv('Trello_API_Key'),
        'token': os.getenv('Trello_API_Token')
        }
        
    status_url = f"https://api.trello.com/1/boards/{os.getenv('Trello_Board_ID')}/lists" #needs to be lists at the end see trello docs
    response=requests.get(
        status_url,
        params=query)
    
    statuses=response.json()
    for card_status in statuses:
        if card_status["id"]==id:
            return card_status["name"]



# add_item(title) — adds a new item with specified title.
@app.route('/additem', methods = ['POST'])
def add_item(): 
    newtodo = request.form.get('newtodo')
    session_items.add_item(newtodo)
    return redirect('/')

#mark an item as completed

#Sort the item list by status ("Not Started", then "Completed")



if __name__ == '__main__':
    app.run()


#Create a new card on the board's 'To Do' list
#Move a card from 'To Do' to 'Done' (or 'Doing' if you want to allow in-progress to-do items)
