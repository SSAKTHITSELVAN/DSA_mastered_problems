from pathlib import Path
import turtle
import time

# Constants
START = "S"
OBSTACLE = "+"
TRIED = "."
DEAD_END = "-"
PART_OF_PATH = "0"
PATH_COLOR = "green"
OBSTACLE_COLOR = "orange"
TRIED_COLOR = "red"
DEAD_END_COLOR = "red"

class Maze:
    def __init__(self, maze_filename):
        # Use Path for more robust file handling
        maze_path = Path(__file__).parent / maze_filename
        
        with maze_path.open("r") as maze_file:
            # Use the character-by-character processing
            self.maze_list = [
                [ch for ch in line.strip("\n")]
                for line in maze_file.readlines()
            ]
            
        # Initialize maze properties
        self.rows_in_maze = len(self.maze_list)
        self.columns_in_maze = len(self.maze_list[0])
        
        # Find the starting position
        for row_idx, row in enumerate(self.maze_list):
            if START in row:
                self.start_row = row_idx
                self.start_col = row.index(START)
                break
                
        # Setup for visualization
        self.x_translate = self.columns_in_maze / 2
        self.y_translate = self.rows_in_maze / 2
        
        # Depth tracking for recursion visualization
        self.current_depth = 0
        self.max_depth = 0
        
        # Initialize turtle graphics
        self.t = turtle.Turtle()
        self.t.shape("turtle")
        self.wn = turtle.Screen()
        self.wn.title("Maze Solver - Watch the Recursion in Action")
        self.wn.setworldcoordinates(
            -(self.columns_in_maze - 1) / 2 - 0.5,
            -(self.rows_in_maze - 1) / 2 - 0.5,
            (self.columns_in_maze - 1) / 2 + 0.5,
            (self.rows_in_maze - 1) / 2 + 0.5
        )
        
        # Add a status turtle for displaying recursion info
        self.status_t = turtle.Turtle()
        self.status_t.hideturtle()
        self.status_t.penup()
        self.status_t.goto(0, self.rows_in_maze / 2 + 1)
        
        # Slow delay between steps (seconds)
        self.delay = 0.2
    
    def read_maze(self):
        return self.maze_list
        
    def draw_maze(self):
        """Draw the initial maze structure"""
        self.t.speed(0)
        self.wn.tracer(0)
        
        for y in range(self.rows_in_maze):
            for x in range(self.columns_in_maze):
                if self.maze_list[y][x] == OBSTACLE:
                    self.draw_centered_box(
                        x - self.x_translate,
                        -y + self.y_translate,
                        OBSTACLE_COLOR
                    )
                elif self.maze_list[y][x] == START:
                    # Mark the starting position more clearly
                    self.draw_centered_box(
                        x - self.x_translate,
                        -y + self.y_translate,
                        "blue"
                    )
        
        self.t.color("black")
        self.t.fillcolor("blue")
        self.wn.update()
        self.wn.tracer(1)
        
        # Create a legend
        self.create_legend()

    def create_legend(self):
        """Create a legend for the different colors used"""
        legend = turtle.Turtle()
        legend.hideturtle()
        legend.penup()
        
        # Position the legend
        x_pos = -self.columns_in_maze / 2 - 0.5
        y_pos = self.rows_in_maze / 2
        
        # Draw legend items
        items = [
            ("Start", "blue"),
            ("Obstacle", OBSTACLE_COLOR),
            ("Path Tried", TRIED_COLOR),
            ("Dead End", DEAD_END_COLOR),
            ("Solution Path", PATH_COLOR)
        ]
        
        for i, (text, color) in enumerate(items):
            legend.penup()
            legend.goto(x_pos, y_pos - i)
            
            # Draw color box
            legend.pendown()
            legend.fillcolor(color)
            legend.begin_fill()
            for _ in range(4):
                legend.forward(0.8)
                legend.right(90)
            legend.end_fill()
            legend.penup()
            
            # Write text
            legend.goto(x_pos + 1, y_pos - i - 0.5)
            legend.write(text, font=("Arial", 8, "normal"))
            
        self.wn.update()

    def draw_centered_box(self, x, y, color):
        """Draw a colored box at the specified coordinate"""
        self.t.up()
        self.t.goto(x - 0.5, y - 0.5)
        self.t.color("black")
        self.t.fillcolor(color)
        self.t.setheading(90)
        self.t.down()
        self.t.begin_fill()
        
        for i in range(4):
            self.t.forward(1)
            self.t.right(90)
        
        self.t.end_fill()

    def update_position(self, row, col, val=None):
        """Update the maze position with a new value and visualize it"""
        if val:
            self.maze_list[row][col] = val
            
        self.t.up()
        self.t.goto(col - self.x_translate, -row + self.y_translate)
        
        if val == PART_OF_PATH:
            self.t.color("black")
            self.t.fillcolor(PATH_COLOR)
        elif val == OBSTACLE:
            self.t.color("black")
            self.t.fillcolor(OBSTACLE_COLOR)
        elif val == TRIED:
            self.t.color("black")
            self.t.fillcolor(TRIED_COLOR)
        elif val == DEAD_END:
            self.t.color("black")
            self.t.fillcolor(DEAD_END_COLOR)
        else:
            self.t.color("black")
            self.t.fillcolor("blue")
            
        self.t.shape("turtle")
        self.t.shapesize(0.6)  # Make turtle smaller to see the path better
        self.t.stamp()
        self.wn.update()
        
        # Add delay to slow down the visualization
        time.sleep(self.delay)

    def update_status(self, row, col, direction=None):
        """Update the status display with current recursion information"""
        self.status_t.clear()
        
        # Format status message
        status = f"Exploring [{row},{col}]"
        if direction:
            status += f" Direction: {direction}"
        status += f" | Recursion Depth: {self.current_depth}"
        
        self.status_t.write(status, align="center", font=("Arial", 12, "bold"))

    def is_exit(self, row, col):
        """We've reached an exit if we're at the edge of the maze"""
        return (row == 0 or
                row == self.rows_in_maze - 1 or
                col == 0 or
                col == self.columns_in_maze - 1)

    def __getitem__(self, idx):
        """Allow indexing directly on the Maze object to access maze_list rows"""
        return self.maze_list[idx]

    def search_from(self, row, col, direction=None):
        """
        Search for a solution from the current position.
        Direction parameter helps visualize which direction we're exploring.
        """
        # Track recursion depth for visualization
        self.current_depth += 1
        self.max_depth = max(self.max_depth, self.current_depth)
        
        # Update status display
        self.update_status(row, col, direction)
        
        # Base cases
        # 1. Hit an obstacle
        if self.maze_list[row][col] == OBSTACLE:
            self.current_depth -= 1
            return False
        
        # 2. Found a square already tried or a dead end
        if self.maze_list[row][col] == TRIED or self.maze_list[row][col] == DEAD_END:
            self.current_depth -= 1
            return False
        
        # 3. Found an outside edge that's not an obstacle
        if self.is_exit(row, col):
            self.update_position(row, col, PART_OF_PATH)
            self.current_depth -= 1
            return True
        
        # 4. Mark as tried and explore
        self.update_position(row, col, TRIED)
        
        # Try each of the four directions with clear labels
        # The order determines which direction is tried first
        found = False
        
        # North
        if not found:
            self.t.setheading(90)  # Point turtle north
            found = self.search_from(row - 1, col, "North")
        
        # East
        if not found:
            self.t.setheading(0)  # Point turtle east
            found = self.search_from(row, col + 1, "East")
        
        # South
        if not found:
            self.t.setheading(270)  # Point turtle south
            found = self.search_from(row + 1, col, "South")
        
        # West
        if not found:
            self.t.setheading(180)  # Point turtle west
            found = self.search_from(row, col - 1, "West")
        
        # Update position based on whether a path was found
        if found:
            self.update_position(row, col, PART_OF_PATH)
        else:
            self.update_position(row, col, DEAD_END)
        
        # Decrease recursion depth as we're backtracking
        self.current_depth -= 1
        return found

    def solve_maze(self):
        """Draw the maze and solve it"""
        # Set slower speed for better visualization
        self.t.speed(3)
        self.wn.tracer(1)  # Enable animation
        
        # Draw the maze first
        self.draw_maze()
        
        # Brief pause to see the full maze before starting
        time.sleep(1)
        
        # Display starting message
        self.status_t.write("Starting maze solution from S...", 
                           align="center", font=("Arial", 12, "bold"))
        time.sleep(1)
        
        # Start searching from the starting position
        self.t.penup()
        self.t.goto(self.start_col - self.x_translate, -self.start_row + self.y_translate)
        self.t.pendown()
        
        result = self.search_from(self.start_row, self.start_col)
        
        # Display completion message
        self.status_t.clear()
        if result:
            self.status_t.write(f"Maze solved! Maximum recursion depth: {self.max_depth}", 
                               align="center", font=("Arial", 12, "bold"))
        else:
            self.status_t.write("No solution found!", 
                               align="center", font=("Arial", 12, "bold"))
        
        return result

