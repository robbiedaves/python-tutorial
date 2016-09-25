class IfsAndLoops:

    def ifs_and_loops_demo(self):

        # if statements, if elif elif is a substitute for switch case statements
        x = -5
        if x < 0:
            x = 0
            print('Negative changed to zero')
        elif x == 0:
            print('Zero')
        elif x == 1:
            print('single')
        else:
            print('More')

        # for loops
        # for loops do not iterate over a number sequence but iterate over items in a sequence
        words = ['cat', 'window', 'defenestrate']
        for w in words:
            print(w, len(w))

        # If you need to modify the sequence you are iterating over while inside the loop
        # (for example to duplicate selected items),
        # it is recommended that you first make a copy.
        # Iterating over a sequence does not implicitly make a copy.
        # The slice notation makes this especially convenient:
        for w in words[:]:      # Loop over a slice copy of the entire list.
            if len(w) > 6:
                words.insert(0, w)
        print(words)

        # if you need to iterate over a sequence of numbers , the built in range() can be used
        for i in range(5):
            print(i)            # prints 0 1 2 3 4

        # makes the range start from a starting position to the ending position
        for j in range(5, 10):
            print(j)            # prints 5 6 7 8 9

        # sets a start and end position, with an increment step (in this case -30)
        for k in range(-10, -100, -30):
            print(k)            # prints -10 -40 -70

        # To iterate over the indices of a sequence, you can combine range() and len() as follows:
        sentence = ['Mary', 'had', 'a', 'little', 'lamb']
        for l in range(len(sentence)):
            print(l, sentence[l])

        # In most such cases, however, it is convenient to use the enumerate() function, see Looping Techniques.

        # break and continue Statements, and else Clauses on Loops
        for n in range(2, 10):
            for x in range(2, n):
                if n % x == 0:
                    print(n, 'equals', x, '*', n//x)
                    break
            else:       # This else statement is connected to the for loop not the if statement
                # loop fell through without finding a factor
                print(n, 'is a prime number')
        # When used with a loop, the else clause has more in common with the else clause of a try statement,
        # than it does that of if statements: a try statement’s else clause runs when no exception occurs,
        # and a loop’s else clause runs when no break occurs.

        # The continue statement, also borrowed from c, continues with the next iteration of the loop
        if __name__ == '__main__':
            for num in range(2, 10):
                if num % 2 == 0:
                    print("Found an even number", num)
                    continue
                print("Found a number", num)

        # pass statement - the pass statement does nothing
        #  it can be used when a statement is required syntactically but the program requires no action
        for nx in range(100):
            pass    # does nothing

        

