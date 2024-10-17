# This is to introduce my favorite animal
I = "My favorite animal is a finger monkey."
print(I)

# This is for the favorite animal class
class FA:
    # Data members and initializing
    def __init__(self, arm_length, leg_length, num_eyes, has_tail, is_furry):
        self.arm_length = arm_length
        self.leg_length = leg_length
        self.num_eyes = num_eyes
        self.has_tail = has_tail
        self.is_furry = is_furry

    # Describing the data members
    def describe(self):
        print("Physical Characteristics:")
        print(f"Length of arms: {self.arm_length} inches")
        print(f"Length of legs: {self.leg_length} inches")
        print(f"Number of eyes: {self.num_eyes}")
        print(f"Has a tail: {'Yes' if self.has_tail else 'No'}")
        print(f"Is furry: {'Yes' if self.is_furry else 'No'}")

# Create an instance of the FA class
myfavoriteanimal = FA(1.5, 2.2, 2, True, True)

# Call the describe method
myfavoriteanimal.describe()