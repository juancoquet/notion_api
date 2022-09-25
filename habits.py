import datetime as dt
from dotenv import load_dotenv, find_dotenv
import requests
import os

load_dotenv(find_dotenv())

TOKEN = os.getenv("ACCESS_TOKEN")
HABITS_DB = os.getenv("HABITS_DB")

def create_habit(name, date):
    """Creates a habit page in the habits database.
    Args:
        name (str): Name of the habit.
        date (str): Date of the habit.
    Returns:
        dict: The response from the API.
    """
    url = f'https://api.notion.com/v1/pages'
    headers = {
        'accept': 'application/json',
        'Notion-Version': '2022-06-28',
        'Authorization': f'Bearer {TOKEN}'   
    }
    payload = {
        'parent' : {'database_id' : HABITS_DB},
        'properties' : {
            'Name': {'title': [{'text' : {'content' : name}}]},
            'Date': {'date': {'start' : date,}},
        },
        'icon': {'external': {'url': 'https://www.notion.so/icons/link_gray.svg'}}
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()