import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to set the volume level
def set_volume(level):
    """Set the volume level (0.0 to 1.0)."""
    if 0.0 <= level <= 1.0:
        engine.setProperty('volume', level)
        return f"Volume set to {level * 100:.0f}%."
    else:
        return "Volume level must be between 0 and 1."

# Function to get the current volume level
def get_volume():
    """Get the current volume level."""
    return engine.getProperty('volume')

# Function to increase the volume
def increase_volume(increment=0.1):
    """Increase the volume by the specified increment."""
    current_volume = get_volume()
    new_volume = min(current_volume + increment, 1.0)  # Cap at 1.0
    set_volume(new_volume)
    return f"Volume increased to {new_volume * 100:.0f}%."

# Function to decrease the volume
def decrease_volume(decrement=0.1):
    """Decrease the volume by the specified decrement."""
    current_volume = get_volume()
    new_volume = max(current_volume - decrement, 0.0)  # Floor at 0.0
    set_volume(new_volume)
    return f"Volume decreased to {new_volume * 100:.0f}%."

# Function to mute the volume
def mute_volume():
    """Mute the volume."""
    set_volume(0.0)
    return "Volume muted."

# Function to unmute the volume
def unmute_volume(previous_volume):
    """Unmute the volume and restore the previous volume level."""
    set_volume(previous_volume)
    return f"Volume restored to {previous_volume * 100:.0f}%."
