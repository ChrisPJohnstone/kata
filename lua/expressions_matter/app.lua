return function(a, b, c)
    plus_plus = a + b + c
    plus_mult = (a + b) * c
    mult_plus = a * (b + c)
    mult_mult = a * b * c
    return math.max(plus_plus, plus_mult, mult_plus, mult_mult)
end
