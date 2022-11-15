class AlgoHashTable:

    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()

    def create_buckets(self):
        return [[] for _ in range(self.size)]

    def set_val(self, key, value):
        hashed_key = 10 # hash(key)%self.size
        bucket = self.hash_table[hashed_key]
        bucket.append((key, value))

    def get_val(self, key):
        pass

    def __str__(self):
        return "".join(str(item) for item in self.hash_table)

hash_table = AlgoHashTable(256)
print(hash_table)
hash_table.set_val('mashrur@example.com','some value')
hash_table.set_val('evgeny@example.com','some other value')
print(hash_table)
