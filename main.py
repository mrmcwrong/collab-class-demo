from vpython import * #import vpython library

class Bunny:
    def __init__(self):
        #sphere for face
        f = sphere()
        f.radius = 3
        self.furcolor = vector (188/255, 143/255, 108/255)
        f.color = self.furcolor
        self.face = f
        #list of spheres for ears
        #list of spheres for eyes
        self.eyes = []
        for i in range(2):
            eye = sphere()
            eye.radius = 0.5
            eye.pos.y += 1
            if i == 0:
                eye.pos.x -= 1
            else:
                eye.pos.x = i
            eye.pos.z = 3
            eye.color = color.black
            self.eyes.append(eye)
        self.ears = []
        for i in range(2):
            ear = sphere()
            ear.radius = 1.5
            ear.pos.y += 3
            if i == 0:
                ear.pos.x -= 1.25
            else:
                ear.pos.x = 1.25
            ear.pos.z = 0
            ear.color = self.furcolor
            self.ears.append(ear)
    def blinkEyes(self,f):
        if f%10 == 0: #check if 10 frames elapsed
            for eye in self.eyes:
                if eye.color == self.furcolor:
                    eye.color = color.black
                else:
                    eye.color = self.furcolor

#Brennen's method
#blink's eyes


t = Bunny()
frames = 0
while True:
    rate(10)
    t.blinkEyes(frames)
    frames += 1