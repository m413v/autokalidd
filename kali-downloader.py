#!/usr/bin/python

from bs4 import BeautifulSoup
import requests
import threading

base_url = "https://cdimage.kali.org/current/"

page = requests.get(base_url)
kali = BeautifulSoup(page.content, "html.parser")

def download_iso(url, filename):
	response = requests.get(url, stream = True)
	text_file = open(filename,"wb")

	for chunk in response.iter_content(chunk_size=1024):
		text_file.write(chunk)
	text_file.close()



for a in kali.find_all('a', href=True):
	if "amd64" in a['href']:
		if "installer" in a['href'] or "live" in a['href']:
			image = a['href']
			print("Found the URL: %s, downloading... "%image)
			download_iso(base_url+image, image)

