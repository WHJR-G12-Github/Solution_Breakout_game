import pygame
pygame.init()
 
WHITE = (255,255,255)
DARKBLUE = (36,90,190)
LIGHTBLUE = (0,176,240)
RED = (255,0,0)
GREEN = (0, 255, 0)

bricks1=[]
bricks2=[]
bricks3=[]

# Using 'for' loop, appending 6 bricks to 'bricks1' list at 'y=60'
for i in range(6):
    bricks1.append(pygame.Rect(10 + i* 100,60,80,30))
  
# Using 'for' loop, append 6 bricks to 'bricks2' list at 'y=100'
for i in range(6):
    bricks2.append(pygame.Rect(10 + i* 100,100,80,30))
  
# Using 'for' loop, append 6 bricks to 'bricks3' list at 'y=140'
for i in range(6):
    bricks3.append(pygame.Rect(10 + i* 100,140,80,30))
  
# Creating a function to draw the bricks in 'RED' color
def draw_brick(brick_list):
    for i in brick_list:
        # Drawing the brick 'i' on the 'screen' in 'RED' color
        pygame.draw.rect(screen,RED,i)
     
# Creating a variable 'score' and initializing to zero
score = 0

velocity=[1,1]
size = (600, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout Game")
paddle=pygame.Rect(300,550,60,10) #(x,y,width,height)
ball=pygame.Rect(200,250,10,10)
carryOn = True
while carryOn:
    for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                  carryOn = False # Flag that we are done so we exit this loop             
    screen.fill(DARKBLUE)
    pygame.draw.rect(screen,LIGHTBLUE,paddle)
    font = pygame.font.Font(None, 34)
    text = font.render("Score: " + str(score), 1, WHITE)
    screen.blit(text, (20,10))
    #paddle movement
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            if paddle.x<540: 
                paddle.x+=5
        if event.key == pygame.K_LEFT:
            if paddle.x>0:
                paddle.x-=5
    
    # Drawing the bricks on the screen by calling the 'draw_brick()' function
    # Calling the function for every brick list created  
    draw_brick(bricks1)
    draw_brick(bricks2)
    draw_brick(bricks3)
    
    
    #ball movement    
    ball.x+=velocity[0]
    ball.y+=velocity[1]  
    
    if ball.x>=590 or ball.x<=0:
        velocity[0] = -velocity[0]
    if ball.y<=38  :
        velocity[1] = -velocity[1]
    if paddle.collidepoint(ball.x,ball.y):
         velocity[1]=-velocity[1]
    if ball.y>=590:
        font = pygame.font.Font(None, 74)
        text = font.render("GAME OVER", 1, RED)
        screen.blit(text, (150,350))
        pygame.display.flip()
        pygame.time.wait(2000)
        break
    pygame.draw.rect(screen,WHITE ,ball)
    
    # Scoring for each brick layer
    for i in bricks1:
        if i.collidepoint(ball.x,ball.y):
            # Removing the brick 'i' from 'bricks1' list
            bricks1.remove(i)
            velocity[0] = -velocity[0]
            velocity[1]=-velocity[1]
            # Incrementing the value of 'score' by 3
            score+=3
            
    for i in bricks2:
        if i.collidepoint(ball.x,ball.y):
            # Removing the brick 'i' from 'bricks2' list
            bricks2.remove(i)
            velocity[0] = -velocity[0]
            velocity[1]=-velocity[1]
            # Incrementing the value of 'score' by 2
            score+=2
            
    for i in bricks3:
        if i.collidepoint(ball.x,ball.y):
            # Removing the brick 'i' from 'bricks3' list
            bricks3.remove(i)
            velocity[0] = -velocity[0]
            velocity[1]=-velocity[1]
            # Incrementing the value of 'score' by 1
            score+=1
            
    # Maximum score on breaking all the bricks would be 36
    # Breaking the first row bricks [1 point * 6 bricks = 6 points]
    # Breaking the second row bricks [2 points * 6 bricks = 12 points]
    # Breaking the third row bricks [3 points * 6 bricks = 18 points]
    # Maximum score = 6+12+18 = 36 points
    # Checking if score equals 36             
    if score==36:
        font = pygame.font.Font(None, 74)
      
        # Creating the text to be displayed "YOU WON!!" using 'font.render()' function       
        text = font.render("YOU WON!!", 1, RED)
        
        # Displaying 'text' on the screen using 'screen.blit()' at the location (150,350)
        screen.blit(text, (150,350))
        
        pygame.display.flip()
        pygame.time.wait(2000)
        break
    pygame.time.wait(1)
    pygame.display.flip()       
pygame.quit(  )
