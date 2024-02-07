<h1>LightSwitch - Object-Oriented Python Example</h1>

<h2>Description</h2>

The LightSwitch program is a demonstration of Object-Oriented Programming (OOP) principles in Python, as featured in the book "Object-Oriented Python: Master OOP by Building Games and GUIs" by Irv Kalb. This program models a basic light switch, showcasing fundamental OOP concepts such as class creation, object instantiation, and method invocation.

<h2>Features</h2>

LightSwitch Class: Represents a light switch with an internal state that determines whether the switch is on or off.
* `__init__`: Constructor method to initialize the LightSwitch object with the  switch in the off position (switchIsOn = False).
* `turnOn`: Method to set the switchIsOn state to True, simulating the turning on of the light switch.
* `turnOff`: Method to set the switchIsOn state to False, simulating the turning off of the light switch.
* `show`: Method to print the current state of the switch (True for on, False for off).

<h2>Usage</h2>

To use the program, create an instance of the LightSwitch class and invoke its methods to toggle the switch's state and display its current state.

    `if __name__ == "__main__":
        oLightSwitch = LightSwitch() # Object instantiation
        oLightSwitch.show()          # Display initial state (expected to be False)`


<h2>Example</h2>

Here's a simple example of how you can interact with the LightSwitch object:

    `oLightSwitch = LightSwitch() # Creating a LightSwitch object
    oLightSwitch.turnOn()        # Turning on the light switch
    oLightSwitch.show()          # Should display: True
    oLightSwitch.turnOff()       # Turning off the light switch
    oLightSwitch.show()          # Should display: False`

This program is an excellent starting point for beginners in Python to understand the basics of OOP, and how classes and objects can be used to model real-world entities and their behaviors.
