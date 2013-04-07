
import pygame, sys
from pygame.locals import *

class Board:
    '''this is board of lightsoff'''

    level_map = []
    level = 0
    rects = []
    count = 0    
    level_map_source_name = ''
    level_map_string = ''
    
    def __init__(self,file_name):
        print "\t\t\t Hello Dear"
        print "\t for win the game you must do your best to kill"
        print "\t all lights (change them to X)"
        print "\t for reseting the level type 'reset'"
        print "\t for adding a level click on level?"
        #a = str(raw_input("\t you are ready? "))

        self.level_map_source_name = file_name
        self.load_level(file_name)
        self.update_level(0)
                
    def update_board(self, i, j):#cpp
        '''updates the map according to touch'''
        self.rects[i][j] = not self.rects[i][j] 
        if i - 1 >= 0 : self.rects[i - 1][j] = not self.rects[i - 1][j] 
        if i + 1 <= 4 : self.rects[i + 1][j] = not self.rects[i + 1][j] 
        if j - 1 >= 0 : self.rects[i][j - 1] = not self.rects[i][j - 1] 
        if j + 1 <= 4 : self.rects[i][j + 1] = not self.rects[i][j + 1] 

    def update_level(self, level):#cpp
        '''loads level data'''
        self.rects = []
        for i in range(5):
            self.rects.append([])
            for j in range(5):
                self.rects[i].append(self.level_map[level][j][i])
                
    def end_game(self):#cpp
        '''check if the game has finished or not if finished load next level'''
        end = True
        for i in range(5):
            for j in range(5):
                if self.rects[i][j]:
                    end = False
                    break

        if (end and self.level != len(self.level_map)):
            print "--------------- you pass level",self.level + 1 ,"---------------"
            self.level += 1
            sound_level_finish.play()
            pygame.time.delay(200)
            self.update_level(self.level)
            self.show_board()
            return 1
        elif (end and self.level == len(self.level_map)):
            print "WOW you win with ",self.count,"moves"
            return 0
        else:
            return 1

    def end_game_for_level(self):#cpp
        '''check if the level has finished or not'''
        end = True
        for i in range(5):
            for j in range(5):
                if self.rects[i][j]:
                    end = False
                    break

        return 1
    '''
        if (end and self.level != len(level_map)):
            return 1
        else:
            return 0
        '''
    def get_move(self,a):#cpp
        '''set your move in the board by giving 2 strings such as e1 or 5a'''
        if (a == "reset"):
            self.update_level(self.level)
            
        elif (len(a) == 2):
            if ((ord(a[0]) >= ord('a') and ord(a[0]) <= ord('e'))
                and (ord(a[1]) >= ord('1') and ord(a[1]) <= ord('5'))):
                self.update_board(int(ord(a[1]) - ord('1')), int(ord(a[0]) - ord('a')))
                self.count += 1
            elif ((ord(a[1]) >= ord('a') and ord(a[1]) <= ord('e'))
                 and (ord(a[0]) >= ord('1') and ord(a[0]) <= ord('5'))):
                self.update_board(int(ord(a[0]) - ord('1')), int(ord(a[1]) - ord('a')))
                self.count += 1
        else:
            print "unillegal move"
            self.count += 1
            self.show_board()

    def get_move_display(self,a,b):
        '''set the move by giving 2 integers'''
        self.update_board(a,b)
        self.count += 1

    def show_board(self):#cpp
        '''show the board in consol'''
        print "level : ",self.level + 1
        print "   ______________________________ " 
        print "  |  _     _     _     _     _   |"
        for i in range(5):
            print i+1,"|",
            for j in range(5):
                if self.rects[j][i] :
                    print "|O|",
                else:
                    print "|_|",
                if j != 4 :
                    print " ",
                else:
                    print " |"
            if i != 4:
                print "  |  _     _     _     _     _   |"
                
        print "   ------------------------------ \n     A     B     C     D     E   "

    def load_level(self,file_name):
        '''read and load levels from a file'''
        file_temp = open(file_name, 'r')
        temp = file_temp.read()
        file_temp.close()

        file_temp_core = ''
        for i in temp:
            if (i == '1' or i == '0'):
                file_temp_core += i

        for i in range(int(len(file_temp_core)/25)):
            self.level_map.append([])
            for j in range(5):
                self.level_map[i].append([])
                for k in range(5):
                    self.level_map[i][j].append(int(file_temp_core[i*25 + j*5 + k]))

    def save_level(self,rect):
        '''save updates to a file'''
        file_temp = open(self.level_map_source_name,'r')
        self.level_map_string = file_temp.read()
        file_temp.close()

        level_temp = ''
        level_temp += "{"
        for i in range(5):
            level_temp += "{"
            for j in range(5):
                if rect[i][j] == 1:
                    level_temp += '1'
                else:
                    level_temp += '0'
                if j != 4:
                    level_temp += ","
            level_temp += "},"
            level_temp += "\n"
        level_temp += "}"
        
        self.level_map_string += "\n"
        self.level_map_string += level_temp

        file_temp = open(self.level_map_source_name,'w')
        file_temp.write(self.level_map_string)
        file_temp.close()
       
    def append_level(self):
        '''appending a level'''
        self.save_level(self.rects)
        self.level_map.append(self.rects)

    def reset(self):
        '''reseting the game'''
        self.update_level(0)
        self.count = 0
        
    def get_board(self):
        return self.rects

    def get_level(self):
        return self.level

    def show_lamp(self,display,rects,size):
        mysize = size[0]/5
        for i in range(5):
            for j in range(5):
                if rects[i][j]:
                    display.blit(on, (mysize*i, mysize*j))
                else:
                    display.blit(off, (mysize*i, mysize*j))


