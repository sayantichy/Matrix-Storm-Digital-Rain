import sys, random, time

try:
    import curses
except ImportError:
    print("Curses module not found. Install it using: pip install windows-curses (Windows only)")
    sys.exit()

def matrix_storm(stdscr):
    curses.curs_set(0)  # Hide cursor
    stdscr.nodelay(1)  # Non-blocking input
    stdscr.timeout(100)  # Refresh speed

    # Initialize colors
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)   # Matrix rain
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)   # Thunder
    curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)    # Clouds
    curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_BLACK)    # Water puddles
    curses.init_pair(5, curses.COLOR_YELLOW, curses.COLOR_BLACK)  # Raindrop splash

    sh, sw = stdscr.getmaxyx()  # Screen height & width
    cols = [random.randint(0, sh - 1) for _ in range(sw)]  # Initial column positions
    speeds = [random.randint(1, 3) for _ in range(sw)]  # Speed variations

    symbols = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ@#$%&*+"  # Matrix symbols
    cloud_shape = " ☁☁  ☁☁☁   ☁☁  "  # Large clouds
    water_accumulation = ["_", "~", "≈", "≋"]  # Water ripples
    puddles = [" " for _ in range(sw)]  # Store puddle state

    thunder_active = False  # Track if thunder just flashed

    while True:
        stdscr.clear()

        # Generate Large Clouds ☁️ at the top
        for i in range(0, sw, 10):  # Space them out
            if random.random() > 0.85:  # Random chance for cloud
                stdscr.addstr(0, i, cloud_shape, curses.color_pair(3))

        # Loop through each column for matrix rain
        for i in range(sw):
            if random.random() > 0.95:  # Randomly reset a column
                cols[i] = 0
                speeds[i] = random.randint(1, 3)  # Random new speed

            if cols[i] < sh - 2:  # Ensure it does not go beyond screen
                char = random.choice(symbols)
                stdscr.addstr(cols[i], i, char, curses.color_pair(1))  # Green matrix rain
                cols[i] += speeds[i]

                # Create water effect at the bottom
                if cols[i] >= sh - 2:
                    puddles[i] = random.choice(water_accumulation)  # Water ripples
                    stdscr.addstr(sh - 2, i, random.choice(["💦", "*"]), curses.color_pair(5))  # Splash effect

        # Display water accumulation 🌊 at the bottom
        water_line = "".join(puddles)
        stdscr.addstr(sh - 2, 0, water_line, curses.color_pair(4))

        # Random Thunderstorm Effect ⚡ with Reflection 🌊
        if random.random() > 0.98:  # Small chance for thunder
            thunder_x = random.randint(0, sw - 6)
            thunder_strike = "⚡⚡⚡⚡⚡"
            stdscr.addstr(random.randint(1, sh // 2), thunder_x, thunder_strike, curses.color_pair(2))
            
            # Lightning Reflection on Water 🌊
            stdscr.addstr(sh - 2, 0, "_" * sw, curses.color_pair(2))  # Flash water reflection

            # Screen Flash Effect 💥
            stdscr.refresh()
            time.sleep(0.05)  # Short delay for flash effect
            stdscr.clear()  # Clear screen after flash
            thunder_active = True

        # Remove flash effect from water after thunder
        if thunder_active:
            stdscr.addstr(sh - 2, 0, water_line, curses.color_pair(4))
            thunder_active = False

        stdscr.refresh()
        time.sleep(0.1)

        # Quit if 'q' is pressed
        if stdscr.getch() == ord('q'):
            break

curses.wrapper(matrix_storm)
