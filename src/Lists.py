class Lists:

    @staticmethod
    def lists_demo():

            # Lists can have items of different types, but usually contain the same types
            squares = [1, 4, 9, 16, 25]
            print(squares)          # prints [1, 4, 9, 16, 25]

            # Lists can be indexed and sliced
            print(squares[0])       # prints 1
            print(squares[-1])      # prints 25
            print(squares[-3:])     # prints [9, 16, 25]

            # All slice operations return a new list containing the requested elements
            new_squares = squares[:]
            print(new_squares)       # prints [1, 4, 9, 16, 25]

            # Lists also support operations like concatenation
            print(squares + [36, 49, 64, 81, 100])  # prints [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

            # Unlike strings, which are immutable, lists are mutable types i.e. you can change the content
            cubes = [1, 8, 27, 65, 125]
            print(cubes)                    # prints [1, 8, 27, 65, 125]
            cubes[3] = 64                   # however, 4 ** 3 is 64 not 65, so fix this
            print(cubes)                    # prints [1, 8, 27, 64, 125]

            # Add new items to the end using the append method
            cubes.append(216)       # adds the cube of 6
            cubes.append(7 ** 3)    # adds the cube of 7
            print(cubes)            # prints [1, 8, 27, 64, 125, 216, 343]

            # Assignment to slices is also possible, and this can even change the size of the list or clear it entirely
            letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
            print(letters)
            # replace some values
            letters[2:5] = ['C', 'D', 'E']
            print(letters)      # prints ['a', 'b', 'C', 'D', 'E', 'f', 'g']
            # now remove them
            letters[2:5] = []
            print(letters)      # prints ['a', 'b', 'f', 'g']
            # clears the list by replacing all elements with an empty list
            letters[:] = []
            print(letters)      # prints []

            # The built in len method also works on lists
            numbers = [1, 2, 3, 4, 5]
            print(len(numbers))     # prints 5

            # You can also nest lists (create lists containing lists)
            a = ['a', 'b', 'c']
            n = [1, 2, 3]
            x = [a, n]
            print(x)            # prints [['a', 'b', 'c'], [1, 2, 3]]
            print(x[0])         # prints ['a', 'b', 'c']

            # the in statement
            answers = ['y', 'ye', 'yes']
            answer_one = 'yes'
            answer_two = 'yea'
            if answer_one in answers:
                print(answer_one, 'is one of the answers', answers)
            else:
                print(answer_one, 'is not one of the answers', answers)
            if answer_two in answers:
                print(answer_two, 'is one of the answers', answers)
            else:
                print(answer_two, 'is not one of the answers', answers)
