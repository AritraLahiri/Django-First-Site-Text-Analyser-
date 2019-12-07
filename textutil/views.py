# # I have created this Website - Aritra Lahiri
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyse(request):

    # Get the text
    user_text = request.POST.get('text', 'default')
    # CheckboX Value
    punc = request.POST.get('punc', 'off')
    capz = request.POST.get('uppercase', 'off')
    new_line = request.POST.get('newline', 'off')
    space_remove = request.POST.get('remove_space', 'off')
    char_count = request.POST.get('char_count', 'off')
    # Punctuation List
    punc_lst = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    # Final Result to Show
    characs = 0

    if punc == 'on':
        # Removes Punctuations from string
        res = ''
        for letters in user_text:
            if letters not in punc_lst:
                res += letters
        user_text = res
        params = {'purpose': 'Removed Punctuations', 'analysed_text': res}

    if capz == 'on':
        res = ''
        # Capitalizes the whole string
        res = user_text.upper()
        user_text = res
        params = {'purpose': 'Capitalized', 'analysed_text': res}

    if new_line == 'on':
        res = ''
        # Removes new line characters
        for letters in user_text:
            if letters != '\n' and letters != "\r":
                res += letters
        user_text = res
        params = {'purpose': 'Removed Newlines', 'analysed_text': res}

    if space_remove == "on":
        res = ''
        # Removes Spaces from string
        for index, letters in enumerate(user_text):
            if user_text[index] == " " and user_text[index+1] == " ":
                pass
            else:
                res += letters
        user_text = res
        params = {'purpose': 'Removed Extra Spaces', 'analysed_text': res}

    if char_count == "on":
        res = 'Total Number of Characters is: '
        # Counts no of Charcters in string
        for letters in user_text:
            if letters != " ":
                characs += 1
        res += str(characs)
        user_text = res
        params = {'purpose': 'Number of Characters are', 'analysed_text': res}

    else:
        # Does Nothing
        res = ''
        res = user_text

    return render(request, 'punc.html', params)


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')
