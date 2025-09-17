#List concept - Ordered based on index, mutable

playlist = ["Shape of you","Naa ready","Tum hi ho"]
fav_foods = ["Pizza","dosa","idli"]
recent_loc = ["Home","Airport","Work","Mall"]
'''
#list methods

playlist.append("Unai kaanadha")
print("Spotify Playlist -  After append", playlist)

playlist.insert(2,"munbe va")
print("Spotify Playlist -  After insert , 2nd index", playlist)

playlist.remove("Naa ready")
print("Spotify Playlist -  After remove , naa ready", playlist)

playlist.pop()
print("Spotify Playlist -  After pop", playlist)

playlist.reverse()
print("Spotify Playlist -  After reverse", playlist)

print(playlist.count("munbe va")) # find the position of the item
'''
#LIST SLICING
# Top 2 songs
print(playlist[0:2])
print(recent_loc[-2:])
print(playlist[1:2])

# List Iteration
for food in fav_foods:
    print("All food",food)

for i,loca in enumerate(recent_loc):
    print(f"{i} : {loca}")
