import random
class aa:
    def sortear(Canvas1,img1,img2,img3):
        valor=random.randint(1,3)
        if valor==1:
            Canvas1.create_image(50,100,image=img1,anchor="nw")
        elif valor==2:
            Canvas1.create_image(50,100,image=img2,anchor="nw")
        elif valor==3:
            Canvas1.create_image(50,100,image=img3,anchor="nw")