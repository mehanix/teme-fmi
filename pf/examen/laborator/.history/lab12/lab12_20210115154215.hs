
import System.Random

newtype MyRandom a = MyRandom { runRandom :: StdGen -> (a,StdGen) }

randomPositive :: MyRandom Int
randomPositive = (MyRandom next)

instance Functor MyRandom where
  fmap f ra = MyRandom rb
    where
      rb gen = (f a, gen')
        where
          (a,gen') = runRandom ra gen

randomBoundedInt :: Int -> MyRandom Int
randomBoundedInt n = fmap (`mod` n) randomPositive

randomLetter :: MyRandom Char
randomLetter = fmap toChar (randomBoundedInt 26)
  where
    toChar n = chr (ord 'a' + n)    

random10LetterPair :: MyRandom (Int, Char)
random10LetterPair = undefined

