
import requests
import bs4
import json
from datetime import datetime


def get_atp_dates(save_file=None):
	date_list = []

	response = requests.get('http://www.atpworldtour.com/en/rankings/singles')
	soup = bs4.BeautifulSoup(response.text)

	path = soup.select('#filterHolder > div > div > div')
	path = path[0]
	path = path.select('div > ul > li')

	for li in path:
		if (li.attrs.get('class')[0] != "dropdown-default-label"):
			my_date = li.get_text().strip()
			date_list.append(my_date)

	date_list.sort(key=lambda x: datetime.strptime(x, '%Y.%m.%d'), reverse=True)

	# store to json file
	if (save_file):
		with open(save_file, 'w') as fp:
			json.dump(date_list, fp)

	return date_list


# v_date: format is yyyy-mm-dd (2000-01-10)
def get_atp_ranking(v_date):
	data = []

	response = requests.get('http://www.atpworldtour.com/en/rankings/singles?rankDate='+v_date+'&rankRange=0-10')
	soup = bs4.BeautifulSoup(response.text)

	tr_list = soup.select('#rankingDetailAjaxContainer > table > tbody > tr')

	for tr in tr_list:
		country = tr.select('td.country-cell > div > div > img')[0].attrs.get('alt')
		player = tr.select('td.player-cell > a')[0].get_text()
		score = int(tr.select('td.points-cell > a')[0].get_text().replace(",",""))

		# print(country,player,score)

		data.append({'key': player, 'country': country, 'player': player, 'score': score})

	return data



def get_history_atp_rankings(since="2000-01-01", date_file=None, save_file=None):
	pass


if __name__ == '__main__':

	get_atp_dates('date.json')

	# get_atp_ranking('2000-01-10')