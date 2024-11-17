class Bullet:
    def __init__(self, canvas, x, y, image, speed, direction, window):
        self.canvas = canvas
        self.image = image
        self.speed = speed
        self.direction = direction
        self.window = window
        self.bullet = self.canvas.create_image(x,y, image = self.image, anchor = 'nw')
        self.active = True
        
    def move(self):
        
        if self.active == True:
            self.canvas.move(self.bullet,0, self.speed * self.direction)
            coords = self.canvas.coords(self.bullet)
            if coords[1] < 0 or coords[1] > self.canvas.winfo_height():
                self.remove()
        
    def remove(self):
        self.canvas.delete(self.bullet)
        self.active = False