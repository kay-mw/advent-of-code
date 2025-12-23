{:ok, file} = File.read("6/input.txt")
file = String.split(file, "\n")
file = for str <- file, str != "", do: String.split(str)
file = Enum.zip(file) |> Enum.map(&Tuple.to_list/1)

result = for tup <- file do
  operator = List.last(tup)
  tup = for val <- tup, val != "*" and val != "+", do: String.to_integer(val)
  case operator do
    "*" -> Enum.reduce(tup, fn x, acc -> x * acc end)
    "+" -> Enum.sum(tup)
  end

end

answer = Enum.sum(result)

IO.inspect(answer)
