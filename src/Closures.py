# This is a simple example of a closure
def outer_func(msg):
    message = msg

    def inner_func():
        print(message)

    return inner_func  # This returns the function and not the result of calling the function (no brackets)

# The inner func is returned and it has 'closed' over the message variable
# now the variable, even though it is not inside the scope of inner_func is available when outer_func is called below

hi_func = outer_func('hi')
hello_func = outer_func('hello')

hi_func()
hello_func()


# A better example to show closures in practice is the following example
def html_tag(tag):
    def wrap_text(msg):
        return '<' + tag + '>' + msg + '</' + tag + '>'
    return wrap_text

h1_tag = html_tag('h1')
p_tag = html_tag('p')

print(h1_tag('This is a heading h1 string'))
print(p_tag('This is a paragraph is the p tag'))
