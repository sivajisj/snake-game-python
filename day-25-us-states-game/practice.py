
#
# output_list = []
# name = input("Enter your name : ")
#
# for i in name:
#     for n in word_list:
#         if n.startswith(i,0):
#             output_list.append(n)
# print(output_list)
#
# list = [ l for l in "sivaji"]
# print(list)

# double_list = [num * 2 for num in range(1,6)]
# print(double_list)
#
# three_letter_list = [word for word in word_list if len(word) <=3]
# print(three_letter_list)

#
import pandas

word_list = ["apple", "boll", "cat", "dog", "elephant", "fish", "grape", "house", "ice", "jacket", "kite", "lemon",
             "moon", "nest", "orange", "pear", "queen", "rose", "sun", "table", "umbrella", "volcano", "window",
             "xylophone", "yellow", "zebra"]
my_dict = {
    'apple': ["apple", "boll", "cat", "dog", "elephant", "fish", "grape", "house", "ice", "jacket", "kite", "lemon",
             "moon", "nest", "orange", "pear", "queen", "rose", "sun", "table", "umbrella", "volcano", "window",
             "xylophone", "yellow", "zebra"],
    'banana': ["apple", "boll", "cat", "dog", "elephant", "fish", "grape", "house", "ice", "jacket", "kite", "lemon",
             "moon", "nest", "orange", "pear", "queen", "rose", "sun", "table", "umbrella", "volcano", "window",
             "xylophone", "yellow", "zebra"],
}
dict_d_f = pandas.DataFrame(my_dict)
print(my_dict)
print(dict_d_f)

for (index,data) in dict_d_f.items():
    print(data)
#
# updated = {key:value for (key,value) in my_dict.items() if value > 3}
# print(updated)

# sentense = input()
# arr = sentense.split(" ")
# print(arr)
# output = {key : len(key) for key in arr}
# print(output)
