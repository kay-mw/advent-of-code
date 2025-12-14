readLines path = do
  contents <- readFile path
  let contentLines = lines contents
  return contentLines

readInts :: [String] -> [Int]
readInts = map read

count :: (Eq a) => a -> [a] -> Int
count x = length . filter (== x)

main = do
  contentLines <- readLines "1/example.txt"
  let directions = map head contentLines

  let magnitudeStrings = map tail contentLines
  let magnitudes = readInts magnitudeStrings

  let directionMagnitude = zip directions magnitudes

  let detection =
        scanl
          ( \(accX, accY) (x, y) ->
              if x == 'L'
                then
                  ( if (accY - y) < 0
                      then
                        ( x,
                          if (100 - (abs (accY - y)) `mod` 100) == 100
                            then 0
                            else 100 - (abs (accY - y)) `mod` 100
                        )
                      else (x, accY - y)
                  )
                else
                  ( if (accY + y) > 100
                      then
                        ( x,
                          (accY + y) `mod` 100
                        )
                      else
                        ( x,
                          if accY + y == 100
                            then 0
                            else accY + y
                        )
                  )
          )
          ('L', 50)
          directionMagnitude

  let zeroes = map (\(x, y) -> if y == 0 then 1 else 0) detection
  let zeroesCount = count 1 zeroes

  -- let res = zipWith (\(_, dial) (direction, change) -> if direction == 'L' then (dial, -change) else (dial, change)) detection directionMagnitude

  print detection
  print zeroesCount

-- print res

-- putStrLn "\n"
-- print directionMagnitude
-- putStrLn "\n"
-- print detection
-- putStrLn "\n"
-- print zeroesCount
