# brute-force-searching
Scripts for brute force searching certain things.

## find-+X-sol.py
Program that attempts to find a solution for programs stated in [this codegolf challenge](https://codegolf.stackexchange.com/questions/287678/generate-a-large-number-using-and-%C3%97) given a program length to start from and a number to output. With no prior knowledge, you should start from programs of length `floor(log_2(log_2(n))) + 1` where `n` is the target number. This is guaranteed to terminate because there will always be a program of length `n-1` that outputs the target number by just adding 1 each time.
