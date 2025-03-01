import os

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Get the parent directory
parent_dir = os.path.dirname(current_dir)

# Create the 'Game' directory in the parent directory if it doesn't exist
game_dir = os.path.join(parent_dir, 'Game')
os.makedirs(game_dir, exist_ok=True)

# Path to the .bat file
bat_file_path = os.path.join(game_dir, 'Agrios (Terminal Mode).bat')

# Command to run 'terminal_mode.py' from the original directory
command = f'python "{os.path.join(current_dir, "terminal_mode.py")}"'

# Write the command to the .bat file
with open(bat_file_path, 'w') as bat_file:
    bat_file.write(command)

print(f'.bat file created at: {bat_file_path}')
