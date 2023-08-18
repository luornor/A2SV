def findRadius(houses, heaters):
    min_radius = 0
    houses.sort()  # Sort houses
    heaters.sort()  # Sort heaters
    i = 0  # House index
    j = 0  # Heater index

    while i < len(houses):
        # Find the nearest heater for the current house
        #For each house, calculate the distance between the current house and the current and next heaters.
        # Then Move the position of the heater index to the next heater 
        # if the next heater is closer to the current house
        while j < len(heaters) - 1 and abs(houses[i] - heaters[j + 1]) <= abs(houses[i] - heaters[j]):
            j += 1

        # Update the minimum radius if necessary
        min_radius = max(min_radius, abs(houses[i] - heaters[j]))
        i += 1

    return min_radius
            