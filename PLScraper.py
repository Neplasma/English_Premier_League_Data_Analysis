#! pyhton 3
# Webscraper for English Premier League Data
from bs4 import BeautifulSoup as soup
import requests

main_url = 'https://fbref.com'
user_agent_headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}
league_url = 'https://fbref.com/en/comps/9/Premier-League-Stats'

def team_scraper(league_url): # get the url link for each PL team
    page = requests.get(league_url, headers = user_agent_headers)
    page_soup = soup(page.content,'html.parser')

    #containers = page_soup.find_all('th',{'data-stat':'squad'}) 
    containers = page_soup.find(id='stats_squads_standard_for') 
    teams = containers.find_all('a') # find all teams 

    for idx, team in enumerate(teams):
        team_name = team.text
        team_url = main_url + team['href']

        print('Team',idx+1)
        print(team_name)
        print(team_url)

        player_scraper(team_url)

        print('-' *40)

def player_scraper(team_url):
    page = requests.get(team_url, headers = user_agent_headers)
    page_soup = soup(page.content,'html.parser')

    containers = page_soup.tbody
    players = containers.find_all('th',{'scope':'row'}) # find all players

    for idx, player in enumerate(players):
        player_name = player.a.text
        player_url = main_url + player.a['href']
        print('Player',idx+1)
        print(player_name)
        print(player_url)

team_scraper(league_url)
