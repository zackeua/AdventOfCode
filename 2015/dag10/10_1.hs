next :: String -> Char -> Int -> String
next s c i | length s == 0 = (show i) ++ [c]
           | s!!0 == c = next (drop 1 s) c (i+1)
           | s!!0 /= c = (show i) ++ [c] ++ next (drop 1 s) (s!!0) 1
           
iter :: Int -> String -> String
iter i s | i == 0 = s
            | otherwise = iter (i-1) (next s (s!!0) 0)

main :: IO ()
main = do
    let s = "1321131112"
    print $ length $ iter 40 s