import qualified Data.List as List
import Prelude hiding (lookup)

class Collection c where
  empty :: c key value
  singleton :: key -> value -> c key value
  insert ::
    Ord key =>
    key ->
    value ->
    c key value ->
    c key value
  lookup :: Ord key => key -> c key value -> Maybe value
  delete :: Ord key => key -> c key value -> c key value
  keys :: c key value -> [key]
  keys collection = [fst x | x <- toList collection]
  values :: c key value -> [value]
  values collection = [snd x | x <- toList collection]
  toList :: c key value -> [(key, value)]
  fromList :: Ord key => [(key, value)] -> c key value
  fromList lst = foldr (Prelude.uncurry insert) empty lst

newtype PairList k v = PairList {getPairList :: [(k, v)]}

instance Collection PairList where
  empty = PairList []
  singleton k v = PairList [(k, v)]
  insert k v c = PairList ((k, v) : toList c)
  toList (PairList a) = a
  lookup k c =
    let res = [p | p <- toList c, fst p == k]
     in if length res == 0 then Nothing else Just (snd (head res))
  delete k c = fromList (foldr (\x acc -> if fst x == k then acc else x : acc) [] (toList c))

data SearchTree key value
  = Empty
  | Node
      (SearchTree key value) -- elemente cu cheia mai mica
      key -- cheia elementului
      (Maybe value) -- valoarea elementului
      (SearchTree key value) -- elemente cu cheia mai mare

order = 1

data Element k v
  = Element k (Maybe v)
  | OverLimit

data BTree key value
  = BEmpty
  | BNode [(BTree key value, Element key value)]
