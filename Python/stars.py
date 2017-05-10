# Stars Part 1

def draw_stars(list):
    for value in list:
        string = "*" * value
        print string
x = [4, 6, 1, 3, 5, 7, 25]
draw_stars(x)

# Stars Part 2

def draw_stars(list):
    for value in list:
        if type(value) == int:
            string = "*" * value
            print string
        elif type(value) == str:
            letter = value[0].lower()
            print letter * len(value)
x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars(x)
