class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        ret = []

        for s in strs:
            ret.append(f"{len(s)}#{s}")

        return "".join(ret)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        ret = []
        i = 0
        n = len(s)

        while i < n:
            j = i

            while j < n and s[j] != "#":
                j += 1

            length = int(s[i:j])

            ret.append(s[j + 1 : j + 1 + length])

            i = j + 1 + length

        return ret


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
