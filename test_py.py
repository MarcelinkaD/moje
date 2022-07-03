def between_markers(t: str, b: str, e: str) -> str:
    try:
        indexb = t.index(b)
    except ValueError:
        indexb = -1
    
    try:
        indexe = t.index(e)
    except ValueError:
        indexe = -1
    
    if indexb != -1 and indexe != -1:
        if len(str(b)) != 1:
            return t[indexb + len(str(b)) - 1 : indexe]
        else:
            return t[indexb + 1 : indexe]
    elif indexb == -1 and indexe != -1:
        return t[0 : indexe]
    elif indexb != -1 and indexe == -1:
        return t[indexb + 1 : len(t)]
        
    

if __name__ == '__main__':
    print('Example:')
   

    # These "asserts" are used for self-checking and not for testing

    breakpoint()
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')
