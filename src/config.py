"""
Global configuration for Clock of Clocks application.
"""

# Display settings
FRAME_WIDTH = 1024
FRAME_HEIGHT = 300
RADIUS = FRAME_WIDTH // 64
GAP = RADIUS // 8
LINE_WIDTH = 2

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
GRAY = (100, 100, 100)

# FPS settings
TARGET_FPS = 60
UPDATE_INTERVAL_MS = 1000  # Update every 1 second