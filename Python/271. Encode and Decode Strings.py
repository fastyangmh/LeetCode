class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        tmp = []

        for s in strs:
            tmp.append(f"{len(s)}#{s}")

        return "".join(tmp)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        ans = []

        n = len(s)
        i = 0

        while i < n:
            j = i

            while s[j] != "#" and j < n:
                j += 1

            l = int(s[i:j])
            i = j + 1

            ans.append(s[i : i + l])

            i += l

        return ans


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
