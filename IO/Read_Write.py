This code is from the Udemy course by Colt Stelle.
'''
copy('story.txt', 'story_copy.txt') # None
# expect the contents of story.txt and story_copy.txt to be the same
'''

def copy(file_name, new_file_name):
    with open(file_name) as file:
    	text = file.read()

    with open(new_file_name, 'w') as new_file:
    	new_file.write(text)


copy('story.txt', 'story_copy.txt')


