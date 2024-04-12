import pygame  

pygame.init()


WIDTH = 800
HEIGHT = 600
colorWHITE = (255, 255, 255)


screen = pygame.display.set_mode((WIDTH, HEIGHT))

base_layer.fill(colorWHITE)
screen.fill(colorWHITE)
pygame.display.set_caption("Paint")

 
clock = pygame.time.Clock()

 
LMBpressed = False
THICKNESS = 5  

 
currX = 0
currY = 0

prevX = 0
prevY = 0

 
mode = "rectangle"
color_mode = "red"   

 
def calculate_rect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

 
def calculate_equilateral_triangle(x1, y1, x2, y2):
    side_length = abs(x2 - x1)  
    height = int(side_length * (3 ** 0.5) / 2)  
    return ((x1, y1), ((x1 + x2) // 2, y1 - height), (x2, y1))   

def draw_rhombus(screen, color, rect):
    points = [rect.midtop, rect.midright, rect.midbottom, rect.midleft]
    pygame.draw.polygon(screen, color, points,THICKNESS)  

 
done = False

 
while not done:

     
    pressed = pygame.key.get_pressed()
    shift_held = pressed[pygame.K_LSHIFT] or pressed[pygame.K_RSHIFT]

    for event in pygame.event.get():
        if LMBpressed:
            screen.blit(base_layer, (0, 0))  
        if event.type == pygame.QUIT:
            done = True   

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
             
            LMBpressed = True
            prevX = event.pos[0]
            prevY = event.pos[1]

        if event.type == pygame.MOUSEMOTION:
            if LMBpressed:
                 
                currX = event.pos[0]
                currY = event.pos[1]

                
                if mode == "rectangle":
                    pygame.draw.rect(screen, color_mode, calculate_rect(prevX, prevY, currX, currY), THICKNESS)
                elif mode == "circle":
                    pygame.draw.circle(screen, color_mode, (prevX, prevY), abs(currX - prevX), THICKNESS)
                elif mode == "righttriangle":
                    pygame.draw.polygon(screen, color_mode, ((prevX, prevY), (prevX, currY), (currX, currY)), THICKNESS)
                elif mode == "triangle":
                    pygame.draw.polygon(screen, color_mode, calculate_equilateral_triangle(prevX, prevY, currX, currY), THICKNESS)
                elif mode == "rhombus":
                    rect1 = calculate_rect(prevX, prevY, currX, currY)
                    draw_rhombus(screen, color_mode, rect1)
                elif mode == "sguare":
                     
                    top_left = (min(prevX, currX), min(prevY, currY))
                    side_length = min(abs(currX - prevX), abs(currY - prevY))
                     
                    pygame.draw.rect(screen, color_mode, (top_left[0], top_left[1], side_length, side_length), THICKNESS)
                elif mode == "eraser":
                    pygame.draw.circle(screen, (255, 255, 255), (currX, currY), THICKNESS)
                    base_layer.blit(screen, (0, 0))   

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            
            LMBpressed = False
            currX = event.pos[0]
            currY = event.pos[1]

            
            if mode == "rectangle":
                pygame.draw.rect(screen, color_mode, calculate_rect(prevX, prevY, currX, currY), THICKNESS)
                base_layer.blit(screen, (0, 0))   
            elif mode == "circle":
                pygame.draw.circle(screen, color_mode, (prevX, prevY), abs(currX - prevX), THICKNESS) 
            elif mode == "righttriangle": 
                base_layer.blit(screen, (0, 0))  
                pygame.draw.polygon(screen, color_mode, ((prevX, prevY), (prevX, currY), (currX, currY)), THICKNESS)
                base_layer.blit(screen, (0, 0))  
            elif mode == "triangle":
                pygame.draw.polygon(screen, color_mode, calculate_equilateral_triangle(prevX, prevY, currX, currY), THICKNESS)
                base_layer.blit(screen, (0, 0)) 
            elif mode == "rhombus":
                rect1 = calculate_rect(prevX, prevY, currX, currY)
                draw_rhombus(screen, color_mode, rect1)
                base_layer.blit(screen, (0, 0))
            elif mode == "sguare":
                а
                top_left = (min(prevX, currX), min(prevY, currY))
                side_length = min(abs(currX - prevX), abs(currY - prevY))
               
                pygame.draw.rect(screen, color_mode, (top_left[0], top_left[1], side_length, side_length), THICKNESS)
                base_layer.blit(screen, (0, 0)) 


        if event.type == pygame.KEYDOWN:
            
            
            if event.key == pygame.K_ESCAPE:
                done = True  

            
            if event.key == pygame.K_c:
                mode = "circle"
            if event.key == pygame.K_r:
                mode = "rectangle"
            if event.key == pygame.K_t:
                mode = "righttriangle"
            if event.key == pygame.K_v:
                mode = "triangle"
            if event.key == pygame.K_h:
                mode = "rhombus"
            if event.key == pygame.K_e:
                mode = "eraser"
            if event.key == pygame.K_s:
                mode = "sguare"

            
            if event.key == pygame.K_r and shift_held:
                color_mode = "red"
            if event.key == pygame.K_b and shift_held:
                color_mode = "blue"
            if event.key == pygame.K_g and shift_held:
                color_mode = "green"
            if event.key == pygame.K_k and shift_held:
                color_mode = "black"
            

    pygame.display.flip()   
    clock.tick(10000000)   