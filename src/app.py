"""
Main application entry point for Clock of Clocks.
"""

import pygame
import sys
from config import (
    FRAME_WIDTH, FRAME_HEIGHT, RADIUS, GAP, LINE_WIDTH,
    BLACK, GREEN, TARGET_FPS
)
from clock_renderer import ClockRenderer
from time_handler import get_current_time


class ClockApp:
    """Main application class for Clock of Clocks."""
    
    def __init__(self):
        """Initialize the clock application."""
        pygame.init()
        
        self.screen = pygame.display.set_mode(
            (FRAME_WIDTH, FRAME_HEIGHT),
            pygame.RESIZABLE | pygame.SCALED
        )
        pygame.display.set_caption("Clock of Clocks")
        
        self.clock = pygame.time.Clock()
        self.renderer = ClockRenderer(
            radius=RADIUS,
            gap=GAP,
            line_width=LINE_WIDTH,
            colour=GREEN
        )
        
        # Calculate starting positions
        self._calculate_start_positions()
        
        self.running = True
    
    def _calculate_start_positions(self):
        """Calculate the starting x and y positions for rendering."""
        # Calculate offset to center the time display
        total_width = (26 * 2 * RADIUS) + (25 * GAP)
        total_height = (6 * 2 * RADIUS) + (5 * GAP)
        
        self.start_x = (FRAME_WIDTH - total_width) // 2 + RADIUS
        self.start_y = (FRAME_HEIGHT - total_height) // 2 + RADIUS
    
    def _handle_events(self):
        """Handle pygame events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.VIDEORESIZE:
                # Handle window resize if needed
                pass
    
    def _update(self):
        """Update application state."""
        pass
    
    def _render(self):
        """Render the current frame."""
        self.screen.fill(BLACK)
        
        # Get current time
        hour, minute, second = get_current_time()
        
        # Draw the time display
        self.renderer.draw_time(
            self.screen,
            BLACK,  # Colour for circle outlines
            hour,
            minute,
            second,
            self.start_x,
            self.start_y
        )
        
        pygame.display.flip()
        self.clock.tick(TARGET_FPS)
    
    def run(self):
        """Main application loop."""
        while self.running:
            self._handle_events()
            self._update()
            self._render()
    
    def quit(self):
        """Clean up and exit the application."""
        pygame.quit()
        sys.exit()


def main():
    """Entry point for the application."""
    app = ClockApp()
    try:
        app.run()
    except KeyboardInterrupt:
        print("\nClosing Clock of Clocks...")
    finally:
        app.quit()


if __name__ == "__main__":
    main()