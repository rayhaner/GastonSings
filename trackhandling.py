import os
import sys

from pydub import AudioSegment
from pydub.playback import play
from random import choice

file_list = ['gaston_full', 'when_i_was_a', 'lad', 'i_ate', 'four_dozen', 'eggs1', 'every_morning', 'large',
             'and_now', 'grown', 'i_eat', 'five_dozen', 'eggs2', 'roughly', 'barge']
nouns = ['lad', 'eggs1', 'eggs2', 'barge', 'grown']
numbers = ['four_dozen', 'five_dozen']

original = ['lad', 'four_dozen', 'eggs1', 'large', 'grown', 'five_dozen', 'eggs2', 'barge']

string_dict = {
    'grown': 'GROWN',
    'lad': 'LAD',
    'large': 'LARGE',
    'barge': 'BARGE',
    'eggs1': 'EGGS',
    'eggs2': 'EGGS',
    'five_dozen': 'FIVE DOZEN',
    'four_dozen': 'FOUR DOZEN'
}

string_dict_rev = {value: key for key, value in string_dict.items() if key != 'eggs2'}


def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))

    if relative_path is None:
        return base_path
    else:
        return os.path.join(base_path, relative_path)


def import_tracks():
    def from_string(s):
        soundfile_name = s + '.wav'
        path = resource_path('samples')
        return AudioSegment.from_wav(os.path.join(path, soundfile_name))

    t_list = {}
    for filename in file_list:
        t_list[filename] = from_string(filename)

    return t_list


def to_string(*args):
    return 'When I was a ' + string_dict[args[0]] + ' I ate ' + string_dict[args[1]] + ' ' + string_dict[args[2]] + \
           ' every morning to help me get ' + string_dict[args[3]] + ",\nAnd now that I'm " + string_dict[args[4]] + \
           ' I eat ' + string_dict[args[5]] + ' ' + string_dict[args[6]] + " so I'm roughly the size of a " + \
           string_dict[args[7]] + '!'


t = import_tracks()


def make_track(*input):
    slots = list(input)
    if slots[2] == 'eggs2':
        slots[2] = 'eggs1'
    if slots[6] == 'eggs1':
        slots[6] = 'eggs2'
    out_str = to_string(*slots)
    return t['when_i_was_a'] + t[slots[0]] + t['i_ate'] + t[slots[1]] + t[slots[2]] + \
           t['every_morning'] + t[slots[3]] + t['and_now'] + t[slots[4]] + t['i_eat'] + t[slots[5]] + \
           t[slots[6]] + t['roughly'] + t[slots[7]], out_str


def play_track(track):
    play(track)


def randomize(same_num=False):
    slots = [choice(nouns), choice(numbers), choice(nouns[:4]), choice(nouns), choice(nouns), choice(numbers),
             choice(nouns[:4]), choice(nouns)]

    if same_num:
        slots[1] = 'four_dozen'
        slots[5] = 'five_dozen'

    return make_track(*slots)


def same_word(word=None):
    if word is None:
        word = choice(nouns)

    return make_track(word, 'four_dozen', word, word, word, 'five_dozen', word, word)
