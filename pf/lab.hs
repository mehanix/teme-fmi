divizori n = filter (\x -> n `mod` x == 0) [1 .. n]

sumap n = foldr (\elem accum -> accum + elem * elem) 0 (divizori n)