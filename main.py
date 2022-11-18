from event import Event
#from location_events import LocationEvents
#from time import sleep
#from location_events import LocationEvents
#from sense_hat import SenseHat

# class TestEvents:
#     pass

# def __inti__(self):
#     self.sense = SenseHat()
#     self.sense.clear()
    
#     self.location_events = LocationEvents('Kitchen')
    
#     # self all reversed
#     # self all green
#     # self.blank

# TO DO instantiate 2 events from the class passing the required arguments
 

    #TO DO - print the events 
    
    # TO - DO update the location 


    # TO DO - print new location and events

if __name__ == '__main__':

    # instantiate room events
    event1 = Event ('Lounge Room') 
    event2 = Event ('Kitchen')
    event3 = Event ('Living Room')
    
    # display info to console using self event method
    print(f'Event 1: {event1.location}')
    print(f'Event 2: {event2.location}')
    print(f'Event 3: {event3.location}')
    print(f'Humidity: {event1.humidity}')
    
    # using getters and setters
    print(event1.get_location()) # get the event 1 location
    event1.set_location('Toilet') # set a new location
    print(event1.get_location()) # print the new location of event 1
