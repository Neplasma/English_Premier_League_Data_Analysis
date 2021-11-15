#! pyhton 3
# Webscraper for English Premier League Data
from bs4 import BeautifulSoup as soup
import requests

main_url = 'https://fbref.com'
user_agent_headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}
league_url = 'https://fbref.com/en/comps/9/Premier-League-Stats'

f = open('Player_Stats.csv', 'w', encoding='utf-8') # open file

def team_scraper(league_url): # get the url link for each PL team
    page = requests.get(league_url, headers = user_agent_headers)
    page_soup = soup(page.content,'html.parser')

    # containers = page_soup.find_all('th',{'data-stat':'squad'}) 
    containers = page_soup.find(id='stats_squads_standard_for') 
    teams = containers.find_all('a') # find all teams 

    # csv header
    headers = 'name, team, nationality, position, age, games, games_starts, minutes, minutes_90s, goals, assists, goals_pens, pens_made, pens_att, cards_yellow, cards_red, goals_per90, assists_per90, goals_assists_per90, goals_pens_per90, goals_assists_pens_per90, xg, npxg, xa, npxg_xa, xg_per90, xg_xa_per90, npxg_per90, npxg_xa_per90\n'

    f.write(headers)

    for idx, team in enumerate(teams):
        team_name = team.text
        team_url = main_url + team['href']

        print('Team',idx+1)
        print(team_name)
        print(team_url)

        player_scraper(team_name, team_url)

        print('-' *40)
    
    f.close()
    print('Scraping Done!\n')

def player_scraper(team_name, team_url):
    page = requests.get(team_url, headers = user_agent_headers)
    page_soup = soup(page.content,'html.parser')

    containers = page_soup.find('tbody')
    players = containers.find_all('tr') # find all players

    for idx, player in enumerate(players):
        player_name = player.th.text
        player_url = main_url + player.th.a['href']
        nationality = player.find('td',{'data-stat':'nationality'}).text[-3:]
        position = player.find('td',{'data-stat':'position'}).text.replace(',',' ')
        age = player.find('td',{'data-stat':'age'}).text
        games = player.find('td',{'data-stat':'games'}).text
        games_starts = player.find('td',{'data-stat':'games_starts'}).text
        minutes = player.find('td',{'data-stat':'minutes'}).text
        minutes_90s = player.find('td',{'data-stat':'minutes_90s'}).text
        goals = player.find('td',{'data-stat':'goals'}).text
        assists = player.find('td',{'data-stat':'assists'}).text
        goals_pens = player.find('td',{'data-stat':'goals_pens'}).text
        pens_made = player.find('td',{'data-stat':'pens_made'}).text
        pens_att = player.find('td',{'data-stat':'pens_att'}).text
        cards_yellow = player.find('td',{'data-stat':'cards_yellow'}).text
        cards_red = player.find('td',{'data-stat':'cards_red'}).text
        goals_per90 = player.find('td',{'data-stat':'goals_per90'}).text
        assists_per90 = player.find('td',{'data-stat':'assists_per90'}).text
        goals_assists_per90 = player.find('td',{'data-stat':'goals_assists_per90'}).text
        goals_pens_per90 = player.find('td',{'data-stat':'goals_pens_per90'}).text
        goals_assists_pens_per90 = player.find('td',{'data-stat':'goals_assists_pens_per90'}).text
        xg = player.find('td',{'data-stat':'xg'}).text
        npxg = player.find('td',{'data-stat':'npxg'}).text
        xa = player.find('td',{'data-stat':'xa'}).text
        npxg_xa = player.find('td',{'data-stat':'npxg_xa'}).text
        xg_per90 = player.find('td',{'data-stat':'xg_per90'}).text
        xg_xa_per90 = player.find('td',{'data-stat':'xg_xa_per90'}).text
        npxg_per90 = player.find('td',{'data-stat':'npxg_per90'}).text
        npxg_xa_per90 = player.find('td',{'data-stat':'npxg_xa_per90'}).text

        f.write(player_name + ',' + team_name + ',' + nationality + ',' + position + ',' + age + ',' + games + ',' + games_starts + ',' +  minutes + ',' +  minutes_90s + ',' +  goals + ',' +  assists + ',' +  goals_pens + ',' +  pens_made + ',' +  pens_att + ',' +  cards_yellow + ',' +  cards_red + ',' +  goals_per90 + ',' +  assists_per90 + ',' +  goals_assists_per90 + ',' +  goals_pens_per90 + ',' +  goals_assists_pens_per90 + ',' +  xg + ',' +  npxg + ',' +  xa + ',' +  npxg_xa + ',' +  xg_per90 + ',' +  xg_xa_per90 + ',' +  npxg_per90 + ',' +  npxg_xa_per90 + '\n')
        
        print('Player',idx+1)
        print(player_name)
        #print(player_url)

team_scraper(league_url)
