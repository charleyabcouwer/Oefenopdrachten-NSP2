import math
class PointMass:

    def __init__(self, mass, position, velocity):
        self.mass = mass
        self.position = position
        self.velocity = velocity
    
    def update_velocity(self, velocity):
        self.velocity = velocity 

    def update_position_after(self, time):
        position_x = self.position[0]
        position_y = self.position[1]

        velocity_x = self.velocity[0]
        velocity_y = self.velocity[1]

        p_x = position_x + (velocity_x * time)
        p_y = position_y + (velocity_y * time)

        self.position = (p_x, p_y)  #updaten positie

        return p_x, p_y

        

    def get_kinetic_energy(self):

        velocity_x = self.velocity[0]
        velocity_y = self.velocity[1]
        E_kin = 0.5 * self.mass * ((velocity_x ** 2 + velocity_y ** 2))
        return E_kin

    def get_momentum(self):
        velocity_x = self.velocity[0]
        velocity_y = self.velocity[1]
        momentum = self.mass * math.sqrt((velocity_x ** 2 + velocity_y ** 2))
        return momentum


m = PointMass(mass=5.0, position=(1.0, 0.0), velocity=(3.0, 0.0))
print(f"{m.update_position_after(0)=}")
print(f"{m.update_position_after(0.5)=}")
print(f"{m.update_position_after(0.5)=}")

m.update_velocity((0.0, 3.0))
print(f"{m.update_position_after(0.5)=}")
print(f"{m.update_position_after(0.5)=}")

print(f"{m.velocity=}")
print(f"{m.get_momentum()=}")
print(f"{m.get_kinetic_energy()=}")