import functools
import json

from utility.hash_util import hash_block
from block import Block
from transaction import Transaction
from utility.verification import Verification
from wallet import Wallet

MINING_REWARD = 10


class Blockchain:
    def __init__(self, hosting_node_id):
        # Initializing our blockchain list
        genesis_block = Block(
            index=0,
            previous_hash='',
            proof=100,
            transactions=[],
            timestamp=0
        )
        self.__chain = [genesis_block]
        self.__open_transactions = []
        self.load_data()
        self.hosting_node = hosting_node_id

    def get_chain(self):
        return self.__chain[:]

    def get_open_transactions(self):
        return self.__open_transactions[:]

    def load_data(self):
        try:
            with open('blockchain.txt', mode='r') as f:
                file_content = f.readlines()
                blockchain = json.loads(file_content[0][:-1])
                self.__chain = [Block(
                    index=block['index'],
                    previous_hash=block['previous_hash'],
                    proof=block['proof'],
                    timestamp=block['timestamp'],
                    transactions=[
                        Transaction(sender=tx['sender'], recipient=tx['recipient'],  signature=tx['signature'], amount=tx['amount']) for tx in
                        block['transactions']]
                ) for block in blockchain]
                open_transactions = json.loads(file_content[1])
                updated_txs = []
                for tx in open_transactions:
                    updated_txs.append(Transaction(sender=tx['sender'], recipient=tx['recipient'], signature=tx['signature'], amount=tx['amount']))
                self.__open_transactions = updated_txs
        except (IOError, IndexError):
            print('Handle Exception...')

    def save_data(self):
        try:
            with open('blockchain.txt', mode='w') as f:
                savable_chain = [block.__dict__ for block in [
                    Block(block_el.index, block_el.previous_hash, [tx.__dict__ for tx in block_el.transactions],
                          block_el.proof, block_el.timestamp) for block_el in self.__chain]]
                f.write(json.dumps(savable_chain))
                f.write('\n')
                f.write(json.dumps([tx.__dict__ for tx in self.__open_transactions]))
        except IOError:
            print('Saving failed!')

    def proof_of_work(self):
        last_block = self.__chain[-1]
        last_hash = hash_block(last_block)
        proof = 0
        while not Verification.valid_proof(self.__open_transactions, last_hash, proof):
            proof += 1
        return proof

    def get_balance(self):
        participant = self.hosting_node

        tx_sender = [[tx.amount for tx in block.transactions if tx.sender == participant] for block in self.__chain]
        open_tx_sender = [tx.amount for tx in self.__open_transactions if tx.sender == participant]
        tx_sender.append(open_tx_sender)
        amount_sent = functools.reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0,
                                       tx_sender, 0)

        tx_recipient = [[tx.amount for tx in block.transactions if tx.recipient == participant] for block in
                        self.__chain]
        amount_received = functools.reduce(
            lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0, tx_recipient, 0)

        return amount_received - amount_sent

    def get_last_blockchain_value(self):
        """ Returns the last value of the current blockchain """
        if len(self.__chain) < 1:
            return None
        return self.__chain[-1]

    def add_transaction(self, recipient, sender, signature, amount=1.0):
        """ Append a new value as well as the last blockchain value to the blockchain

         Arguments:
            :sender: The sender of the coins.
            :sender: The recipient of the coins.
            :amount: The amount of coins sent with the transaction (default = 1.0}
         """

        if self.hosting_node is None:
            return False
        transaction = Transaction(sender=sender, recipient=recipient, signature=signature, amount=amount)

        if Verification.verify_transaction(transaction, self.get_balance):
            self.__open_transactions.append(transaction)
            self.save_data()
            return True
        return False

    def mine_block(self):
        if self.hosting_node is None:
            return False

        # Get last value
        previous_hash = hash_block(self.__chain[-1])
        proof = self.proof_of_work()

        reward_transaction = Transaction(sender='MINING', recipient=self.hosting_node, signature='', amount=MINING_REWARD)
        copied_transactions = self.__open_transactions[:]
        block = Block(
            previous_hash=previous_hash,
            index=len(self.__chain),
            transactions=copied_transactions,
            proof=proof
        )

        for tx in block.transactions:
            if not Wallet.verify_transaction(tx):
                return False

        copied_transactions.append(reward_transaction)
        self.__chain.append(block)

        self.__open_transactions = []
        self.save_data()
        return True
