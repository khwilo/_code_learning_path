print "Let's practice everything."
print 'You\'d need to know \'bout escape with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\tWhere there is none.
"""

print "_______________"
print poem
print "_______________"

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars        = jelly_beans / 1000
    crates      = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)
#one_variable_for_all = secret_formula(start_point)

print "With  a starting point of: %d" % start_point
print "We'd have %d beans, %d jars and %d crates." % (beans, jars, crates)
#print "We'd have %d beans, %d jars and %d crates." % (one_variable_for_all)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)
