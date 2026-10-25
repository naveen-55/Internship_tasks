#The Captain's Room
#https://www.hackerrank.com/challenges/py-the-captains-room/problem

k = int(input())
room_numbers = list(map(int, input().split()))

# Find the room number that appears only once
room_count = {}
for room in room_numbers:
    room_count[room] = room_count.get(room, 0) + 1

captain_room = None
for room, count in room_count.items():
    if count == 1:
        captain_room = room
        break

print(captain_room)
