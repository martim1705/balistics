# 1 meter == 100 px 
# 

g = 9.80665 * 100.0 / (1.0/60.0) # px/s -> freq = 60 Hz 

gravitical_acc = {"Earth": g}

# v = v0 - g * t 
# y = y0 + v0 * t - (g * t**2) / 2