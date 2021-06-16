# @param {Integer} x
# @return {Integer}
def reverse(x)
    if x<0
        sign=-1
        x=x*sign
    else
        sign=1
    end

    array=[]
    while x!=0
        array=array+[x%10]
        x=x/10
    end

    x=array.join.to_i()
    x=x*sign

    if x<(-2**31) or x>((2**31)-1)
        x=0
    end
    return x
end