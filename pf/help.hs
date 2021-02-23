salut = ["a", "b", "c"]

nume = ["d", "e", "f"]

--applicative!
--[(++)] <=> salut <=> nume

--monade!
f saluturi nume_oameni = do
  salut <- saluturi
  nume <- nume_oameni
  let x = salut ++ nume
  return x

g x = do
  y <- x
  z <- y
  return z

-- monad fara do notation
f' saluturi nume_oameni =
  saluturi >>= (\salut -> nume_oameni >>= (\nume -> let x = salut ++ nume in return x))