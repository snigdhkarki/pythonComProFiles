# notes= [1,2,5,10]
# def combos(list):
#     #given list gives a list of combos that satisfy that have list elements as preceding elements
#     if sum(list) == 7:
#         return [list]
#     elif sum(list)>7:
#         return []
#     else:
#         return combos(list+[notes[0]])+combos(list+[notes[1]])+combos(list+[notes[2]])+combos(list+[notes[3]])
# print(combos([]))