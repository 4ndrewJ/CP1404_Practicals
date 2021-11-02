import wikipedia


search = input('Enter page title / search phrase: ')
while search != '':
    try:
        page = wikipedia.page(search)
        print(page.title)
        print(page.summary)
        print(page.url)
    except wikipedia.exceptions.DisambiguationError as e:
        print('Please enter a more specific search phrase, such as:')
        for option in e.options[:5]:
            print(option)
    except wikipedia.exceptions.PageError:
        print('Page does not exist')
    search = input('Enter page title / search phrase: ')
