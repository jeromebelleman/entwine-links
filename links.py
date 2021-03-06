def tweet(account, inline=False):
    '''
    Print Tweet button
    '''

    if not inline:
        print '<p>'
    print '<a href="https://twitter.com/share" class="twitter-share-button" data-via="%s" data-show-count="false">Tweet</a><script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>' % account # pylint: disable=line-too-long
    if not inline:
        print '</p>'

def follow(account, inline=False):
    '''
    Print Follow button
    '''

    if not inline:
        print '<p>'
    print '<a href="https://twitter.com/%s" class="twitter-follow-button" data-show-count="false">Follow @%s</a><script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>' % (account, account) # pylint: disable=line-too-long
    if not inline:
        print '</p>'

def wiki(article):
    '''
    Print Wikipedia link
    '''

    print 'https://en.wikipedia.org/wiki/' + article
