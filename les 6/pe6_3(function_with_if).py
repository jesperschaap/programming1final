def lang_genoeg(lengte_in_cm):
    if lengte_in_cm>=120:
        return('je bent lang genoeg voor de attractie!')
    else:
        return('Sorry, je bent te klein')
print(lang_genoeg(120))