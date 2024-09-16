# Mad lib example for functions
def madlib(noun_1, adjective_1, adjective_2, noun_2, noun_3, verb_1, adjective_3, noun_4, verb_2, verb_3):
    '''Mad lib function'''

    story = f'''
While on vacation in {noun_1}, I stumbled upon a surprise concert on the beach.
The air was {adjective_1} and the sun was {adjective_2}, making the moment feel
like a dream. Suddenly, out of nowhere, {noun_2} began playing, and to my 
shock, standing on the stage was none other than {noun_3}! I couldn't believe 
it. My heart started {verb_1} as I moved closer, trying not to look too
{adjective_3}. Just as I reached the front of the crowd, {noun_4} 
appeared in the singer's hand, and they tossed it in my direction. I caught
it! Then, the singer smiled at me and {verb_2} into the microphone. I 
knew this was going to be the most {verb_3} vacation ever.
    '''
    return story

def get_user_input():
    """Prompt the user for input for the mad lib."""
noun_1 = input("Enter a noun:")
adjective_1 = input("Enter an adjective")
adjective_2 = input("Enter another adjective")
noun_2 = input("Enter another noun:")
noun_3 = input("Enter another noun:")
verb_1 = input("Enter a verb:")
noun_4 = input("Enter a final  noun:")
adjective_3 = input("Enter a final adjective")
verb_2 = input("Enter another verb:")
verb_3 = input("Enter a final verb:")

return noun_1, adjective_1, adjective_2, noun_2, noun_3, verb_1, noun_4, adjective_3, verb_2, verb_3


def duplicate_get_input():
    """prompt...."""
    noun_1
    adjective_1
    adjective_2
    noun_2
    noun_3
    verb_1
    adjective_3
    noun_4
    verb_2
    verb_3

return noun_1, adjective_1, adjective_2, noun_2, noun_3, verb_1, noun_4, adjective_3, verb_2, verb_3




output_story = madlib('Peru', 'thick', 'fiery', 'music', 'Mariah Carey', 'racing', 'excited', 'money', 'whistled', 'wonderful')
print(output_story)