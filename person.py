class Person():

    # Create a character
    def __init__(self, person_name, person_description):
        self.name = person_name
        self.description = person_description
        self.conversation = None

    # Describe this character
    def describe(self):
        print( self.name + " is here!" )
        print( self.description )

    # # Set what this character will say when talked to
    # def set_conversation(self, conversation):
    #     self.conversation = conversation

    # # Talk to this character
    # def talk(self):
    #     if self.conversation is not None:
    #         print("[" + self.name + " says]: " + self.conversation)
    #     else:
    #         print(self.name + " doesn't want to talk to you")

    # # Fight with this character
    # def fight(self, combat_item):
    #     print(self.name + " doesn't want to fight with you")
    #     return True