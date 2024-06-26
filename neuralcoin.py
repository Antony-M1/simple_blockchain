# Here the Tutorial Link
# https://www.youtube.com/watch?v=pYasYyjByKI

import hashlib


class NeuralCoinblock:

    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = "-".join(transaction_list) + "-" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()


# Transaction History
t1 = "Anna sends 2 NC to Mike"
t2 = "Bob sends 4.3 NC to Mike"
t3 = "Mike sends 3.2 NC to Bob"
t4 = "Daniel sends 0.3 NC to Anna"
t5 = "Mike sends 1 NC to Charlie"
t6 = "Mike sends 5.4 NC to Daniel"

initial_block = NeuralCoinblock("Initial String", [t1, t2])

print(initial_block.block_data)
print(initial_block.block_hash)

second_block = NeuralCoinblock(initial_block.block_hash, [t3, t4])

print(second_block.block_data)
print(second_block.block_hash)

third_block = NeuralCoinblock(second_block.block_hash, [t5, t6])

print(third_block.block_data)
print(third_block.block_hash)

