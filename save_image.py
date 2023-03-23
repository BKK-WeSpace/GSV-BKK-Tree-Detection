try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
import json

api_key = "GSM_API"
location = "40.720032,-73.988354"  # latitude,longitude

url = f"https://maps.googleapis.com/maps/api/streetview?size=600x300&location={location}&key={api_key}"
response = urllib2.urlopen(url)
# data = json.loads(response.read().decode('utf-8'))
print(response)

filename = f"{location}.jpg"
with open(filename, "wb") as f:
	f.write(response.read())
	print(f"Image saved as {filename}")
