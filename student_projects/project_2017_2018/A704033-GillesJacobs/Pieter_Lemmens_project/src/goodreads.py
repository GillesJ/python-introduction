import xml.etree.ElementTree as ET
import requests
import urllib
import re
from bs4 import BeautifulSoup

# Goodreads developer API key and base URL to work with
key = "IVCgRv1t2PrUS43xfHaaNQ"
base_url = "https://www.goodreads.com/"


def main():
	# Setting up user input and query dictionary
	query = input("Please enter an author name or book title: ")
	query_data = {'key': key, "q": query}

	# GET request and parsing the XML response
	search_xml_response = api_call("search", query_data)
	work = parse_search_result(search_xml_response)
	parse_work(work)


def api_call(function, query_data):
	# Forming the right URL for the GET request given an input string
	query_enc = urllib.parse.urlencode(query_data) # Helps with formatting the URL properly to make the request
	print(base_url + str(function) + ".xml?" + str(query_enc))
	# Making the actual request
	response = requests.get(base_url + str(function) + ".xml?" + str(query_enc))
	# Confirming success of request or alerting the user that the request was invalid
	if response.status_code == 200:
		print("Request sucessful! Returning results...")
		return response.content
	else:
		print("Invalid request, status code: " + str(response.status_code))


def parse_xml(xml):
	# Parsing the XML query response from a string directly into Element (root element/tag is the <GoodReadsResponse> tag in this case)
	root = ET.fromstring(xml)
	return root


def parse_search_result(xml):
	# Parsing the XML query response (the search results)
	root = parse_xml(xml)
	search_node = root.find("search")
	results_node = search_node.find("results")  
	work_nodes = results_node.findall("work")  # findall because will almost certainly always be multiple

	# Multiple "works" in the response, prompt the user to pick one
	if len(work_nodes) > 1:
		works_dict = {}
		for work in work_nodes:
			# Each work has a unique ID we can fetch
			work_id = work.find("id").text
			book_title = work.find("best_book").find("title").text
			print(str(work_id) + " --> " + book_title)
			# Adding the work IDs to the dictionary while in this for loop
			works_dict[str(work_id)] = work

		user_choice = input("Copy the ID of the book you wish to select: ")
		# Checking if the user choice of ID is actually a possible choice
		if user_choice in works_dict.keys():
			print('Checking work ID...')
			return works_dict[str(user_choice)]
		elif user_choice not in works_dict.keys():
			print('Please check the ID you have entered is correct... Try again.')
	else:
		return work_nodes[0]


def parse_work(work):
	# Parsing the XML for a specific work
	title = work.find("best_book").find("title").text
	author = work.find("best_book").find("author").find("name").text
	id = work.find("best_book").find("id").text

	print(id)

	# Getting the reviews
	query_data = {'key': key}
	book_xml = api_call("book/show/" + str(id), query_data)
	root = parse_xml(book_xml)
	book = root.find("book")
	review_data = (book.find("reviews_widget")).text

	# Regular expression to filter the review data
	regex = r"src=([^\s]+)"
	match = re.search(regex, str(review_data))

	# Forming the correct URL to make the request for the page that contains the review text
	reviews_url = match.group(1).replace('"', '')
	response = requests.get(reviews_url)
	reviews = parse_reviews(response.content)

	for item in reviews:
		print(item)

def parse_reviews(html):
	# Creating an empty list to store the reviews in
	reviews_list = []
	# Using Bs4 to find and select the right containers for the review text
	soup = BeautifulSoup(html,"lxml")
	reviews_container = soup.find("div", {"class": "gr_reviews_container"})
	review_divs = reviews_container.findAll("div", {"class": "gr_review_container"})

	# Looping over all <div> elements that contain review (and more) and adding them to the list
	for div in review_divs: 
		review_by = div.find("span", {"class": "gr_review_by"}).text
		rating = div.find("span", {"class": "gr_rating"}).text
		review_date = div.find("span", {"class": "gr_review_date"}).text
		text = div.find("div", {"class": "gr_review_text"}).text
		reviews_list.append(text)

	return reviews_list

# To make sure the program can run as a standalone script
if __name__ == "__main__":		
	main()