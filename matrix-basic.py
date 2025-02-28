import sys, random, time
try:
    import curses
except ImportError:
    print("Curses module not found. Run on a terminal!")
    sys.exit()

def matrix_effect(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)
    sh, sw = stdscr.getmaxyx()
    cols = [0] * sw
    while True:
        stdscr.clear()
        for i in range(sw):
            if random.random() > 0.98:
                cols[i] = 0
            if cols[i] < sh - 1:
                stdscr.addstr(cols[i], i, str(random.randint(0, 9)), curses.color_pair(1))
                cols[i] += 1
        stdscr.refresh()
        time.sleep(0.1)

curses.wrapper(matrix_effect)
