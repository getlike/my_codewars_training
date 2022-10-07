def points(games):
    sum = 0
    for points in games:
        if (points.split(':')[0] > points.split(':')[1]):
            sum += 3
        # if (points.split(':')[0] < points.split(':')[1]):
        #     pass
        if (points.split(':')[0] == points.split(':')[1]):
            sum += 1
    print(sum)

points(['1:0', '2:0', '3:0', '4:0', '2:1', '3:1', '4:1', '3:2', '4:2', '4:3'])
