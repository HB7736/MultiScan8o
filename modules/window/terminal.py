import subprocess
from sys import path
from os.path import dirname, abspath
path.append(dirname(dirname(abspath(__file__))))

from others.filesystem import tmpfile_path, delete_file  # Import functions from filesystem.py

def execute_command(command, width=40, height=30, autoclose=False, fontsize="normal", output_file=None):
    """
    Opens a gnome-terminal window with the given size and runs the specified command.

    Args:
    command (str): The command to run in the terminal.
    width (int): The width of the terminal window.
    height (int): The height of the terminal window.
    """
    try:
        if fontsize=="mini":
            profile="miniGhost"
        else:
            profile="Ghost"

        tmp_file = tmpfile_path()
        with open(tmp_file, "w") as tmpfile:
            tmpfile.write(command)
        exit_command = ' echo -n "Press Enter to Close Terminal...."; read' if not autoclose else ''
        subprocess.run([
            'gnome-terminal',
            '--hide-menubar',
            '--disable-factory',
            f'--profile={profile}',
            '--geometry', f'{width}x{height}',
            '--', 'bash', '-c',
            (f"script '{output_file}' -q -c 'bash {tmp_file}';" if output_file else f"bash {tmp_file};") + exit_command
        ])
        delete_file(tmp_file)
    except Exception as e:
        print("Exception Occured:",str(e))

# Example usage:
if __name__=="__main__":
    execute_command(r'''echo Hello, World!''', 80, 24)
