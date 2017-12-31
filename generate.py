# coding=utf-8

from iota import Iota, ProposedTransaction, Address, TryteString, Tag, Transaction

URL_NODE="http://node.deviceproof.org:14265"
SEED="RBYYYKDIUDXV9Z9FQPFJSA9QQIGFZAS9XXAWHSDPPXYR9ULXZWYNQSOOYHOXSNXEORWGRIQXXINRHKTCU"
RECEIVE_ADDRESS="ILXW9VMJQVFQVKVE9GUZSODEMIMGOJIJNFAX9PPJHYQPUHZLTWCJZKZKCZYKKJJRAKFCCNJN9EWOW9N9YDGZDDQDDC"
DEPTH=7
MIN_WEIGHT_MAGNITUDE=14

COUNT_GENERATE=3

def transfer(address, tag, message, value):
    recipient_address = address
    sender_message = message
    sender_tag = tag

    prepared_transferes = []
    api = Iota(URL_NODE, SEED)

    sender_tag = bytes(sender_tag)
    transfer_value = int(value)

    txn = \
        ProposedTransaction(
            address = Address(
                recipient_address
        ),

        message = TryteString.from_string(sender_message),
        tag = Tag(sender_tag),
        value = transfer_value,
    )

    prepared_transferes.append(txn)
    
    dict_raw_trytes_tx = api.prepare_transfer(prepared_transferes)
    len_tx = len(dict_raw_trytes_tx['trytes'])
    for index in range(len_tx):
        print str(dict_raw_trytes_tx['trytes'][index])

    return True

for index in range(COUNT_GENERATE):
    transfer(RECEIVE_ADDRESS, "TEST", "TEST", 0)
