# Problem Statement
# Implement an 'eraser' on a canvas.
# The canvas consists of a grid of blue 'cells' which are drawn as rectangles on the screen. We then create an eraser rectangle which, when dragged around the canvas, sets all of the rectangles it is in contact with to white.

# Solution
from graphics import GraphWin, Rectangle, Point
import time

CANVAS_WIDTH: int = 400
CANVAS_HEIGHT: int = 400

CELL_SIZE: int = 40
ERASER_SIZE: int = 30

def erase_objects(window, eraser):
    """Erase objects in contact with the eraser"""
    # Get mouse info to help us know which cells to delete
    mouse_x = window.getMouse().getX()
    mouse_y = window.getMouse().getY()
    
    # Calculate where our eraser is
    left_x = mouse_x
    top_y = mouse_y
    right_x = left_x + ERASER_SIZE
    bottom_y = top_y + ERASER_SIZE
    
    # Find things that overlap with our eraser
    overlapping_objects = []  # Need custom logic for detecting overlapping (this is just a placeholder)
    
    # For everything that overlaps with our eraser (that isn't our eraser), change
    # its color to white
    for overlapping_object in overlapping_objects:
        if overlapping_object != eraser:
            overlapping_object.setFill('white')

def main():
    win = GraphWin("Canvas", CANVAS_WIDTH, CANVAS_HEIGHT)

    num_rows = CANVAS_HEIGHT // CELL_SIZE  # Figure out how many rows of cells we need
    num_cols = CANVAS_WIDTH // CELL_SIZE   # Figure out how many columns of cells we need
    
    # Make a grid of squares based on the number of rows and columns.
    # The rows and columns along with our cell size help determine where
    # each individual cell belongs in our grid!
    for row in range(num_rows):
        for col in range(num_cols):
            left_x = col * CELL_SIZE
            top_y = row * CELL_SIZE
            right_x = left_x + CELL_SIZE   # The right coordinate of the cell is CELL_SIZE pixels away from the left
            bottom_y = top_y + CELL_SIZE   # The bottom coordinate of the cell is CELL_SIZE pixels away from the top
            
            # Create a single cell in the grid
            rect = Rectangle(Point(left_x, top_y), Point(right_x, bottom_y))
            rect.setFill('blue')
            rect.draw(win)
    
    win.getMouse()  # Wait for the user to click before creating the eraser
    
    # Get the starting location for the eraser
    last_click_x, last_click_y = win.getMouse().getX(), win.getMouse().getY()
    
    # Create our eraser
    eraser = Rectangle(Point(last_click_x, last_click_y), Point(last_click_x + ERASER_SIZE, last_click_y + ERASER_SIZE))
    eraser.setFill('pink')
    eraser.draw(win)
    
    # Move the eraser, and erase what it's touching
    while True:
        # Get where our mouse is and move the eraser to there
        mouse_x, mouse_y = win.getMouse().getX(), win.getMouse().getY()
        eraser.move(mouse_x - eraser.getCenter().getX(), mouse_y - eraser.getCenter().getY())
        
        # Erase anything touching the eraser
        erase_objects(win, eraser)
        
        time.sleep(0.05)

if __name__ == '__main__':
    main()
