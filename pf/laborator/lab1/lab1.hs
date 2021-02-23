import Data.List

myInt = 5555555555555555555555555555555555555555555555555555555555555555555555555555555555555

double :: Integer -> Integer
  double x = x+x
triple x = x+x+x

--maxim :: Integer -> Integer -> Integer
maxim x y = if (x > y)
               then x
          else y

max3 x y z = let
             u = maxim x y
             in (maxim  u z)
             
max4 x y z t = let
				u = maxim x y
				in (let v = maxim u z in
						(let w = maxim v t )) 

               
