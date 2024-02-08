def cross_bridge(distance):
    for i in range(distance):
        print("Crossed step")
    if distance > 5:
        print("The bridge is collapsing!")
    else:
        print("We must keep going!")


# Call the function three times with different distances

cross_bridge(-1)
