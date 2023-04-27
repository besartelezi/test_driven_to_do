# This To-Do list is the GOAT
Following along a book called 'Obey The Testing Goat', I created this To-Do list.
And as you all know, a project made by a certified GOAT, is itself also the GOAT.


![the-goat](src/thats-why-hes-the-goat-the-goat.gif)


## Versions
This To-Do list was made in DJango 1.11.3 and python 3.6.

## Useful Commands
#### To run the functional tests

```python manage.py test functional_tests```

#### To run the unit tests

```python manage.py test lists```

## Unit Tests V.S. Functional Tests
Functional Tests are tests that are meant for the application as a whole, from the P.O.V. of the user.
Unit Tests are tests that are meant to test all the different functionalities.

![flowchart](src/flowchart.png)

## Design and Layout
It is best practice to not write tests for HOW the design/layout looks like.
You have to write tests to make sure IF they're properly loaded on the site.
This is especially important to pick up on problems for when you deploy your code to production.

Write minimal tests that make sure your design and layout are working, without testing **what** it actually is.