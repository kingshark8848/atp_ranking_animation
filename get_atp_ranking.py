
import requests
import bs4

# v_date: format is yyyy-mm-dd (2000-01-10)
def get_atp_data(v_date):
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

	print(data)


if __name__ == '__main__':
	get_atp_data('2000-01-10')