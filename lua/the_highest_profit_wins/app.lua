local function min_max(lst)
  min = math.min(table.unpack(lst))
  max = math.max(table.unpack(lst))
  return {min, max}
end

result = min_max({1, 2, 4, 3})
print(result)
return min_max
