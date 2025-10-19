import pygame
import sys
import math
import digit
from datetime import datetime as dt

frame_width = 1024
frame_heigth = 300
radius = frame_width // 64
gap = radius // 8
w = 1
start_x = ( frame_width - (26 * 2 * radius) - (25 * gap) ) // 2 + radius
start_y = ( frame_heigth - (6 * 2 * radius) - (5 * gap) ) // 2 + radius
temp1 = (4 * 2 * radius) + (4 * gap)
temp2 = (5 * 2 * radius) + (5 * gap)

GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)

def draw_digit(screen, num ,colour, x, y, r, w=2):
    for i in range(24):
        row = i // 4
        col = i % 4
        cx = x + col * (2 * r + gap)
        cy = y + row * (2 * r + gap)
        pygame.draw.circle(screen, colour, (cx, cy), r, w)

        symbol = digit.digits[num][i]
        angles = digit.rotation[symbol]
        hand1_x = cx + r * math.cos(math.radians(angles[0]))
        hand1_y = cy + r * math.sin(math.radians(angles[0]))
        pygame.draw.line(screen, GREEN, (cx, cy), (hand1_x, hand1_y), width=2)

        hand2_x = cx + r * math.cos(math.radians(angles[1]))
        hand2_y = cy + r * math.sin(math.radians(angles[1]))
        pygame.draw.line(screen, GREEN, (cx, cy), (hand2_x, hand2_y), width=2)

def draw(screen, colour, hour, minute, second, start_x, start_y, radius):

    #First Hour Digit
    draw_digit(screen, hour[0], colour, start_x, start_y, radius)
    #Second Hour Digit 
    start_x += temp1
    draw_digit(screen, hour[1], colour, start_x, start_y, radius)
    # draw_digit(1)

    #First Minute Digit
    start_x += temp2
    draw_digit(screen, minute[0], colour, start_x, start_y, radius)
    #Second Minute Digit 
    start_x += temp1
    draw_digit(screen, minute[1], colour, start_x, start_y, radius)

    #First Seconds Digit
    start_x += temp2
    draw_digit(screen, second[0], colour, start_x, start_y, radius)
    #Second Seconds Digit
    start_x += temp1
    draw_digit(screen, second[1], colour, start_x, start_y, radius)

pygame.init()
screen = pygame.display.set_mode((frame_width, frame_heigth), pygame.RESIZABLE, pygame.SCALED)
pygame.display.set_caption("Clock of Clocks")
clock = pygame.time.Clock()
running = True
last_update_time = pygame.time.get_ticks()  # Track time in milliseconds


if __name__ == "__main__":
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Get current time
        current_time = pygame.time.get_ticks()
        
        # Update animation only if 1 second (1000ms) has passed
        if current_time - last_update_time >= 1000:
            last_update_time = current_time  # Reset timer
        
        # Draw (this happens every frame for smooth visuals)
        screen.fill(BLACK)
        now = dt.now()
        hour = str(now.hour).zfill(2)
        minute = str(now.minute).zfill(2)
        second = str(now.second).zfill(2)
        draw(screen, BLACK, hour, minute, second, start_x, start_y, radius)

        pygame.display.flip()
        clock.tick(60)  # Still run at 60 FPS for smooth display

pygame.quit()
sys.exit()