# Example maze file creation helper
def create_sample_maze(filename="maze.txt"):
    """Create a sample maze file if one doesn't exist"""
    maze_text = """+++++++++++++++++++++++
+   +   ++ ++        +
+ +   +       ++++++ +
+ + +  ++  ++++   + ++
+++ ++++++    +++ +  +
+          ++  ++    +
+++++ ++++++   +++++ +
+     +   +++++++  + +
+ +++++++      S +   +
+                + +++
++++++++++++++++++ +++"""
    
    with open(filename, "w") as f:
        f.write(maze_text)
    
    print(f"Sample maze created as {filename}")

# Example usage
if __name__ == "__main__":
    maze_file = "maze.txt"
    
    # Create sample maze if needed
    try:
        with open(maze_file, "r") as f:
            pass  # File exists, do nothing
    except FileNotFoundError:
        create_sample_maze(maze_file)
    
    # Create a maze instance
    my_maze = Maze(maze_file)
    
    # Ask user for speed preference
    try:
        speed = float(input("Enter delay between steps (0.1-1.0 seconds recommended): "))
        my_maze.delay = max(0.05, min(2.0, speed))  # Limit to reasonable range
    except:
        print("Using default delay of 0.2 seconds")
    
    # Solve the maze
    solved = my_maze.solve_maze()
    
    # Print the result
    print(f"Maze solved: {solved}")
    
    # Keep the window open until closed manually
    turtle.mainloop()