# Notite

## Functori

```
instance Functor f where
	fmap (a->b) f a -> f b

ai functie a->b, o cutie de a-uri si returneaza o cutie de b-uri

alta notatie: (a->b) <$> f a (returneaza f b)
```

## Applicative

```
E util sa ai functorul deja facut pt ca il poti folosi
instance Applicative f where
  pure :: a -> f a
  (<*>) :: f (a -> b) -> f a -> f b
  
ai o cutie cu o functie (a->b), o cutie cu a-uri si primesti cutie de b-uri

exemplu:
Just (+3) <*> (Just 5) -> Just 8

E util ca poti folosi fmap de multe ori pt a-l defini pe <*> ca gen
Just f <*> j = fmap f j
e acelasi lucru cu
Just f <*> (Just x) = Just (f x)
```

## Monade
```
instance Monad m where
  (>>=) :: m a -> (a -> m b) -> m b
 
Practic, ai operatorul de bind de mai sus care aplicat intre o cutie si o functie de la valoare simpla la cutie, scoate valoarea din cutie si aplica functia
Exemplu:

Just 5 >>= (+3) -> Just 8
 Spre deosebire de Functor, functia e de la (a->m b) nu de la (m a -> m b), >>= despacheteaza monada din stanga.
 
Tre sa ai Applicative creat ca sa poti face monad. Cred ca si Functor.

Ai si do notation
 do
    x <- ...
    y <- ...
    return x+y
```


## Semigroup
```
O multime cu o operatie <> asociativa
class Semigroup a where
  (<>) :: a -> a -> a
```

## Monoid
```
Semigrup + mempty
mappend -> alias pentru <>

Class Semigroup a => Monoid a where
  mempty :: a
  mappend :: a -> a -> a
  mappend = (<>)
```
