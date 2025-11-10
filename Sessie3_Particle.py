class Particle:
    def __init__(self, name, spin):
        # make instance attribute from name
        # make instance attribute from spin

        self.name = name
        self.spin = spin

    def is_up_or_down(self):
        #   print up when spin is positive
        #   print down when spin is negative

        if self.spin > 0:
            print("Up")

        if self.spin < 0:
            print("Down")

        if self.spin == 0:
            print("_")

    def flip(self):
        #   make spin positive if spin is negative
        #   make spin negative if spin is positive

        self.spin = self.spin * -1


proton = Particle("mooi proton", 0.5)
proton.is_up_or_down()
proton.flip()
proton.is_up_or_down()
print(f"{proton.spin=}")
print(f"{proton.name=}")
