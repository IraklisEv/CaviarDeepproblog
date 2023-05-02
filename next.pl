:- use_module('next.py').
collect_all.
collect_all :- time(X), collect_all(X) == 0.
sorted_pair(X,N) :- collect_all, (X,N) = sort().
next(X, Y) :- sorted_pair(A,X), sorted_pair(A+1,Y).

