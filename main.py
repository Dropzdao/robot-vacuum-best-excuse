def validate(text):
    assert len(text) <= 200, "entry too long"
    return text


line = validate("My lidar mapped that corner as a cliff, so I filed it under 'do not enter' and went back to my dock for emotional support.")

print(line)
