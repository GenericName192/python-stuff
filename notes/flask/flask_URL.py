# When programs become more complex the pathing for pages, may become long or 
# change, this can be fixed using the url_for() function. You write it like:

# <a href="{{ url_for('my_page', id=1) }}">One</a>

# To break down the above, we have url_for() returning the pathing for the page
# "my_page" then after the , we are passing arguements to it. So this works the
# same as writing:

# <a href="/my_page/<int:id">Link</a>