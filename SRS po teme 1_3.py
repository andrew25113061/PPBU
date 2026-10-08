# import random
#
# first_words = ["ты", "у тебя", "в тебе", "твой", "твоя"]
# second_words = ["замечательный", "потрясающая", "волшебный", "прекрасный", "невероятно крутая"]
#
# def generate_compliment():
#     word1 = random.choice(first_words)
#     word2 = random.choice(second_words)
#     return f"{word1} {word2}!"
#
# for _ in range(5):
#     print(generate_compliment())

# s = [x for x in range(10) if x > 3]
# s.append(10)
# print(s)
#
# s = list(range(10, 4, -1))
# print(s)

# s = []
# for x in range(0, 10):
#     if x > 3:
#         s.append(x)
# print (s)
# s= list(range(10, 4, -1))
# print(s)

words = ["море", "солнце", "майка", "отпуск"]

a_words = [i for i in words if i.endswith('е')]

print(a_words)