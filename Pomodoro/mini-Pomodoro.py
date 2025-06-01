timeFactor = 1000
worktime = 25*60*timeFactor
breaktime = 5*60*timeFactor
#---
flag_2 = False
flag_1 = False
pause_time = 0
paused = False
bartime = 0
led_state = 0
start_time = 0
set_n = 0
breaktime = 0
set_n = 1

def on_button_a():
    global start_time, led_state, bartime, pause_time, flag_1, flag_2, set_n
    start_time = input.running_time()
    led_state = 0
    bartime = worktime / 5
    while set_n < 4:
        if paused:
            pause_time += 0.1 * timeFactor
            basic.pause(0.1 * timeFactor)
            continue
        time = input.running_time() - (start_time + pause_time)
        if not (flag_1):
            led_state += 1
            set_led_colors(led_state)
            flag_1 = True
        if time <= bartime:
            flash_bars(1)
        elif time <= 2 * bartime:
            flash_bars(2)
        elif time <= 3 * bartime:
            flash_bars(3)
        elif time <= 4 * bartime:
            flash_bars(4)
        elif time <= 5 * bartime:
            flash_bars(5)
        elif time <= worktime + breaktime:
            if not (flag_2):
                led_state += 1
                set_led_colors(led_state)
                flag_2 = True
            flash_bars(6)
        else:
            set_n += 1
            flag_1 = False
            flag_2 = False
            start_time = input.running_time()
    # ---
    basic.show_icon(IconNames.HAPPY)
    basic.pause(25)
    set_n = 1
    flag_1 = False
    flag_2 = False
input.on_button_event(Button.A, input.button_event_click(), on_button_a)

def set_led_colors(led_state2: number):
    if led_state2 == 1:
        basic.set_led_colors(0xffff00, 0x000000, 0x000000)
    elif led_state2 == 2:
        basic.set_led_colors(0x00ff00, 0x000000, 0x000000)
    elif led_state2 == 3:
        basic.set_led_colors(0x00ff00, 0xffff00, 0x000000)
    elif led_state2 == 4:
        basic.set_led_colors(0x00ff00, 0x00ff00, 0x000000)
    elif led_state == 5:
        basic.set_led_colors(0x00ff00, 0x00ff00, 0xffff00)
    elif led_state == 6:
        basic.set_led_colors(0x00ff00, 0x00ff00, 0x00ff00)
    basic.pause(25)

def on_button_b():
    global paused
    paused = not (paused)
input.on_button_event(Button.B, input.button_event_click(), on_button_b)

def show_bars(n: number):
    if n == 0:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
    elif n == 1:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            # # # # #
            """)
    elif n == 2:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            """)
    elif n == 3:
        basic.show_leds("""
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            """)
    elif n == 4:
        basic.show_leds("""
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
    elif n == 5:
        basic.show_leds("""
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
    elif n == 6:
        basic.show_icon(IconNames.HEART)

def flash_bars(o: number):
    show_bars(o)
    basic.pause(500)
    if o < 6:
        show_bars(o - 1)
    else:
        show_bars(0)
    basic.pause(500)