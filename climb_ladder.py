def climb_ladder(steps_remaining, steps_crossed):
    if steps_remaining > steps_crossed:
        print("Still some way to go!")
    else:
        print("We are almost there!")


# Call the function three times with different distances
climb_ladder(10, 5)
climb_ladder(5, 7)
climb_ladder(1, 1)
