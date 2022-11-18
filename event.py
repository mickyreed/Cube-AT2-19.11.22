# All refernces to the sense hat removed for developing on any system.  
# you will need to add the sense hat to get values and collect events

from time import sleep
from datetime import datetime

class Event:
	def __init__(self, location, presence = False, temperature = 0, humidity = 0):
		"""
		Event class to indicate if someone is in a room

		param location:
		param presence:
		param temperature:
		param humidity:
  
		"""
		self.location = location
		self.presence = presence
		self.temperature = temperature
		self.humidity = humidity
		self.timestamp = datetime.now()
		self.linked_rooms = {}
		self.person = None
	
	def link_room(self, room_to_link, direction):
		self.linked_rooms[direction] = room_to_link

	def get_location(self):
		return self.location
	
	def describe_location(self):
		print(f'You are in the: {self.location}')

	def set_location(self, location):
		self.location = location
	
	def set_timestamp(self, timestamp):
		self.timestamp = timestamp
	
	def get_timestamp(self):
		return self.timestamp 

	def set_person(self, new_person):
		self.person = new_person
	
	def get_person(self):
		return self.person 
	
	def move(self, direction):
		if direction in self.linked_rooms:
			return self.linked_rooms[direction]
		else:
			print("You can't go that way")
			return self

	def get_details(self):
		for direction in self.linked_rooms:
			room = self.linked_rooms[direction]
			#print( "The " + room.get_location() + " is " + direction)
			print(f"The {room.get_location()} is {direction}")
	
	def __str__(self):
		return f'location {self.location},\ntimestamp {self.timestamp},\npresence {self.presence},\ntemparature {self.temparture},\nhumidity {self.humidity}\n'

if __name__ == '__main__':
	event1 = Event ('Kitchen')
	event2 = Event ('Living Room')
	event3 = Event ('Lounge Room')
	
	event1.link_room(event2, "east")
	event2.link_room(event1, "west")
	event2.link_room(event3, "east")
	event3.link_room(event2, "west")

	game_state = {"room_index" : 0}

	
	# display info to console using self event method
	# print(f'Event 1: {event1.location}')
	# print(f'Event 2: {event2.location}')
	# print(f'Event 3: {event3.location}')
	# print(f'Humidity {event1.location}: {event1.humidity}')

	# print(f'Event 1: {event1.location}, user presence = {event1.presence}')  
	# event1.presence = True # change presence user enters Lounge Room
	# print(f'Event 1: {event1.location}, user presence = {event1.presence}')

	# event1.get_details()
	# event2.get_details()

	current_room = event1
	from person import Person
	dave = Person("Dave", "A smelly zombie")
	# dave.describe()
	event2.set_person(dave)
	current_room = event1
	event1.presence = True

	while True:
		print("\n")
		current_room.describe_location()
		current_room.set_timestamp(datetime.now())
		print(f'{current_room.location} presence = {current_room.presence} at {current_room.timestamp}')
		current_room.get_details()
		
		#print(f'Event 1: {event1.location}, user presence = {event1.presence}')  
		command = input("> ")
		
		inhabitant = current_room.get_person()
		if inhabitant is not None:
			inhabitant.describe()

		# Add this to terminate the program
		if command == "exit":
			break
		
		current_room.presence = False	
		current_room = current_room.move(command)
		current_room.presence = True
		print(f'Kitchen presence = {event1.presence}')
		print(f'Living Presece = {event2.presence}')
		print(f'Lounge Presence = {event3.presence}')
		
		# inhabitant = current_room.get_person()
		# if inhabitant is not None:
		#     inhabitant.describe()

		# using getters and setters
		# print(event1.get_location()) # get the event 1 location
		# event1.set_location('Toilet') # set a new location
		# print(event1.get_location()) # print the new location of event 1

			# if command == "west":
			# 	game_state["room_index"] -= 1
			
			# elif command == "east":
			# 	game_state["room_index"] += 1

		#if inhabitant is not None and isinstance(inhabitant, Enemy):
		#current_room.set_character(None)


		# self.timestamp = datetime.now()