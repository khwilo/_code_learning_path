from collections import OrderedDict

favorite_languages = {
        'jen': ['python', 'ruby'],
        'sarah': ['c'],
        'edward': ['ruby', 'go'],
        'phil': ['python', 'haskell'],
        }

for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())


favorited_languages = OrderedDict()

favorited_languages['jen'] = 'python'
favorited_languages['sarah'] = 'c'
favorited_languages['edward'] = 'ruby'
favorited_languages['phil'] = 'python'

print("\n")

for name, language in favorited_languages.items():
    print(name.title() + "'s favorited language is " + 
            language.title() + ".")
