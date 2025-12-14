open("3/input.txt", "r") do f
  contents = read(f, String)
  contentlines = split(contents, "\n")

  joltages = []
  for line in contentlines
    if line != "" 
      num = parse(BigInt, line)
      dig = reverse(digits(num, base = 10))
      len = length(dig)
      max_val = findmax(dig)
      val = max_val[1]
      index = max_val[2]
      if index == len
	max_val = findmax(dig[1:len-1])
	val = max_val[1]
	index = max_val[2]
      end
      second_max_val = findmax(dig[index+1:len])

      joltage = parse(Int64, string(val, second_max_val[1]))
      push!(joltages, joltage)
    end
  end

  println(sum(joltages))
end
