# @param {String} s
# @return {Integer}
def roman_to_int(s)
    hash={'I'=>1,'V'=>5,'X'=>10,'L'=>50,'C'=>100,'D'=>500,'M'=>1000}
    s=s.reverse()
    ans=hash[s[0]]
    last=ans
    for idx in 1...s.length()do
        a=hash[s[idx]]
        if last>a
            ans-=a
        else
            ans+=a
        end
        last=a
    end
    return ans
end