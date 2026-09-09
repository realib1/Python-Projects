"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes:
        (class) total_aliens_created (int): Total number of Alien instances.
        x_coordinate (int): Position on the x-axis.
        y_coordinate (int): Position on the y-axis.
        health (int): Number of health points.

    Methods:
        hit(): Decrement Alien health by one point.
        is_alive(): Return a boolean for if Alien is alive (if health is > 0).
        teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
        collision_detection(other): Implementation TBD.

    """

    total_aliens_created = 0

    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = 3
        
        Alien.total_aliens_created += 1

    def hit(self):
        self.health -= 1

    def is_alive(self):
        if (self.health <= 0):
            return False
        return True

    def teleport(self, new_x_coordinate, new_y_coordinate):
        self.x_coordinate = new_x_coordinate
        self.y_coordinate = new_y_coordinate
        
    def collision_detection(self, other):
        pass
        
        
# TODO (Student): Create the new_aliens_collection() function below to call your Alien class with a list of coordinates


def new_aliens_collection(positions):
    return [Alien(x_coordinate, y_coordinate) for x_coordinate, y_coordinate in positions]


alien = Alien(2, 4)
alien.hit()
alien.is_alive()
alien.collision_detection(alien)
alien.teleport(5, -4)
alien.total_aliens_created

aliens = new_aliens_collection([(-2, 6), (1, 5), (-4, -3)])

print(aliens)
