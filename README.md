# the-first-fifty-blocks-of-the-bitcoin-blockchain.py

the-first-fifty-blocks-of-the-bitcoin-blockchain.py is a python script that creates an [HTML document](https://www.meixler-tech.com/the-first-fifty-blocks-of-the-bitcoin-blockchain.html) which visually shows how the block hashes of the first fifty blocks in the bitcoin blockchain are calculated, and how the blocks are chained together.  

For each block, there are six color-coded inputs to the double sha256 hash function which is used to calculate the block hash.  Note that for each block, one of these inputs (shown in black) is block hash of the previous block.  Hence, the blocks are chained together - by virtue of the fact for each block, one of the inputs used to calculate the block hash is the block hash of the previous block.  

the-first-fifty-blocks-of-the-bitcoin-blockchain.py obtains block data from the [Blockchain.com API](https://www.blockchain.com/explorer/api/blockchain_api).  

Reference: [https://en.bitcoin.it/wiki/Block_hashing_algorithm](https://en.bitcoin.it/wiki/Block_hashing_algorithm)

