


import pygame
import random
from algo import get_var_1, give_answer
clock = pygame.time.Clock()

win_counter = 0 
difficulty = 0

pygame.init()
pygame.mixer.init()
Screen_W, Screen_H = 1280, 720

screen = pygame.display.set_mode((Screen_W, Screen_H))

other_text_font = pygame.font.Font('font/Pixeltype.ttf',150)
question_text = pygame.font.Font('font/Pixeltype.ttf',80)

answer = False

victory_sound = pygame.mixer.Sound("goody.mp3")
loss_sound = pygame.mixer.Sound("bad.mp3")

class Combat():
    def __init__(self, BG, sigma, Q, A1, A2, A3, corA): #BG file, Sprite LIST, Question, Answers, correct answer
        self.sigma = sigma
        self.Q = Q
        self.A1 = A1
        self.A2 = A2
        self.A3 = A3
        self.BG = BG
        self.corA = corA

        self.buttons = 'menu'
        self.click = 0
#--------------------------------------------------------------------------------------


        self.BG_load = pygame.image.load(self.BG)
        self.BG_load = pygame.transform.scale(self.BG_load,(Screen_W, Screen_H))
        screen.blit(self.BG_load,(0,0))
      
        #mouse and buttons

        self.cursor = pygame.image.load('GUI/cursor.png')
        self.mouse_pos = pygame.mouse.get_pos()
        self.mouse_rect = pygame.Rect(0, 0, 25, 25)
        self.cursor = pygame.transform.scale(self.cursor, (50,75))

#------------------------------------------------------------------------------------
        #rect buttons
        self.x1, self.y1 = 1300, 100
        self.endx1, self.endy1 = 950, 100
        self.col1 = ('#b38570')
        self.button1_rect = pygame.Rect(self.x1, self.y1, 150, 150)

        self.x2, self.y2 = 1300, 300
        self.endx2, self.endy2 = 950, 300
        self.col2 = ('#b38570')
        self.button2_rect = pygame.Rect(self.x2, self.y2, 150, 150)

        self.x3, self.y3 = 1300, 500
        self.endx3, self.endy3 = 950, 500
        self.col3 = ('#b38570')
        self.button3_rect = pygame.Rect(self.x3, self.y3, 150, 150)
        
        self.col4 = ('#b38570')
        self.button4_rect = pygame.Rect((Screen_W/2)-150, 450, 350, 100)

        self.counter = 0
    def menu(self):
        global game
        self.menuscreen = pygame.image.load('images/menu.jpg')
        self.menuscreen = pygame.transform.scale(self.menuscreen,(Screen_W, Screen_H))
        screen.blit(self.menuscreen,(0,0))
        #pygame.draw.rect(screen, self.col4, self.button4_rect)

        self.menu_text = question_text.render('Sigma math tutoring', False, (0,0,0))
        self.menu_rect = self.menu_text.get_rect(center = (640,100))
        screen.blit(self.menu_text, self.menu_rect)

        self.start_text = question_text.render('Start', False, (0,0,0))
        self.start_text_rect = self.start_text.get_rect(center = (640,500))
        self.bg_rect = self.start_text_rect.inflate(400,70)
        pygame.draw.rect(screen, self.col4, self.bg_rect)

        screen.blit(self.start_text, self.start_text_rect)

        self.mouse_pos = pygame.mouse.get_pos()
        self.mouse_rect.center = self.mouse_pos

        if event.type == pygame.MOUSEBUTTONUP:
            self.click += 1
        #play button
        if self.mouse_rect.colliderect(self.button4_rect):
            self.col4 = ('#d49c83')
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.col4 = ('#f0cdbd')
                self.click = 0
            elif self.click == 1:
                
                game = True
        else: 
            self.col4 = ('#b38570')


        pygame.mouse.set_visible(False)
        screen.blit(self.cursor, self.mouse_rect)


    def enter_combat(self):
        global win_counter,difficulty, x, y , corA , l, A1, A2 ,A3 , sigma_faces, p1
        screen.blit(self.BG_load,(0,0))
        
        
        #buttons
        self.mouse_pos = pygame.mouse.get_pos()
        self.mouse_rect.center = self.mouse_pos

        if event.type == pygame.MOUSEBUTTONUP:
            self.click += 1

        if self.counter >= 1:
            self.counter -= 1
            print(self.counter)
        
        self.delay = 100
        self.sigma_text = question_text.render('Sigma', False, (0,0,0))
        screen.blit(self.sigma_text, (50,50))

        self.win_count_text = question_text.render(f'Points: {win_counter}', False, (0,0,0))
        screen.blit(self.win_count_text, (50,150))

