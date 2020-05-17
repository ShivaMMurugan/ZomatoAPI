# importing pyzomato module

# requirement > pip install pyzomato


# checkout geocode endpoint, very useful one to find restaurent id.

# expore latitue and longitude for your city.

import os
from pyzomato import Pyzomato

''' There is so much we can do with this API, there are 17 endpoints
 we can configure and use however we want, I just used few to see what's
 available in this api.'''

class ZomotoAPI:


	def __init__(self):

		# Api secret keys stored in enviornment variable

		self.api_key = os.environ.get('api_key')

	def get_Categories(self, citi_id):

		self.api_client_auth = Pyzomato(self.api_key)

		self.api_client_auth.search(name="Chennai")

		# city id for chennai is 7

		return self.api_client_auth.getCategories()


	def search_city_by_geo_code(self, latitude, longitude):


		return self.api_client_auth.getByGeocode(latitude, longitude)

		


	def locating_res_by_id(self, res_id):


		# id > 18387708 
		# name > kakada ramprasad
		# "locality_verbose": "Kilpauk, Chennai"

		return self.api_client_auth.getRestaurantDetails(res_id)




def main():

	zomoto = ZomotoAPI()

	get_categories = zomoto.get_Categories(7)

	search_city = zomoto.search_city_by_geo_code('13.067439', '80.237617')

	locate = zomoto.locating_res_by_id('18387708')

	print(get_categories)
	print(search_city)
	print(locate)

if __name__ == '__main__':

	main()


