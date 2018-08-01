This is a script that is able to produce all positive combinations of the N-Queens game, save it to a postgresql database and prints it.
It's runtime is of a couple of seconds until the number of queens is > 12. 
The number of queens is a variable editable in line 12.


You should be able to run it using docker-compose up and then python generatequeens.py

Running tests:
Tests were hardcoded for the first 8 sizes of boards.  
pytest generatequeens.py
