from jupyturtle import forward, left, right

def koch(x):
    if x < 5:
        forward(x)  # Draw a straight line if length is less than 5
    else:
        # Recursive case to draw a Koch curve
        koch(x / 3)  # First third
        left(60)  # Turn left by 60 degrees
        koch(x / 3)  # Second third
        right(120)  # Turn right by 120 degrees
        koch(x / 3)  # Third third
        left(60)  # Turn left by 60 degrees

# Example usage:
koch(100)  # Draw a Koch curve with length 100
