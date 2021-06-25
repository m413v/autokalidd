#!/usr/bin/python

from bs4 import BeautifulSoup
import requests
import threading
from pathlib import Path
base_url = "https://cdimage.kali.org/current/"

page = requests.get(base_url)
kali = BeautifulSoup(page.content, "html.parser")

download_threads = list()

def download(url, filename):
	print("Downloading %s"%url)
	response = requests.get(url, stream = True)
	text_file = open(filename,"wb")
	for chunk in response.iter_content(chunk_size=1024):
		text_file.write(chunk)
	text_file.close()



for a in kali.find_all('a', href=True):
	if "SHA256SUMS" in a['href']:
		filename = a['href']
		download(base_url+filename, filename)
	if "amd64" in a['href']:
		if "installer" in a['href'] or "live" in a['href']:
			image = a['href']
			iso = Path("./"+image)
			if not iso.is_file():
    			# file exists
				print("Found the URL: %s, added to thread list. "%image)
				x = threading.Thread(target=download, args=(base_url+image, image,))
				download_threads.append(x)
				x.start()
			else:
				print("%s exists in current dir, skipping."%image)