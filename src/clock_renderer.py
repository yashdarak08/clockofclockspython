"""
Clock rendering logic for Clock of Clocks.
"""

import pygame
import math
from digit_data import DIGITS, ROTATION


class ClockRenderer:
    """Handles rendering of the clock display."""
    
    def __init__(self, radius, gap, line_width, colour=None):
        """
        Initialize the clock renderer.
        
        Args:
            radius (int): Radius of each individual clock face
            gap (int): Gap between clock faces
            line_width (int): Width of the clock hand lines
            colour (tuple): RGB colour tuple for the clock hands
        """
        self.radius = radius
        self.gap = gap
        self.line_width = line_width
        self.colour = colour or (0, 255, 0)  # Default to green
        self._calculate_positions()
    
    def _calculate_positions(self):
        """Calculate spacing positions for digit groups."""
        # temp1: spacing for single digits within a group (4 clocks wide)
        # temp2: spacing between digit groups (5 clocks wide)
        self.temp1 = (4 * 2 * self.radius) + (4 * self.gap)
        self.temp2 = (5 * 2 * self.radius) + (5 * self.gap)
    
    def draw_digit(self, screen, num, colour, x, y):
        """
        Draw a single digit made of 24 clock faces (6 rows x 4 columns).
        
        Args:
            screen: Pygame surface to draw on
            num (str): The digit character to draw ('0'-'9')
            colour (tuple): RGB colour for clock outlines
            x (int): Starting x position
            y (int): Starting y position
        """
        if num not in DIGITS:
            raise ValueError(f"Invalid digit: {num}")
        
        segments = DIGITS[num]
        
        for i in range(24):
            row = i // 4
            col = i % 4
            cx = x + col * (2 * self.radius + self.gap)
            cy = y + row * (2 * self.radius + self.gap)
            
            # Draw the circle outline
            pygame.draw.circle(screen, colour, (cx, cy), self.radius, 1)
            
            # Get the symbol and its rotation angles
            symbol = segments[i]
            angles = ROTATION.get(symbol, [135, 135])
            
            # Draw first hand
            hand1_x = cx + self.radius * math.cos(math.radians(angles[0]))
            hand1_y = cy + self.radius * math.sin(math.radians(angles[0]))
            pygame.draw.line(screen, self.colour, (cx, cy), 
                           (hand1_x, hand1_y), width=self.line_width)
            
            # Draw second hand
            hand2_x = cx + self.radius * math.cos(math.radians(angles[1]))
            hand2_y = cy + self.radius * math.sin(math.radians(angles[1]))
            pygame.draw.line(screen, self.colour, (cx, cy), 
                           (hand2_x, hand2_y), width=self.line_width)
    
    def draw_time(self, screen, colour, hour, minute, second, start_x, start_y):
        """
        Draw the complete time display (HH:MM:SS).
        
        Args:
            screen: Pygame surface to draw on
            colour (tuple): RGB colour for circle outlines
            hour (str): Hour in HH format
            minute (str): Minute in MM format
            second (str): Second in SS format
            start_x (int): Starting x position
            start_y (int): Starting y position
        """
        x = start_x
        
        # Hour digits
        self.draw_digit(screen, hour[0], colour, x, start_y)
        x += self.temp1
        
        self.draw_digit(screen, hour[1], colour, x, start_y)
        x += self.temp2
        
        # Minute digits
        self.draw_digit(screen, minute[0], colour, x, start_y)
        x += self.temp1
        
        self.draw_digit(screen, minute[1], colour, x, start_y)
        x += self.temp2
        
        # Second digits
        self.draw_digit(screen, second[0], colour, x, start_y)
        x += self.temp1
        
        self.draw_digit(screen, second[1], colour, x, start_y)