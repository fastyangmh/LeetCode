# @param {Integer} x
# @return {Boolean}
def is_palindrome(x)
    return x>=0? "#{x}".reverse().to_i == x:FALSE
end