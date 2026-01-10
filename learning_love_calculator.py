true_count = [0, 0, 0, 0]
love_count = [0, 0, 0, 0]

def true_love_compare(letter):
    if letter == "T" or letter == "t":
        true_count[0] += 1
    if letter == "R" or letter == "r":
        true_count[1] += 1
    if letter == "U" or letter == "u":
        true_count[2] += 1
    if letter == "E" or letter == "e":
        true_count[3] += 1

    if letter == "L" or letter == "l":
        love_count[0] += 1
    if letter == "O" or letter == "o":
        love_count[1] += 1
    if letter == "V" or letter == "v":
        love_count[2] += 1
    if letter == "E" or letter == "e":
        love_count[3] += 1

def calculate_love_score(name1, name2):
    longest_name_length = 0

    name1_length = len(name1)
    name2_length = len(name2)
    if name1_length > name2_length:
        longest_name_length = name1_length
    else:
        longest_name_length = name2_length

    list_name1 = list(name1)
    list_name2 = list(name2)
    for i in range(longest_name_length):
        if i < name1_length:
            true_love_compare(list_name1[i])

        if i < name2_length:
            true_love_compare(list_name2[i])

# input_name1 = input("The first person's name: ")
# input_name2 = input("The second person's name: ")
#
# calculate_love_score(input_name1, input_name2)
#
# print(f"Love Score = {sum(true_count)}{sum(love_count)}")

calculate_love_score("Kanye West", "Kim Kardashian")
love_score = str(sum(true_count)) + str(sum(love_count))

print(love_score)