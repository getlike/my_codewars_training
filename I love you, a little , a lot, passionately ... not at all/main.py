leaf = int(input('number leaf (it must be bigger tnan 0): '))
while leaf > 6:
    leaf -= 6
flower_leaf = ["I love you",
               "a little",
               "a lot",
               "passionately",
               "madly",
               "not at all"]
print(flower_leaf[leaf-1])
