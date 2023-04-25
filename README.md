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
So as far as I understand it: 
1. You start with writing a unit test for a feature you'd like to add.
1. You add said feature.
1. Check the test again and see if you can add on to it and improve upon it.
1. In case you did, then rewrite your code until the code passes the test.
1. Repeat those steps until you have a very bare-boned version of the app.
1. Write a functional test to see if application works.
    1. The functional test should be written while following along to a user story which will be added in comments
1. Rewrite code in case functional test results in an error
1. On success, write a new unit test for the next feature on the app.r