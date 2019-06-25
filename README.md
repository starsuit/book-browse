# Book Browse

A Django app which uses the Google Books API to allow a user search for and see information about books.

This has been quite the challenge for me - I have little more than beginner Python, and have never used it for the web. I've also never written a Django app before, so this has been a huge learning curve!

## My thought process

### Why I chose Django

I do not know much Python, and as I had a short timescale in which to build this project I did not feel comfortable building a server in 'vanilla' Python. I don't understand the language well enough to know when I would be making fundamental mistakes that would leave the site vulnerable or just broken. 

I soon came across Django as an option - having little idea of how I would get a Python site deployed on Heroku, I looked into their docs and found an example deployment which used Python with Django. Researching Django, I found that it was popular and well documented, and decided that as I was on unfamiliar ground, it made sense to follow a route that had been clearly documented with plenty of examples.

Although I feel like a spent a large amount of my time on DevOps and getting the framework deployed, Django takes care of a lot of the lower level processes that I did not feel comfortable writing myself, and allowed me to write the part I did understand: making an API call and templating the result on the page.

### Testing

I've written a few tests with the inbuilt Django testing library. There seem to be many different options for testing and I would like to learn more about them, but for now I've had to settle for some simple test cases (literally, I used the `SimpleTestCase` subclass...). These tests check my util function works, my url paths work and my html templates render correctly. 

### BEM

I've used the [BEM](http://getbem.com/) class naming convention to style my CSS.   

## Features I'd like to add

- [ ] Search by author / genre
- [ ] Filter / sort functionality
- [ ] 'Favourite' books
- [ ] Autocomplete on search


