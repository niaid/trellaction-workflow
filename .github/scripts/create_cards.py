import os
from trello import TrelloClient
import json

client = TrelloClient(
    api_key=os.getenv("TRELLO_API_KEY"),
    api_secret=os.getenv("TRELLO_API_SECRET"),
    token=os.getenv("TRELLO_TOKEN"),
    token_secret=os.getenv("TRELLO_TOKEN_SECRET")
)

board_id = os.getenv('TRELLO_BOARD_ID')
list_index = os.getenv('TRELLO_LIST_INDEX') - 1
github_event = os.getenv('GITHUB_EVENT_PATH')
with open(github_event, "r") as event_file:
    event = json.load(event_file)

issue = event["issue"]
if "security" in [label["name"] for label in issue["labels"]]:
    board = client.get_board(board_id)
    list = board.list_lists()[list_index]  # assuming you want the first list
    card = list.add_card(issue["title"], desc=issue["body"])