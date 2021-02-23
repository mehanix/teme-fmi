import qualified Data.Foldable as F
import qualified Data.List as List

type Concept = String

type Definitie = String

type Categorie = String

data Enciclopedie = Intrare Concept Definitie | Lista Categorie [Enciclopedie]
  deriving (Show)

enc1 = Lista "animal" [Lista "mamifer" [Intrare "elefant" "acesta e un elefant", Intrare "caine" "acesta este un caine", Intrare "pisica" "aceasta este o pisica"], Intrare "zebra" "zebra este un animal"]

enc2 = Lista "Animal" [Lista "animal" [Intrare "Elefant" "acesta e un elefant", Intrare "caIne" "acesta este un caine"], Intrare "caine" "definitie"]

-- lower_compare a b =
-- parcurg (Intrare con def) = con
-- parcurg ()
-- parcurg (Lista cat [enc]) = parcurg enc
enc3 = Lista "a" [Intrare "b" "b", Intrare "c" "c"]

-- parcurg (Intrare cat desc) = [cat]
-- parcurg [] = []
-- parcurg [Lista cat enc] = parcurg enc
-- parcurg (Lista cat (h : t)) = (parcurg h) ++ (parcurg t)

f09cnParcurg (Intrare c desc) = c
f09cnParcurg (Lista cat (h : t)) = f09cnParcurg h

--b
-- Instance Eq Enciclopedie where
--     a == b = let pairs = zip (sort (f09cnParcurg a)) (sort(f09cnParcurg b)) in
--         sum [1| x<-pairs, (fst x) == (snd x)] == length (f09cnParcurg a)

--3
data C a = C [a] | T
  deriving (Show, Eq)

test3 = mempty <> C ['a', 'z'] == C ['a', 'z']

instance (Eq a) => Semigroup (C a) where
  (C a) <> (C b) = C (List.intersect a b)

instance (Eq a) => Monoid (C a) where
  mempty = T

-- instance F.Foldable C where
--   foldMap f (C []) = mempty
--   foldMap f x = f x
--   foldMap f (C (h : t)) = (F.foldMap f (h)) `mappend` (F.foldMap f (C t))
