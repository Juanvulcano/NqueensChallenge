#Recursive solution
import unittest
from math import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base



x = {}
numberqueens = 8
solutions = []

def place(k, i):
    if (i in x.values()):
        return False
    j = 1
    while(j < k):
        if abs(x[j]-i) == abs(j-k):
            return False
        j+=1
    return True

def clear_future_blocks(k):
    for i in range(k,numberqueens+1):
       x[i]=None

def NQueens(k):
    for i in range(1, numberqueens + 1):
        clear_future_blocks(k)
        if place(k, i):
            x[k] = i
            if (k==numberqueens):
                solution = []
                for j in x:
                    solution.append(x[j])
                solutions.append(solution)
            else:
                NQueens(k+1)
NQueens(1)








Base = declarative_base()

# Fails when initial value is null, it should be able to work with a default value but I'm doing something wrong
class Solution(Base):
    __tablename__ = 'solutions'
    id=Column(Integer, primary_key=True)
    _coordinates=Column('db.String', default=0.0)
    @property
    def coordinates(self):
        return [int(x) for x in self._coordinates.split(';')]
    @coordinates.setter
    def coordinates(self, value):
        try:
            self._coordinates += ';%s' % value
            if self._coordinates[0:2] == "0;":
            	self._coordinates = self._coordinates[2:]
        except TypeError:
        	self._coordinates = "0"


engine = create_engine('postgresql://postgres:pass@localhost:32768/nqueen')
metadata = MetaData(engine)
# Declare a table
table = Table('solutions',metadata,
              Column('id',Integer, primary_key=True),
              Column('db.String',String))

# Create all tables
metadata.create_all()

Session = sessionmaker(bind=engine)

session = Session()
for coordinate in solutions:
    conn = engine.connect()
    solve = Solution()
    for queen in coordinate:
        solve.coordinates = str(queen)
    session.add(solve)
session.commit()
conn.close()
engine.dispose()




