# Use https://www.si.umich.edu/programs/bachelor-science-
# information/bsi-admissions as a template.
# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.

# Deliverables
# Make sure the new page is uploaded to your GitHub account.
import requests
from bs4 import BeautifulSoup

print ("\nIbrahim A. Rasheed, BeautifulSoup Project")

base_url = 'http://collemc.people.si.umich.edu/data/bshw3StarterFile.html'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "lxml")

for line in soup.findall(class_="field-item"):
	if line.a == "student":
		lin.a.replace("student", "AMAZING student")
	print (line.a)

print ("Done.")


#f = open("index.html", "w")

#html doc

#f.write(html.doc)