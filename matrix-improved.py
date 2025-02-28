import sys, random, time

try:
    import curses
except ImportError:
    print("Curses module not found. Install it using: pip install windows-curses (Windows only)")
    sys.exit()

def matrix_effect(stdscr):
    curses.curs_set(0)  # Hide the cursor
    stdscr.nodelay(1)  # Non-blocking input (allows quitting)
    stdscr.timeout(100)  # Refresh speed

    # Initialize colors (Green on Black)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)

    sh, sw = stdscr.getmaxyx()  # Get screen height and width
    cols = [random.randint(0, sh - 1) for _ in range(sw)]  # Random start positions for each column
    speeds = [random.randint(1, 3) for _ in range(sw)]  # Random speed per column

    symbols = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ@#$%&*+"  # Matrix-like symbols

    while True:
        stdscr.clear()

        # Loop through each column
        for i in range(sw):
            if random.random() > 0.95:  # Randomly reset a column
                cols[i] = 0
                speeds[i] = random.randint(1, 3)  # Change speed randomly

            if cols[i] < sh - 1:  # Stay within screen bounds
                char = random.choice(symbols)  # Pick a random Matrix-like symbol
                stdscr.addstr(cols[i], i, char, curses.color_pair(1))  # Print character in green
                cols[i] += speeds[i]  # Move down by speed amount

        stdscr.refresh()
        time.sleep(0.1)  # Controls the animation speed

        # Quit if 'q' is pressed
        if stdscr.getch() == ord('q'):
            break

curses.wrapper(matrix_effect)
