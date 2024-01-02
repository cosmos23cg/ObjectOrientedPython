def turn_on():
    global switch_is_on
    switch_is_on = True

def turn_off():
    global switch_is_on
    switch_is_on = False


switch_is_on = False

print(switch_is_on)
turn_on()
print(switch_is_on)
turn_off()
print(switch_is_on)
turn_on()
print(switch_is_on)
