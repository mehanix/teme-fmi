
import System.Random

newtype MyRandom a = MyRandom { runRandom :: StdGen -> (a,StdGen) }

instance Functor MyRandom where
  fmap f ra = MyRandom rb
    where
      rb gen = (f a, gen')
        where
          (a,gen') = runRandom ra gen

randomPositive :: MyRandom Int
randomPositive = (MyRandom next)

randomBoundedInt :: Int -> MyRandom Int
randomBoundedInt = undefined

randomLetter :: MyRandom Char
randomLetter = undefined

random10LetterPair :: MyRandom (Int, Char)
random10LetterPair = undefined

