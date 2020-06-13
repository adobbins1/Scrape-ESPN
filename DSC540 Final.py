# Austin Dobbins
# DSC540
# Final Project
# In this project I will scrape the ESPN website in order collect stats for all pitchers from the 2019 season.
# I will then take that data and put it in a data frame and transform the data to properly describe all stats.

import pandas as pd
from bs4 import BeautifulSoup
import requests
import re

# Grabbing Website Source Code
url = 'http://www.espn.com/mlb/stats/pitching/_/year/2019/seasontype/2'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

# Identify Header Row
header = soup.find('tr', attrs={'class': 'colhead'})

# Get Column Names from the Header
columns = [col.get_text() for col in header.find_all('td')]

# Creating Empty Data Frame
df = pd.DataFrame(columns=columns)
print(df)

# Scraping Player stats
players = soup.find_all('tr', attrs={'class': re.compile('player-10-')})
for player in players:
    stats = [stat.get_text() for stat in player.find_all('td')]
    # Creating temp data frame for stats
    temp = pd.DataFrame(stats).transpose()
    temp.columns = columns
    # Adding to empty data frame
    df = pd.concat([df, temp], ignore_index=True)
print(df)

# Changing the Column Names to Help Understand the Stats
df.columns = ['Rank', 'Player', 'Team', 'Games Played', 'Games Started', 'Innings Pitched', 'Hits', 'Runs',
              'Errors', 'Walks', 'Strikeouts', 'Wins', 'Losses', 'Saves', 'Blown Saves', 'Wins Above Replacement',
              'Walks and Hits/Inning Pitched', 'Earned Run Average']
print(df.columns)
print(df)

# Deleting Rank Column
del df['Rank']
print(df)
