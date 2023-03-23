# ใช้สำหรับหาทิศหน้าตรงของถนนแต่ละเส้น

import osmapi
from math import atan2, degrees

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
    line_direction = degrees(atan2(y, x))

    # calculate the direction of the way in the current node based on the direction of the line between the current and next nodes
    print(line_direction);
    if line_direction >= -45 and line_direction < 45:
        node_direction = 'east'
    elif line_direction >= 45 and line_direction < 135:
        node_direction = 'north'
    elif line_direction >= 135 or line_direction < -135:
        node_direction = 'west'
    else:
        node_direction = 'south'
    
    # append the direction of the way in the current node to the list
    way_directions.append(node_direction)

# add the direction of the last node in the way based on the direction of the line between the last two nodes
last_node = api.NodeGet(node_ids[-1])
second_last_node = api.NodeGet(node_ids[-2])
x = last_node['lon'] - second_last_node['lon']
y = last_node['lat'] - second_last_node['lat']
line_direction = degrees(atan2(y, x))
if line_direction >= -45 and line_direction < 45:
    node_direction = 'east'
elif line_direction >= 45 and line_direction < 135:
    node_direction = 'north'
elif line_direction >= 135 or line_direction < -135:
    node_direction = 'west'
else:
    node_direction = 'south'
way_directions.append(node_direction)

# print the list of directions of the way in each node
print(way_directions)