b = Board('data_main\level_map_source.txt')#the argument is level_map, called from a text file
b.show_board()

size_screen = x, y = (400,440)
pygame.init()
d = pygame.display.set_mode(size_screen)
bgcolor = (60, 60, 100)

on2 = pygame.image.load('data_main\on2.png')
on2 = pygame.transform.scale(on2, (size_screen[0]/5,size_screen[0]/5))
on = pygame.image.load('data_main\on.png')
on = pygame.transform.scale(on, (size_screen[0]/5,size_screen[0]/5))
off = pygame.image.load('data_main\off.png')
off = pygame.transform.scale(off, (size_screen[0]/5,size_screen[0]/5))

sound_level_finish = pygame.mixer.Sound("data_main\levelfinish.wav")
sound_click = pygame.mixer.Sound("data_main\click.wav")

text = pygame.font.Font('data_main\\f.ttf',size_screen[0]/19)

level_text = []
for i in range(1,20):
    level_text.append(text.render('add level | level    ' + str(i), True, [0,0,0]))

reset_bottun = pygame.font.Font('data_main\\f.ttf',size_screen[0]/19).render('reset game   reset level', True, [0,250,0])

loop = True
while loop:
    while b.end_game() or loop:
        d.fill(bgcolor)
        b.show_lamp(d, b.get_board(),size_screen)
        
        pygame.draw.rect(d,[0,25,250],[5,size_screen[0] + 5,size_screen[0]/2 - 7,size_screen[1]-size_screen[0] - 10], 5)#for level show
        pygame.draw.rect(d,[0,250,0],[size_screen[0]/2 + 7,size_screen[0] + 5,size_screen[0]/2 - 12,size_screen[1]-size_screen[0] - 10], 5)#reset_bottun
        pygame.draw.line(d,[0,255,0],[size_screen[0]*3/4 + 5,size_screen[0] + 5],[size_screen[0]*3/4 + 5,size_screen[1]-5],5)#for deviding the resets bottuns
        
        d.blit(reset_bottun,[size_screen[0]/2 + 14,size_screen[0] + 6])#reset bottuns text
        d.blit(level_text[b.get_level()],[size_screen[0]/16,size_screen[0] + 9])#for level show
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == MOUSEBUTTONDOWN:
                x, y = event.pos
                sound_click.play()
                if x > 0 and x < size_screen[0] and y > 0 and y < size_screen[0]:#for lamps
                    b.get_move_display(int(x/(size_screen[0]/5.0)), int(y/(size_screen[0]/5)))
                    b.show_board()
                elif x > size_screen[0]*3/4 + 5 and x < size_screen[0] and y > size_screen[0] + 5 and y < size_screen[1]:#for reset level bottun
                    b.get_move('reset')
                    b.show_board()
                elif x > size_screen[0]/2 + 5 and x < size_screen[0]*3/4 and y > size_screen[0] + 5 and y < size_screen[1]:#for reset bottun
                    b.reset()
                    b.show_board()
                    print "reseting"
                elif x < size_screen[0]/2 and x > 0 and y > size_screen[0] + 5 and y < size_screen[1]:#for add level
                    b.append_level()
                    b.show_board()

        pygame.display.update()
        loop = False
        
    pygame.quit()
    
pygame.quit()


''' 
while (b.end_game(1,1)):
    b.show_board()
    move = str(raw_input("your move : "))
    b.get_move(move)
    #b.show_board()
'''
