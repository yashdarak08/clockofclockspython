"""
Clock of Clocks - A Python implementation of the Clock of Clocks concept.
"""

__version__ = "1.0.0"
__author__ = "Yash Darak"

from clock_renderer import ClockRenderer
from time_handler import get_current_time, format_time
from digit_data import DIGITS, ROTATION

__all__ = [
    "ClockRenderer",
    "get_current_time",
    "format_time",
    "DIGITS",
    "ROTATION",
]