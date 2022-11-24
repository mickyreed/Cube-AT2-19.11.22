#import types
#from attr import attributes
from event import Event


class LocationEvents:
    '''
    Record events in a room/location and places them in an list
    When you instantiate this object, you must pass in a location,
    which will be stored as an instance variable. 
    You must also create an empty list of potential events as an instance variable. 
    Write the __init__ method so that these requirements are met. 
    '''

    def __init__(self, location, presence= False ): #TO DO atributes to be passed

#TO DO define atributes

        # self.atribute1 = atribute1 
        # self.atribute1 = atribute1
        self.location = location
        self.presence = presence

    def add_event(self): #TO DO - inheritance):
        pass
# TO DO create the setter.
    def enter_room(self, location, presence):

        if something happened
            self.set the attributes for the data types eg bool
            return True
        else:
            return False

# TO DO create a human readable string

    def __str__(self):
        return f"location: {self. #TO DO define location atribute}"









class LocationEvents:
	def __init__(self, location, presence = False, temperature = 0, humidity = 0):
		
		"""
			Event class to indicate if someone is in a room

			param location:
		param presence:
		param temperature:
		paam humidity:

		"""
		self.location = location
		# self.timestamp = datetime.now()
		self.presence = presence

	def enter_room(self, location, presence):
	# self.health = self.health - damage
	# print(“Health: %i” % (self.health))

    # def speak(self):
    #     print(“%s says…” % (self.name))
    #     print(self.speech)

# displays the letters of the direction on the sensehat when joystick or arrow keys used 
from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

e = (0, 0, 0)
w = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)

game_state = {"room_index" : 0} # pulled from trinket rock scissor paper

sense.clear()
while True:
  for event in sense.stick.get_events():
    # Check if the joystick was pressed
    if event.action == "pressed":
      
      # Check which direction
      if event.direction == "up":
        sense.show_letter("U", back_colour = red)      # Up arrow
        print(event.direction, event.action)
      elif event.direction == "down":
        sense.show_letter("D", back_colour = red)      # Down arrow
        print(event.direction, event.action)
      elif event.direction == "left":
        game_state["room_index"] -= 1
        #display(game_state)
        print(game_state)
        sense.show_letter("L", back_colour = green)      # Left arrow
        print(event.direction, event.action)
        temp = sense.temp
        print(temp)
        humidity = sense.humidityLocation
        print(humidity)
        pressure = sense.pressure
        print(pressure)
      elif event.direction == "right":
        game_state["room_index"] += 1
        #display(game_state)
        print(game_state)
        sense.show_letter("R", back_colour = blue)      # Right arrow
        print(event.direction, event.action)
      elif event.direction == "middle":
        sense.show_letter("M", back_colour = white)      # Enter key
        print(event.direction, event.action)
      
      # Wait a while and then clear the screen
      sleep(0.5)
      sense.clear()
    
