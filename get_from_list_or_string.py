
# Feel free to change the list to a list of your own to see the results 

example_list = ["a", "b", "c", "d", "e", "f"]



# Choose element starting from index 0 using list_name[index of element] 
# Play around with the value of select_by_index to see the results
select_by_index = 2
get_element = example_list[select_by_index]


# Choose elements within a defined range 
# list slice starts at the left of the colon, in this case 1
# List is sliced all the way up to but does not include the end position
# which is on the right of the colon in this case 5

# Play around with the numbers in start_index and end_index and runing the program to see the results
start_index = 2
end_index = 5

get_elements_within_slice = example_list[start_index:end_index]


# To change the default step size of one element at a time
# we add a second ":"inside the square brackets i.e: [::step_size]
# In this example to change only the step we can ommit the start and end numbers just adding the colon

# play around with the value of step_size to see the behaviour
step_Size = 3
get_every_step_size_element_full_list = example_list[::step_Size]



# Play around with these variables to see the results of selecting elements from a list slice with a different step size
start_Index = 2
end_Index = 5
step_Size = 2

get_every_step_size_element_sliced_list = example_list[start_Index:end_Index:step_Size]















# Just the formated print statements, no need to worry about this part =)

print("\n#---------- List navigation cheatsheet =)-----------#\n")       



print("####################################################")
print("#             Select element by index              #")       
print("####################################################")

print(f"\nGiven the list: example_list = {example_list}\nthe element '{get_element}' which is on index {select_by_index}\ncan be selected by using the index inside square brackets\nuse the following syntax\n\n   example_list[{select_by_index}]\n      Results in:\n{example_list} -> {get_element}\n")

print("####################################################")
print("#                 List slicing                     #")       
print("####################################################")

print(f"\nGiven the list: example_list = {example_list}\nto select only from start index up to to but not included end index\nusing the following syntax\n\nexample_list[{start_index}:{end_index}]\n      Results in:\n {example_list} -> {get_elements_within_slice}\n")


print("####################################################")
print("#             Changing step size                   #")       
print("####################################################")

print(f"\nGiven the list: example_list = {example_list}\nchanging the step size to {step_Size}\nuse the following syntax\nexample_list[::{step_Size}]\n      Results in:\n {example_list} -> {get_every_step_size_element_full_list}\n\nps: if step_size = -1 the list will be reversed\n")

print("######################################################")
print("#         Changing step size of a list slice         #")       
print("######################################################")

print(f"\nGiven the list: example_list = {example_list}\nstarting on index {start_Index} up to but not including the element in index {end_Index} changing the step size to {step_Size}\nuse the following syntax\nexample_list[{start_Index}:{end_Index}:{step_Size}]\n      Results in:\n {example_list} -> {get_every_step_size_element_sliced_list}\n")

print("------------------------------------------------------")