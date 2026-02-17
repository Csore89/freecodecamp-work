# 1. Variable Definitions
distance_mi = 5
is_raining = False
has_bike = True
has_car = False
has_ride_share_app = False

# 2. Conditional Logic
if not distance_mi:
    # Handles 0 or None (Falsy)
    print(False)

elif distance_mi <= 1:
    # Short Distance: True only if NOT raining
    if not is_raining:
        print(True)
    else:
        print(False)

elif distance_mi <= 6:
    # Medium Distance (Between 1 and 6 miles)
    # MUST have bike AND NOT be raining
    if has_bike and not is_raining:
        print(True)
    else:
        print(False)

else:
    # Long Distance (> 6 miles)
    # Needs car OR ride share
    if has_car or has_ride_share_app:
        print(True)
    else:
        print(False)