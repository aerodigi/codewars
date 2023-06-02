'''There was a test in your class and you passed it. Congratulations!
But you're an ambitious person. You want to know if you're better than the average student in your class.

You receive an array with your peers' test scores. Now calculate the average and compare your score!

Return True if you're better, else False!'''

def better_than_average(class_points, your_points):
    total = 0
    for x in class_points:
        total += x
    average = total / len(class_points)
    if your_points > average:
        return True
    else:
        return False
        

better_than_average([41, 75, 72, 56, 80, 82, 81, 33], 50)