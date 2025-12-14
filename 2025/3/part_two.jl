# Find the most significant digit that has at least 11 digits after it.
# For the digits after it, do the same thing, whilst decrementing the number of allowable digits.
#
# So with 234234234234278, valid first digits are:
# [2342]34234234278
# So you select 4, ending up with:
# [4]234234234278
# Now valid digits need at least 10 after them, so:
# 4 [23]4234234278
# So again, now 9 after:
# 43 [4]234234278
# Now 8 after:
# 434 234234278
# You can see another rule here, which is that if a certain number of indices have been "skipped",
# you reach a point where there is only one valid choice per digit location. Originally, there was
# only 15 digits, and we skipped 3 indices when selecting the most siginificant digits; this means 
# we end up in a situation where only one digit is valid. For optimisation, I could maybe write 
# something that just skips all these cases but we'll see how slow it is without this first :)

open("3/input.txt", "r") do f
  contents = read(f, String)
  contentlines = split(contents, "\n")

  joltages = []
  for line in contentlines
    if line != "" 
      num = parse(BigInt, line)
      dig = reverse(digits(num, base = 10))
      len = length(dig)
      min_valid_index = 1
      max_valid_index = len - 11
      joltage = []
      while length(joltage) < 12
	valid_digits = dig[min_valid_index:max_valid_index]
	max_digit = findmax(valid_digits)
	max_digit_value = max_digit[1]
	max_digit_index = max_digit[2]
	push!(joltage, max_digit_value)
	min_valid_index = min_valid_index + max_digit_index
	max_valid_index = len - (11 - length(joltage))
      end
      # Thanks to: https://stackoverflow.com/a/55525289
      joltage = sum(reverse(joltage).*10 .^(0:(length(joltage)-1)))
      push!(joltages, joltage)
    end
  end

  println(sum(joltages))
end
