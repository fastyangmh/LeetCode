class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')


if __name__ == "__main__":
    address = '1.1.1.1'
    print(Solution().defangIPaddr(address))
