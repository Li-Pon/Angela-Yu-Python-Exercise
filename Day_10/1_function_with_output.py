def format_name(f_name, l_name):
    total_name = f_name.title() + ' ' + l_name.title()
    return total_name


first_name = input("Input your first name: ")
last_name = input("Input your last name: ")

title_name = format_name(f_name=first_name, l_name=last_name)
print(title_name)
