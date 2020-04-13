# Print out all of the strings in the following array in alphabetical order, each on a separate line.
name_array = ['Waltz', 'Tango', 'Viennese Waltz', 'Foxtrot', 'Cha Cha', 'Samba', 'Rumba', 'Paso Doble', 'Jive']
num_array = [57, 93, 44, 2, 109, 33, 22, 12, 69, 75, 81 ]
'''
The expected output is:
'Cha Cha'
'Foxtrot'
'Jive'
'Paso Doble'
'Rumba'
'Samba'
'Tango'
'Viennese Waltz'
'Waltz'
'''



# order the array of strings and print each string on new line
def sort_string_array(str_arr):
    print("Array of names in alphabetical order, each name on a new line.")
    for name in sorted(str_arr, reverse=True):
        print(name)
    print("\n\n")

# sort the array of strings and print in reverse order, z to a
def rev_sort_string_array(str_arr):
    print("Array of names in reverse alphabetical order, each name on a new line.")
    for name in sorted(str_arr, reverse=True):
        print(name)
    print("\n\n")


# use key attribute to sort number array 
def sort_nums(num_arr):
    num_array.sort(reverse=False, key=int)
    print("lowest to highest(default sort): ", num_array)

# sort the num array highest to lowest:
def rev_sort_nums(num_arr):
    num_array.sort(reverse=True, key=int)
    print("highest to lowest: ", num_array)

sort_string_array(name_array)
rev_sort_string_array(name_array)
sort_nums(num_array)
rev_sort_nums(num_array)

# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.