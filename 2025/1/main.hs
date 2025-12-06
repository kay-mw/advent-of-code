readLines path = do
  contents <- readFile path
  let contentLines = lines contents
  return contentLines

readInts :: [String] -> [Float]
readInts = map read

count :: (Eq a) => a -> [a] -> Int
count x = length . filter (== x)

main = do
  contentLines <- readLines "1/input.txt"
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
                          max (abs (fromIntegral (round ((accY - y) / 100) * 100))) 100 + (fromIntegral (round (accY) - round (y)))
                        )
                      else (x, accY - y)
                  )
                else
                  ( if (accY + y) > 99
                      then (x, abs (fromIntegral (floor ((accY + y) / 100) * 100) - (fromIntegral (round (accY) + round (y)))))
                      else (x, accY + y)
                  )
          )
          ('L', 50.0)
          directionMagnitude

  let zeroes = map (\(x, y) -> if y == 0.0 then 1 else 0) detection
  let zeroesCount = count 1 zeroes

  print zeroesCount