#-----------------------------------------------------------------------------
                #Action Select
        if self.buttons == 'menu':
            pygame.draw.rect(screen, self.col1, self.button1_rect)
            pygame.draw.rect(screen, self.col2, self.button2_rect)
            pygame.draw.rect(screen, self.col3, self.button3_rect)

            if self.x1 != self.endx1:
                self.x1 -=25
                self.x2 -=25
                self.x3 -=25
            self.button1_rect = pygame.Rect(self.x1, self.y1, 250, 150)
            self.button2_rect = pygame.Rect(self.x2, self.y2, 250, 150)
            self.button3_rect = pygame.Rect(self.x3, self.y3, 250, 150)

            self.question = question_text.render(self.Q, False, (0,0,0))
            screen.blit(self.question, (50,100))

            self.sigma_load = pygame.image.load(self.sigma[0])
            #self.sigma_load = pygame.transform.scale(self.sigma_load,(100,250))
            screen.blit(self.sigma_load,(0,300))

            

                                                                    #A1 BUTTON
            if self.mouse_rect.colliderect(self.button1_rect):
                self.col1 = ('#d49c83')
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.col1 = ('#f0cdbd')
                    self.click = 0
                elif self.click == 1:
                    self.answer = self.A1
                    self.counter = self.delay
                    self.buttons = 'reaction to answer'
            else: 
                self.col1 = ('#b38570')
                                                                    #A2 BUTTON
            if self.mouse_rect.colliderect(self.button2_rect):
                self.col2 = ('#d49c83')
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.col2 = ('#f0cdbd')
                    self.click = 0
                elif self.click == 1:
                    self.answer = self.A2
                    self.counter = self.delay
                    self.buttons = 'reaction to answer'
            else: 
                self.col2 = ('#b38570')
                                                                    #A3 BUTTON
            if self.mouse_rect.colliderect(self.button3_rect):
                self.col3 = ('#d49c83')
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.col3 = ('#f0cdbd')
                    self.click = 0
                elif self.click == 1:
                    self.answer = self.A3
                    self.counter = self.delay
                    self.buttons = 'reaction to answer'
            else: 
                self.col3 = ('#b38570')
            self.a1_text = other_text_font.render(f'{self.A1}', False, (0,0,0))
            screen.blit(self.a1_text, (self.x1+40,self.y1+50))

            self.a2_text = other_text_font.render(f'{self.A2}', False, (0,0,0))
            screen.blit(self.a2_text, (self.x2+40,self.y2+50))

            self.a3_text = other_text_font.render(f'{self.A3}', False, (0,0,0))
            screen.blit(self.a3_text, (self.x3+40, self.y3+50))

            
#--------------------------------------------------------------------------------------------------------

        if self.buttons == 'reaction to answer':
            
            
            if self.answer != self.corA:
                self.sigma_load = pygame.image.load(self.sigma[1])
                #self.sigma_load = pygame.transform.scale(self.sigma_load,(100,250))
                screen.blit(self.sigma_load,(0,300))
                print("Loss")
                if self.counter == self.delay:
                    loss_sound.play(0)

                self.question = question_text.render('You are a failure..', False, (0,0,0))
                screen.blit(self.question, (50,100))
            elif self.answer == self.corA:
                self.sigma_load = pygame.image.load(self.sigma[0])
                #self.sigma_load = pygame.transform.scale(self.sigma_load,(100,250))
                screen.blit(self.sigma_load,(0,300))
                if self.counter == self.delay:
                    victory_sound.play(0)
                    win_counter +=1
                    if win_counter % 5 == 0:
                        self.text = 'Time to make it more difficult..'
                        difficulty += 10
                    else:
                        self.text = 'You are amazing!!'
                self.question = question_text.render(self.text, False, (0,0,0))

                screen.blit(self.question, (50,100))

            #self.question = question_text.render(self.Q, False, (255,255,255))
            #screen.blit(self.question, (750,Screen_H-200))
            #print(self.answer)
            if self.counter == 0:
                
             
                x, y , corA , l = get_var_1(1,10 + difficulty)

                answers = give_answer(corA,20 + difficulty)
                A1, A2 , A3 = answers[0], answers[1], answers[2]
                Q = f"Answer this youngin : {x} {l} {y} = ?"
                sigma_faces = ['images/sigma.png','images/made_guy.png']
                ##BG file, Sprite LIST, Question, Answers, correct answer
                p1 = Combat('images/backy.jpg', sigma_faces, Q, A1, A2, A3, corA)
                self.buttons = 'menu'

            #self.buttons = 'menu'


#----------------------------------------------------------------------------------------------------------------
        pygame.mouse.set_visible(False)
        screen.blit(self.cursor, self.mouse_rect)







game = False


x, y , corA , l = get_var_1(1,10)

answers = give_answer(corA,20)
A1, A2 , A3 = answers[0], answers[1], answers[2]
Q = f"Answer this youngin : {x} {l} {y} = ?"
sigma_faces = ['images/sigma.png','images/made_guy.png']
##BG file, Sprite LIST, Question, Answers, correct answer
p1 = Combat('images/backy.jpg', sigma_faces, Q, A1, A2, A3, corA)


background_music = pygame.mixer.Sound("music/bee.mp3")
background_music.play(-1)
running = True

pygame.display.toggle_fullscreen()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    if game: p1.enter_combat()
    else: p1.menu()
    clock.tick(60)
    pygame.display.update()
pygame.quit()




"""

Ans = 0
question_counter = 0


when button clicked
    if button is button 1 :
        if button 1 == correct answer:
            happy sigma
        else:
            sigma mad
        question_counter +=1 # increments difficulty / questions





"""