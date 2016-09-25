class Strings:

    @staticmethod
    def strings_demo():

        # strings cal be in single quotes '...' or double quotes "..."
        a = 'single quotes'
        print(a)
        b = "double quotes"
        print(b)

        # mix single and double quotes
        c = 'using "double" quotes inside single quotes'    # using "double" quotes inside single quotes
        print(c)

        # use backslash \ as an escape character
        d = 'doesn\'t'                                      # doesn't
        print(d)

        # newline
        e = 'First line \nSecond line'
        print(e)
        f = 'C:\some\name'      # because \n is newline this prints c:\some and ame on the next line
        print(f)
        g = r'C:\some\name'     # notice the r before the quotes. This uses the raw string and outputs correctly
        print(g)

        # multi line strings - use """...""" Prevent the newline using escape character \
        h = """\
        Usage: thing [OPTIONS]
                -h
                -H hostname
        """
        print(h)

        # concatenate and repeated strings using + and *
        i = 3 * 'three ' + 'one '       # result is 'three three one'
        print(i)
        j = 'Py' 'thon'                 # two string literals together are automatically concatenated
        print(j)                        # Note: only works for literals and not variables

        # strings can be indexed (subscripted)
        word = 'Python'
        print(word[0])      # character in position 0   'P'
        print(word[5])      # character in position 5   'n'
        print(word[-1])     # use negative values to start counting from the right. [-1] last character 'n'
        print(word[-2])     # second-last character 'o'
        print(word[-6])     # 'P'

        # substring using slicing
        print(word[0:2])    # characters from position 0 (including) to 2 (excluding)   'Py'
        print(word[2:5])    # characters from position 2 (including) to 5 (excluding)   'tho'
        # Note how the start is always including, and the end is always excluding, which allows:
        print(word[:2] + word[2:])  # notice [:2] and [2:]
        print(word[:2])     # characters from the beginning to position 2 (excluded)    'Py'
        print(word[4:])     # characters from position 4 (including) to the end         'on'
        print(word[-2:])    # characters from second-last (including to the end         'on'
        # Think of slices as:
        #  +---+---+---+---+---+---+
        #  | P | y | t | h | o | n |
        #  +---+---+---+---+---+---+
        #  0   1   2   3   4   5   6
        # -6  -5  -4  -3  -2  -1

        # strings cannot be changed
        # word[0] = 'J'    # this will cause a runtime error
        # instead you need to create a new string
        new_word = 'J' + word[1:]   # will produce Jython
        print(new_word)

        # String lengths
        s = 'this is a string with length 31'
        length = len(s)
        print(length)
