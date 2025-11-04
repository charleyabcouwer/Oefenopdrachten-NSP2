# Onderstaande code geeft via een class informatie over de instance (turtle): shape, distance, left

# class Turtle:
#     def __init__(self, shape):
#         print(shape)

#     def forward(self, distance):
#         print(distance)

#     def left(self, angle):
#         print(angle)

# master_oogway = Turtle("turtle")

# # master_oogway.shape()
# master_oogway.left(30)
# master_oogway.forward(50)

class Turtle:
    def __init__(self, shape):
        # transform turtle into shape
        print(shape)

    def forward(self, distance):
        print(distance)

    def left(self, angle):
        # turn turtle counterclockwise
        # by angle in degrees
        print(angle)

    def do_kungfu_move(self):
        # do kungfu move
        self.forward(130)
        self.left(350)
        self.forward(60)
        print(f"{self=}")

    
master_oogway = Turtle("turtle")
print(f"{master_oogway=}")
master_oogway.do_kungfu_move()

toby = Turtle("turtle")
print(f"{toby=}")
toby.do_kungfu_move()

# print(f"{self=}")
# print(f"{master_oogway=}")