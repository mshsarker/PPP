'''
copy_and_reverse('story.txt', 'story_reversed.txt') # None
# expect the contents of story_reversed.txt to be the reverse of the contents of story.txt
'''

def copy_and_reverse(story, story_reversed):
	with open(story) as file:
		text = file.read()
		
	with open(story_reversed, 'w') as new_file:
		new_file.write(text[::-1])

copy_and_reverse('story.txt', 'story_reversed.txt')