from pygame import *
font.init()
font=font.SysFont('Arial',35)
window=display.set_mode((1000,700))
display.set_caption('pin-pong')
fon=transform.scale(image.load('fon.jpg'),(1000,700))
class zxc(sprite.Sprite):
    def __init__(self, pi_image, pi_x, pi_y, size_x, size_y, pi_step):
        super().__init__()
        self.image=transform.scale(image.load(pi_image),(size_x,size_y))
        self.rect=self.image.get_rect()
        self.rect.x=pi_x
        self.rect.y=pi_y
        self.step=pi_step
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Hero(zxc):
    def control_1(self):
        knopochki=key.get_pressed()
        if knopochki[K_w] and self.rect.y>5:
            self.rect.y-=self.step
        if knopochki[K_s] and self.rect.y<600:
            self.rect.y+=self.step
    def control_2(self):
        knopochki=key.get_pressed()
        if knopochki[K_UP] and self.rect.y>5:
            self.rect.y-=self.step
        if knopochki[K_DOWN] and self.rect.y<600:
            self.rect.y+=self.step
game=True
finish=False
clock=time.Clock()
pl1=Hero('roketka.jpg',20,300,10,100,15)
pl2=Hero('roketka.jpg',970,300,10,100,15)
ball=Hero('ball.jpg',500,300,40,50,0)
lose_1=font.render('Проиграл первый игрок',True,(255,255,255))
lose_2=font.render('Проиграл второй игрок',True,(255,255,255))
ball_speed_x=6
ball_speed_y=6
while game:
    for e in event.get():
        if e.type==QUIT:
            game=False
    if finish!=True:
        window.blit(fon,(0,0))
        pl1.reset()
        pl2.reset()
        ball.reset()
        pl1.control_1()
        pl2.control_2()
        ball.rect.x+=ball_speed_x
        ball.rect.y-=ball_speed_y
        if ball.rect.y<0 or ball.rect.y>650:
            ball_speed_y*=-1
        if ball.rect.x<0:
            finish=True
            window.blit(lose_1,(400,300))
        if ball.rect.x>1000:
            finish=True
            window.blit(lose_2,(400,300))
        if sprite.collide_rect(pl1,ball)or sprite.collide_rect(pl2,ball):
            ball_speed_y*=1
            ball_speed_x*=-1
        display.update()
    clock.tick(60)