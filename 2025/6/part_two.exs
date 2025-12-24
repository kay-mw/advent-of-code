{:ok, file} = File.read("6/input.txt")
file = String.split(file, "\n")
file = for str <- file, str != "", do: String.split(str, "")

file =
  for li <- file do
    for str <- li do
      try do
        String.to_integer(str)
      rescue
        _e -> str
      end
    end
  end

file = Enum.zip(file) |> Enum.map(&Tuple.to_list/1)

numbers =
  for li <- file do
    Enum.reduce(li, 0, fn x, acc ->
      if is_integer(x) and is_integer(acc) do
        res = Integer.to_string(acc) <> Integer.to_string(x)
        String.to_integer(res)
      else
        acc
      end
    end)
  end

numbers = Enum.chunk_by(numbers, fn x -> x != 0 end)
numbers = Enum.filter(numbers, fn x -> x != [0] end)

operators = for li <- file, do: Enum.filter(li, fn x -> x == "+" or x == "*" end)
operators = Enum.filter(operators, fn x -> x != [] end)
operators = List.flatten(operators)

result =
  Enum.zip(numbers, operators)
  |> Enum.map(fn {number, operator} ->
    case operator do
      "*" -> Enum.reduce(number, fn x, acc -> x * acc end)
      "+" -> Enum.sum(number)
    end
  end)

result = Enum.sum(result)

IO.inspect(result, pretty: true)
