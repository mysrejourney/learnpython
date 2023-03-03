# def format_name(f_name, l_name):
#     first_name = f_name.title()
#     last_name = l_name.title()
#     return first_name + ' ' + last_name
#
#
# print(format_name("satheesh", "PaNdiAN"))

def outer_function(f_no, s_no):
    def inner_function(f, s):
        return  f + s
    return inner_function(f_no, s_no)

print(outer_function(5, 10))