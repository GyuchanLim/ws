#allows connection to web requests
import requests
#allows copying files and directories
import shutil
#allows creation and deletion of a directory
import os
#allows easy web-scraping tools
from bs4 import BeautifulSoup

def project():
	url = 'https://www.seek.co.nz'


	#x = requests.get('https://pypi.org/project/requests/')
	x = requests.get(url)
	textify = x.text

	soup = BeautifulSoup(textify, "html.parser")
	print(soup.prettify())

def practice():

	url = 'https://books.toscrape.com'

	#Pre-defining all lists
	images_list = []
	books_list = []

	x = requests.get(url)
	textify = x.text

	#Store html as text
	soup = BeautifulSoup(textify, 'html.parser')

	'''
	#Find all links by searching for a
	count=0
	for link in soup.find_all('a'):
		print(link.get('href'))
		if count >= 4:
			count = 0
			break
		count+=1
	'''

	#Save the directory for all the thumbnail images
	for li in soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3"):
		for img in li.find_all('img', class_= "thumbnail"):
			images_list.append(url+'/'+img['src'])
	while(True):
		ans = input("Would you like to save images? (Y/N)")
		if ans.lower() in ('y','n'):
			if ans.lower() == 'y':
				save_images(images_list)
			break
		else:
			print("Please answer in Y/N")

#Save the images from the links stored in 'image_url'
def save_images(images_list):
	os.chdir('/home/kanga/Documents/python/WebImages')
	count=0
	for image in images_list:
		res = requests.get(image, stream=True)
		#image_url = url+'/'+image
		#res = requests.get(image_url, stream = True)
		if res.status_code == 200:
			print("Image found, saving image "+str(count+1))
			file_name = 'Image'+str(count)
			with open(file_name,'wb') as f:
				shutil.copyfileobj(res.raw, f)
		else:
			print("Image not found, skipped ...")
			continue
		count+=1

#Testing user input
while True:
	ans = input("Is this practice? (Y/N)")
	if ans.lower() == 'y':
		practice()
		break
	elif ans.lower()=='n':
		project()
		break
	print("Please answer either Y or N")
#This is a test
