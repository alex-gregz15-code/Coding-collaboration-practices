import hashlib
import datetime

class Block:
    def __init__(self, index, transaction, previous_hash):
        self.index = index
        self.timestamp = str(datetime.datetime.now())
        self.transaction = transaction
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data = (
            str(self.index)
            + self.timestamp
            + self.transaction
            + self.previous_hash
        )
        return hashlib.sha256(data.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "Accounting Ledger Started", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, transaction):
        latest_block = self.get_latest_block()
        new_block = Block(
            len(self.chain),
            transaction,
            latest_block.hash
        )
        self.chain.append(new_block)

    def display_chain(self):
        for block in self.chain:
            print("Block No:", block.index)
            print("Date:", block.timestamp)
            print("Transaction:", block.transaction)
            print("Hash:", block.hash)
            print("Previous Hash:", block.previous_hash)
            print("-" * 50)


# Create blockchain ledger
ledger = Blockchain()

# Accounting transactions
ledger.add_block("Cash Deposit: +5000")
ledger.add_block("Office Supplies Expense: -1200")
ledger.add_block("Service Revenue: +3000")
ledger.add_block("Utility Expense: -800")

# Display ledger
ledger.display_chain()
