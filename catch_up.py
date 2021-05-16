from pygame import *
window = display.set_mode((700, 500))
display.set_caption("Догонялки")
background = transform.scale(image.load("background.png"), (700, 500))
sprite1 = transform.scale(image.load('sprite1.png'),(100, 100))
sprite2 = transform.scale(image.load('sprite2.png'),(100, 100))
clock = time.Clock()
FPS = 60
x1,y1 = 100, 100
x2,y2 = 300, 300
speed = 10
game = True
while game:
    window.blit(background,(0, 0))
    window.blit(sprite1,(x1, y1))
    window.blit(sprite2,(x2, y2))
    for e in event.get():
        if e.type == QUIT:
            game = False
    clock.tick(FPS)
    keys_pressed = key.get_pressed()

    if keys_pressed[K_a] and x1 > 5:
        x1 -= speed

    if keys_pressed[K_d] and x1 < 595:
        x1 += speed

    if keys_pressed[K_w] and y1 > 5:
        y1 -= speed
    
    if keys_pressed[K_s] and y1 < 395:
        y1 += speed


        
    display.update()