kata = {}

function kata.strEndsWith(s, ending)
  if string.len(ending) == 0 then
    return true
  end
  ending_length = string.len(ending)
  end_of_s = string.sub(s, -ending_length)
  if ending == end_of_s then
    return true
  else
    return false
  end
end

result = kata.strEndsWith("abc", "")
print(result)
return kata
