print("Welcome to the love calculator")
first_name = input("Enter your name: ")
second_name = input("Enter your crush name: ")

combine_name = first_name + second_name
t_count = combine_name.lower().count('t')
r_count = combine_name.lower().count('r')
u_count = combine_name.lower().count('u')
e_count = combine_name.lower().count('e')

true_sum = t_count + r_count + u_count + e_count

l_count = combine_name.lower().count('l')
o_count = combine_name.lower().count('0')
v_count = combine_name.lower().count('v')
# e_count = combine_name.lower().count('e')

love_sum = l_count + o_count + v_count + e_count

final_score = true_sum * 10 + love_sum

if final_score < 10 or final_score > 90:
    print(f"Your score is {final_score}, you go together like coke and mentos")

elif final_score > 40 and final_score < 50:
    print(f"Your score is {final_score}, you are alright together")
else:
    print(f"Your score is {final_score}")

