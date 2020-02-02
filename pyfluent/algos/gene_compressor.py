from sys import getsizeof


class CompressGene:
    """
    Rational for creating this compression class. Every character requires 8 bits, but each nucleotide of a gene
    can be represented with just 2 bits.
    So, there is scope to reduce the overall bytes in storing the gene string.
    """
    def __init__(self, gene):
        self._compress(gene)

    def _compress(self, gene: str):
        self.bit_string: int = 1        # sentinel value
        for nucleotide in gene:
            self.bit_string <<= 2
            if nucleotide == 'A':
                self.bit_string |= 0b00
            elif nucleotide == 'C':
                self.bit_string |= 0b01
            elif nucleotide == 'T':
                self.bit_string |= 0b10
            else:
                self.bit_string |= 0b11

        print(bin(self.bit_string))
        return self.bit_string

    def decompress(self) -> str:
        gene = ""
        for i in range(0, self.bit_string.bit_length() - 1, 2):
            val: int = self.bit_string >> i & 0b11
            if val == 0b00:
                gene += "A"
            elif val == 0b01:
                gene += "C"
            elif val == 0b10:
                gene += "T"
            else:
                gene += "G"
        return gene[::-1]


if __name__=="__main__":
    gene = "TCCGTA" * 100
    compressor = CompressGene(gene)
    print(compressor.decompress())

    print(f"Original gene string is {getsizeof(gene)} bytes")
    print(f"Compressed gene string is {getsizeof(compressor.bit_string)} bytes")
