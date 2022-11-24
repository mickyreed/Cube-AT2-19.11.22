import time
from happy import Happy
from sad import Sad
from happy import Happy
from angry import Angry

# Create a happy smiley, which is a subclass of Smiley
smiles = Happy()
frowny = Sad()
anger = Angry()

anger.show()
time.sleep(12)
# This is a form of #polymorphis, as the Happy smiley class
# does not have a method called .show(). This means that
# the method .show() of the base class {Smiley} will be
# used in stead. There is no need to specify the base
# class, like in other, statically typed, languages.
smiles.show()

# Just a short delay
time.sleep(1)

# Another form of polymorphism:
# The method blink is implemented by the Happy class, but
# is defined as an interface (i.e., an abtract base class
# with an abstract method).
smiles.blink()
time.sleep(3)

frowny.show()
time.sleep(1)
frowny.blink()