print(solutions)
def test_queens():
    if numberqueens == 1:
        assert(solutions == [[1]])
    elif numberqueens == 2:
    	assert(solutions == [])
    elif numberqueens ==3:
        assert(solutions == [])
    elif numberqueens ==4:
    	assert(sorted(solutions) == sorted([[2, 4, 1, 3], [3, 1, 4, 2]]))
    elif numberqueens ==5:
    	assert(sorted(solutions) == sorted([[1, 3, 5, 2, 4], [1, 4, 2, 5, 3], [2, 4, 1, 3, 5], [2, 5, 3, 1, 4],
    		[3, 1, 4, 2, 5], [3, 5, 2, 4, 1], [4, 1, 3, 5, 2], [4, 2, 5, 3, 1], [5, 2, 4, 1, 3], [5, 3, 1, 4, 2]]))
    elif numberqueens == 6:
    	assert(sorted(solutions) == sorted([[2, 4, 6, 1, 3, 5], [3, 6, 2, 5, 1, 4], [4, 1, 5, 2, 6, 3], [5, 3, 1, 6, 4, 2]]))
    elif numberqueens == 7:
    	assert(sorted(solutions) == sorted([[1, 3, 5, 7, 2, 4, 6], [1, 4, 7, 3, 6, 2, 5], [1, 5, 2, 6, 3, 7, 4], 
    		[1, 6, 4, 2, 7, 5, 3], [2, 4, 1, 7, 5, 3, 6], [2, 4, 6, 1, 3, 5, 7], [2, 5, 1, 4, 7, 3, 6], [2, 5, 3, 1, 7, 4, 6],
    		[2, 5, 7, 4, 1, 3, 6], [2, 6, 3, 7, 4, 1, 5], [2, 7, 5, 3, 1, 6, 4], [3, 1, 6, 2, 5, 7, 4], [3, 1, 6, 4, 2, 7, 5],
    		[3, 5, 7, 2, 4, 6, 1], [3, 6, 2, 5, 1, 4, 7], [3, 7, 2, 4, 6, 1, 5], [3, 7, 4, 1, 5, 2, 6], [4, 1, 3, 6, 2, 7, 5],
    		[4, 1, 5, 2, 6, 3, 7], [4, 2, 7, 5, 3, 1, 6], [4, 6, 1, 3, 5, 7, 2], [4, 7, 3, 6, 2, 5, 1], [4, 7, 5, 2, 6, 1, 3],
    		[5, 1, 4, 7, 3, 6, 2], [5, 1, 6, 4, 2, 7, 3], [5, 2, 6, 3, 7, 4, 1], [5, 3, 1, 6, 4, 2, 7], [5, 7, 2, 4, 6, 1, 3],
    		[5, 7, 2, 6, 3, 1, 4], [6, 1, 3, 5, 7, 2, 4], [6, 2, 5, 1, 4, 7, 3], [6, 3, 1, 4, 7, 5, 2], [6, 3, 5, 7, 1, 4, 2],
    		[6, 3, 7, 4, 1, 5, 2], [6, 4, 2, 7, 5, 3, 1], [6, 4, 7, 1, 3, 5, 2], [7, 2, 4, 6, 1, 3, 5], [7, 3, 6, 2, 5, 1, 4],
    		[7, 4, 1, 5, 2, 6, 3], [7, 5, 3, 1, 6, 4, 2]]))
    elif numberqueens == 8:
        assert(solutions == [[1, 5, 8, 6, 3, 7, 2, 4], [1, 6, 8, 3, 7, 4, 2, 5], [1, 7, 4, 6, 8, 2, 5, 3],
            [1, 7, 5, 8, 2, 4, 6, 3], [2, 4, 6, 8, 3, 1, 7, 5], [2, 5, 7, 1, 3, 8, 6, 4], [2, 5, 7, 4, 1, 8, 6, 3], 
            [2, 6, 1, 7, 4, 8, 3, 5], [2, 6, 8, 3, 1, 4, 7, 5], [2, 7, 3, 6, 8, 5, 1, 4], [2, 7, 5, 8, 1, 4, 6, 3], 
            [2, 8, 6, 1, 3, 5, 7, 4], [3, 1, 7, 5, 8, 2, 4, 6], [3, 5, 2, 8, 1, 7, 4, 6], [3, 5, 2, 8, 6, 4, 7, 1], 
            [3, 5, 7, 1, 4, 2, 8, 6], [3, 5, 8, 4, 1, 7, 2, 6], [3, 6, 2, 5, 8, 1, 7, 4], [3, 6, 2, 7, 1, 4, 8, 5], 
            [3, 6, 2, 7, 5, 1, 8, 4], [3, 6, 4, 1, 8, 5, 7, 2], [3, 6, 4, 2, 8, 5, 7, 1], [3, 6, 8, 1, 4, 7, 5, 2], 
            [3, 6, 8, 1, 5, 7, 2, 4], [3, 6, 8, 2, 4, 1, 7, 5], [3, 7, 2, 8, 5, 1, 4, 6], [3, 7, 2, 8, 6, 4, 1, 5], 
            [3, 8, 4, 7, 1, 6, 2, 5], [4, 1, 5, 8, 2, 7, 3, 6], [4, 1, 5, 8, 6, 3, 7, 2], [4, 2, 5, 8, 6, 1, 3, 7], 
            [4, 2, 7, 3, 6, 8, 1, 5], [4, 2, 7, 3, 6, 8, 5, 1], [4, 2, 7, 5, 1, 8, 6, 3], [4, 2, 8, 5, 7, 1, 3, 6], 
            [4, 2, 8, 6, 1, 3, 5, 7], [4, 6, 1, 5, 2, 8, 3, 7], [4, 6, 8, 2, 7, 1, 3, 5], [4, 6, 8, 3, 1, 7, 5, 2], 
            [4, 7, 1, 8, 5, 2, 6, 3], [4, 7, 3, 8, 2, 5, 1, 6], [4, 7, 5, 2, 6, 1, 3, 8], [4, 7, 5, 3, 1, 6, 8, 2], 
            [4, 8, 1, 3, 6, 2, 7, 5], [4, 8, 1, 5, 7, 2, 6, 3], [4, 8, 5, 3, 1, 7, 2, 6], [5, 1, 4, 6, 8, 2, 7, 3], 
            [5, 1, 8, 4, 2, 7, 3, 6], [5, 1, 8, 6, 3, 7, 2, 4], [5, 2, 4, 6, 8, 3, 1, 7], [5, 2, 4, 7, 3, 8, 6, 1], 
            [5, 2, 6, 1, 7, 4, 8, 3], [5, 2, 8, 1, 4, 7, 3, 6], [5, 3, 1, 6, 8, 2, 4, 7], [5, 3, 1, 7, 2, 8, 6, 4], 
            [5, 3, 8, 4, 7, 1, 6, 2], [5, 7, 1, 3, 8, 6, 4, 2], [5, 7, 1, 4, 2, 8, 6, 3], [5, 7, 2, 4, 8, 1, 3, 6], 
            [5, 7, 2, 6, 3, 1, 4, 8], [5, 7, 2, 6, 3, 1, 8, 4], [5, 7, 4, 1, 3, 8, 6, 2], [5, 8, 4, 1, 3, 6, 2, 7], 
            [5, 8, 4, 1, 7, 2, 6, 3], [6, 1, 5, 2, 8, 3, 7, 4], [6, 2, 7, 1, 3, 5, 8, 4], [6, 2, 7, 1, 4, 8, 5, 3], 
            [6, 3, 1, 7, 5, 8, 2, 4], [6, 3, 1, 8, 4, 2, 7, 5], [6, 3, 1, 8, 5, 2, 4, 7], [6, 3, 5, 7, 1, 4, 2, 8], 
            [6, 3, 5, 8, 1, 4, 2, 7], [6, 3, 7, 2, 4, 8, 1, 5], [6, 3, 7, 2, 8, 5, 1, 4], [6, 3, 7, 4, 1, 8, 2, 5], 
            [6, 4, 1, 5, 8, 2, 7, 3], [6, 4, 2, 8, 5, 7, 1, 3], [6, 4, 7, 1, 3, 5, 2, 8], [6, 4, 7, 1, 8, 2, 5, 3], 
            [6, 8, 2, 4, 1, 7, 5, 3], [7, 1, 3, 8, 6, 4, 2, 5], [7, 2, 4, 1, 8, 5, 3, 6], [7, 2, 6, 3, 1, 4, 8, 5], 
            [7, 3, 1, 6, 8, 5, 2, 4], [7, 3, 8, 2, 5, 1, 6, 4], [7, 4, 2, 5, 8, 1, 3, 6], [7, 4, 2, 8, 6, 1, 3, 5], 
            [7, 5, 3, 1, 6, 8, 2, 4], [8, 2, 4, 1, 7, 5, 3, 6], [8, 2, 5, 3, 1, 7, 4, 6], [8, 3, 1, 6, 2, 5, 7, 4], 
            [8, 4, 1, 3, 6, 2, 7, 5]])
