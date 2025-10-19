"""
Time handling utilities for Clock of Clocks.
"""

from datetime import datetime

def get_current_time():
    """
    Get the current time formatted as hour, minute, second.
    
    Returns:
        tuple: (hour, minute, second) as zero-padded strings
    """
    now = datetime.now()
    return (
        str(now.hour).zfill(2),
        str(now.minute).zfill(2),
        str(now.second).zfill(2)
    )


def format_time(hour, minute, second):
    """
    Format time components as a readable string.
    
    Args:
        hour (str): Hour in HH format
        minute (str): Minute in MM format
        second (str): Second in SS format
    
    Returns:
        str: Formatted time string "HH:MM:SS"
    """
    return f"{hour}:{minute}:{second}"