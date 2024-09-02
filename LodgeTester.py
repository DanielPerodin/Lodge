# This is the client class. Here we will iterate through some kind of for-loop (lag from 1 day to 30 days) to test r-values
# for different lag times by calling on a function in the Lodge class.
from Lodge import *


Z = Lodge(0)
print(Z.run())