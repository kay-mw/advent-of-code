readLines path = do
  contents <- readFile path
  let contentLines = lines contents
  return contentLines

readInts :: [String] -> [Int]
readInts = map read

thd3 :: (a, b, c) -> c
thd3 (_, _, ywdawd) = ywdawd

main = do
  contentLines <- readLines "1/input.txt"
  let directions = map head contentLines

  let magnitudeStrings = map tail contentLines
  let magnitudes = readInts magnitudeStrings

  let directionMagnitude = zip directions magnitudes

  let directionMagnitudeClicks = map (\(x, y) -> (x, y, 0)) directionMagnitude
  -- let directionMagnitudeClicks = [('L', 82, 0), ('R', 95, 0), ('L', 95, 0), ('L', 30, 0), ('L', 82, 0), ('L', 12, 0), ('R', 39, 0), ('R', 16, 0), ('L', 18, 0), ('L', 89, 0), ('L', 24, 0), ('R', 31, 0)]
  -- let directionMagnitudeClicks = [('L', 51, 0), ('R', 2, 0), ('L', 102, 0), ('R', 202, 0), ('L', 302, 0), ('R', 402, 0), ('L', 502, 0), ('R', 602, 0), ('L', 702, 0), ('R', 802, 0), ('L', 902, 0)]
  -- let directionMagnitudeClicks = [('L', 50, 0), ('R', 100, 0), ('L', 200, 0), ('R', 300, 0), ('L', 400, 0), ('R', 500, 0), ('L', 600, 0), ('R', 700, 0), ('L', 800, 0), ('R', 900, 0), ('R', 1000, 0)]
  -- let directionMagnitudeClicks = [('R', 150, 0)]

  let detection =
        scanl
          ( \(accX, accY, accZ) (x, y, z) ->
              if x == 'L'
                then
                  ( if (accY - y) < 0
                      then
                        ( x,
                          if (100 - ((abs (accY - y)) `mod` 100)) == 100
                            then 0
                            else 100 - ((abs (accY - y)) `mod` 100),
                          if (accY == 0)
                            then abs ((accY - y) `div` 100) - 1
                            else abs ((accY - y) `div` 100)
                        )
                      else (x, accY - y, z)
                  )
                else
                  ( if (accY + y) > 100
                      then
                        ( x,
                          (accY + y) `mod` 100,
                          if (accY + y) `mod` 100 == 0
                            then ((accY + y) `div` 100) - 1
                            else (accY + y) `div` 100
                        )
                      else
                        ( x,
                          if accY + y == 100 then 0 else accY + y,
                          z
                        )
                  )
          )
          ('L', 50, 0)
          directionMagnitudeClicks

  let zeroes = map (\(x, y, z) -> if y == 0 then 1 else 0) detection
  let zeroesCount = sum zeroes

  let clicks = map (\(x, y, z) -> z) detection
  let clicksCount = sum clicks

  let final = zeroesCount + clicksCount

  let indices = [2 .. length detection + 2]
  let res = zipWith3 (\(_, dial, result) (direction, change, _) (i) -> if direction == 'L' then (dial, -change, thd3 $ detection !! (i - 1)) else (dial, change, thd3 $ detection !! (i - 1))) detection directionMagnitudeClicks indices

  print detection
  print res
  print final
