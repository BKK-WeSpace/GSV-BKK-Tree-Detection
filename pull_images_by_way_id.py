import osmapi
from math import atan2, degrees
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2

# create an instance of the osmapi.Api class
api = osmapi.OsmApi()

# specify the ID of the way you want to get the direction of
way_id = 123

# get the details of the way, including its nodes
way = api.WayGet(way_id)

# get the IDs of the nodes in the way
node_ids = way['nd']

# initialize an empty list to store the directions of the way in each node
way_directions = []

# iterate over the nodes in the way, except the last one
for i in range(len(node_ids)-1):
    # get the details of the current and next nodes
    current_node = api.NodeGet(node_ids[i])
    next_node = api.NodeGet(node_ids[i+1])

    # calculate the direction of the line between the current and next nodes using atan2 function
    x = next_node['lon'] - current_node['lon']
    y = next_node['lat'] - current_node['lat']
    ahead = degrees(atan2(y, x))

    lat = current_node['lat']
    lng = current_node['lon']
    api_key = "GSM_API_KEY"
    location = f"{lat},{lng}" # latitude,longitude
    url = f"https://maps.googleapis.com/maps/api/streetview?size=600x300&head={ahead}&location={location}&key={api_key}"
    response = urllib2.urlopen(url)
	
    filename = f"{location}.jpg"
    with open(filename, "wb") as f:
        f.write(response.read())
        print(f"Image saved as {filename}")

