local kata = {}

kata.romanEncoder = function(number)
  romanchars = {
    [1] = "I",
    [5] = "V",
    [10] = "X",
    [50] = "L",
    [100] = "C",
    [500] = "D",
    [1000] = "M",
  }
  numstring = tostring(number)
  output_constructor = {}
  for position = string.len(numstring), 1, -1 do
    character = tonumber(string.sub(numstring, string.len(numstring) - position + 1, string.len(numstring) - position + 1))
    single = 1 * 10 ^ (position - 1)
    roman_single = romanchars[single]
    roman_five = romanchars[single * 5]
    if character >= 1 and character <= 3 then
      table.insert(output_constructor, string.rep(roman_single, character))
    elseif character == 4 then
      table.insert(output_constructor, roman_single .. roman_five)
    elseif character == 5 then
      table.insert(output_constructor, roman_five)
    elseif character >= 6 and character <= 8 then
      table.insert(output_constructor, roman_five .. string.rep(roman_single, character - 5))
    elseif character == 9 then
      roman_ten = romanchars[single * 10]
      table.insert(output_constructor, roman_single .. roman_ten)
    end
  end
  output = ""
  for key, value in ipairs(output_constructor) do
      output = output .. value
  end
  print(output)
  return output
end

kata.romanEncoder(1234)
return kata
