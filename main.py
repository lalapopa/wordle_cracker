import re
import numpy as np
import random
import sys

WORDS_FILE = "words_alpha.txt"


def find_symbols(word, list_symb):
    finded_sym = []
    for sym in word:
        if sym in list_symb:
            finded_sym.append(sym)

    for sym in list_symb:
        if sym in finded_sym:
            pass
        else:
            return False
    return True


def has_dead_symbol(word, dead_sym):
    for sym in word:
        if sym in dead_sym:
            return True

    return False


def accept_yellow_pos(word, y_p):
    if y_p:
        syms = []
        for val in y_p.keys():
            if val not in word:
                return False

        for i, sym in enumerate(word):
            for key, positions in y_p.items():
                if sym == key:
                    if i in positions:
                        return False
    return True


def accept_green_pos(word, g_p):
    has_green_pos = np.array([False for key in g_p.keys()])
    for i, key in enumerate(g_p.keys()):
        pattern = re.compile(key)
        m = pattern.finditer(word)
        pos = [x.start() for x in m]
        check = np.in1d(g_p.get(key), pos)
        if check.all() == True:
            has_green_pos[i] = True
    if has_green_pos.all() == True:
        return True
    return False


def get_words():
    word_list = []
    with open(WORDS_FILE, "r") as f:
        for word in f:
            word = word.rstrip("\n")
            word_list.append(word)
    return word_list


def guess_word(word_len, sym_list, dead_sym, yellow_pos, green_pos):
    find_word = []
    words = get_words()
    for word in words:
        if len(word) == word_len:
            if find_symbols(word, sym_list):
                if has_dead_symbol(word, dead_sym):
                    pass
                else:
                    if accept_yellow_pos(word, yellow_pos):
                        if accept_green_pos(word, green_pos):
                            find_word.append(word)
        else:
            pass
    return find_word


def random_word(word_len):
    words = get_words()
    fine_word = []
    for word in words:
        if len(word) == word_len:
            fine_word.append(word)
    random_index = random.randint(0, len(fine_word) - 1)
    return fine_word[random_index]


def check_dead_sym():
    print("What letter in gray?")
    x = input()
    return list(x)


def check_yellow_sym(yellow_dict):
    print("Do you have yellow letter?")
    answer = input("y/n?")
    if answer == "y":
        print("What letter in yellow?")
        yellow_letter = input()

        for char in list(yellow_letter):
            print(f"In what position letter {char.upper()}?")
            pos = [int(val) - 1 for val in list(input("Begin from 1:"))]
            pos_in_dict = yellow_dict.get(char)
            if pos_in_dict:
                for value in pos:
                    pos_in_dict.append(value)
                yellow_dict[char] = pos_in_dict
            else:
                yellow_dict[char] = pos
    else:
        return False
    return yellow_dict


def check_green_sym(green_dict):
    print("Do you have green letter?")
    answer = input("y/n?")
    if answer == "y":
        print("What letter in green?")
        green_letter = input()
        for char in list(green_letter):
            print(f"In what position letter {char.upper()}?")
            pos = [int(val) - 1 for val in list(input("Begin from 1:"))]
            pos_in_dict = green_dict.get(char)
            if pos_in_dict:
                for value in pos:
                    pos_in_dict.append(value)
                green_dict[char] = pos_in_dict
            else:
                green_dict[char] = pos
    else:
        return False
    return green_dict


def check_win():
    print("We win?")
    answer = input("y/n?")
    if answer == "y":
        return True
    else:
        return False


def green_gray_intersect(dead_array, green_dict):
    dead_array_cp = [val for val in dead_array]
    pop_index = []
    for i, val in enumerate(dead_array):
        if val in green_dict.keys():
            pop_index.append(i)
    for i in pop_index[::-1]:
        dead_array_cp.pop(i)
    return dead_array_cp


def define_word_len():
    try:
        word_len = int(sys.argv[1])
    except IndexError:
        word_len = 5
    return word_len


def main():
    sym_list = []
    dead_sym = []
    yellow_pos = {}
    word_len = define_word_len()
    green_pos = {}
    won = False
    while not won:
        gaved_word = random_word(word_len)
        print(f"Try: {gaved_word} \n Is good?")
        answer = input("y/n?")
        if answer == "y":
            while not won:
                dead_list = check_dead_sym()
                if dead_list:
                    for sym in dead_list:
                        dead_sym.append(sym)
                print(f"Gray symbols: {dead_sym}")

                yellow_dict = check_yellow_sym(yellow_pos)
                if yellow_dict:
                    yellow_pos = yellow_dict
                    for key in yellow_dict.keys():
                        if key in sym_list:
                            pass
                        else:
                            sym_list.append(key)

                print(f"Yellow symbs: {yellow_pos}")
                print(f"seen char: {sym_list}")

                green_dict = check_green_sym(green_pos)
                if green_dict:
                    green_pos = green_dict
                if green_pos:
                    dead_sym = green_gray_intersect(dead_sym, green_pos)
                print(f"Green symbs: {green_pos}")

                find_word = guess_word(
                    word_len, sym_list, dead_sym, yellow_pos, green_pos
                )
                print("My guess is ...")
                print(find_word)
                won = check_win()
        else:
            continue
    print("My work done \U0001F388") 


if __name__ == "__main__":
    main()
