import Data.Char

next :: [(Int, Char)] -> [(Int, Char)]
next [] = []
next ((num, c):xs) | (show num)!!0 == c = (2, c):next xs
                   | otherwise = (1, (show num)!!0):(1, c):next xs


merge :: [(Int, Char)] -> [(Int, Char)]
merge [] = []
merge ((num1,a):(num2,b):xs) |a == b = (num1+num2, a):merge xs
merge (x:xs) = x:merge xs


strToTup :: String -> Char -> Int -> [(Int, Char)]
strToTup s c i | length s == 0 = [(i, c)]
               | s!!0 == c = strToTup (drop 1 s) c (i+1)
               | s!!0 /= c = (i, c) : strToTup (drop 1 s) (s!!0) 1

iter :: Int -> [(Int, Char)] -> Int
iter 0 t = foldl (\b a-> b + fst a) 0 t
iter i t = iter (i-1) (merge (next t))

iter1 :: Int -> [(Int, Char)] -> [(Int, Char)]
iter1 0 t = t
iter1 i t = iter1 (i-1) (merge (next t))
{-- 
"111" -> (3, '1')

"1" -> (1, '1')
"11" -> (2, '1')
"21" -> (1, '2') : (1, '1')
"1211" -> (1, '1') : (1, '2') : (2, '1')
"111221" -> (2, '1') : (1, '1') : (1, '2') : (1, '2') : (1, '1') 
"312211" -> 
--}





main :: IO ()
main = do
    let s = "1321131112"
    --let s = "1"
    let t = strToTup s (s!!0) 0
    print $ iter 50 t