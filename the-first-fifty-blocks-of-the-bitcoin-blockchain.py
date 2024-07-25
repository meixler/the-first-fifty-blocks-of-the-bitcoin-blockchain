import requests
import json
import hashlib

block={'nextblock': '000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f'}

print('<html>')
print('<head><style>body { font-family: courier;}</style></head>')
print('<body>')

print('<h2>The first fifty blocks of the bitcoin blockchain</h2>')
print('<b>Legend</b><br>')
print('<table width=30%><tr><td>')
print('<font color=blue>blue: version</font><br>')
print('<font color=black>black: previous block hash</font><br>')
print('<font color=red>red: current block merkle root</font><br>')
print('</td><td>')
print('<font color=green>green: time</font><br>')
print('<font color=orange>orange: difficulty bits</font><br>')
print('<font color=purple>purple: nonce</font><br>')
print('</td></tr></table>')

print('<p> </p>')
for blocknumber in range(0, 50):
	blockhash=block['nextblock']				
	url='https://blockchain.info/rawblock/' + blockhash
	resp = requests.get(url)
	data = json.loads(resp.text)

	block={}
	block['blocknumber']=blocknumber
	block['version']=data['ver']
	block['hashPrevBlock']=data['prev_block']
	block['hashMerkleRoot']=data['mrkl_root']
	block['time']=data['time']
	block['bits']=data['bits']
	block['nonce']=data['nonce']
	block['hash']=data['hash']
	block['nextblock']=data['next_block'][0]

	block['versionprepared']=int(block['version']).to_bytes(4, byteorder='little').hex()
	block['hashPrevBlockprepared']=bytes.fromhex(block['hashPrevBlock'])[::-1].hex()
	block['hashMerkleRootprepared']=bytes.fromhex(block['hashMerkleRoot'])[::-1].hex()
	block['timeprepared']=int(block['time']).to_bytes(4, byteorder='little').hex()
	block['bitsprepared']=int(block['bits']).to_bytes(4, byteorder='little').hex()
	block['nonceprepared']=int(block['nonce']).to_bytes(4, byteorder='little').hex()
	block['hashprepared']=bytes.fromhex(block['hash'])[::-1].hex()

	block['hashin']=block['versionprepared'] + block['hashPrevBlockprepared'] + block['hashMerkleRootprepared'] + block['timeprepared'] + block['bitsprepared'] + block['nonceprepared']
	block['hashoutcomputed']=(hashlib.sha256(hashlib.sha256(bytes.fromhex(block['hashin'])).digest()).digest()).hex()
	block['header']='<font color=blue>' + block['versionprepared'] + '</font>' + '<font color=black>' + block['hashPrevBlockprepared'] + '</font>' + '<font color=red>' + block['hashMerkleRootprepared'] + '</font>' + '<font color=green>' + block['timeprepared'] + '</font>' + '<font color=orange>' + block['bitsprepared'] + '</font>' + '<font color=purple>' + block['nonceprepared'] + '</font>' 
	
	print('block:', blocknumber, '<br>')
	print('block header:', block['header'], '<br>')
	print('&#8627; SHA256 &#8594; SHA256 &#8628;', '<br>')
	print('block hash:', block['hashoutcomputed'], '<br>')
	print('<p> </p>')
	

print('<br><br>')
print('<font color=black><i>This document produced by <a href=https://github.com/meixler/the-first-fifty-blocks-of-the-bitcoin-blockchain>the-first-fifty-blocks-of-the-bitcoin-blockchain.py</a>.</i></font><br>')
print('<br><br>')

print('</body>')
print('</html>')

	
