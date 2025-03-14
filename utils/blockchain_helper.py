
from web3 import Web3
import os
import json

# Initialize Web3 with Polygon Mumbai testnet
POLYGON_RPC = "https://rpc-mumbai.maticvigil.com/"
web3 = Web3(Web3.HTTPProvider(POLYGON_RPC))

# Simplified NFT Contract ABI
TICKET_NFT_ABI = [
    {
        "inputs": [
            {"internalType": "address", "name": "to", "type": "address"},
            {"internalType": "string", "name": "tokenURI", "type": "string"}
        ],
        "name": "mintTicket",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "nonpayable",
        "type": "function"
    }
]

def mint_space_ticket(user_address, trip_data):
    try:
        contract = web3.eth.contract(
            address=os.environ.get('NFT_CONTRACT_ADDRESS'),
            abi=TICKET_NFT_ABI
        )
        
        # Create metadata for the NFT
        metadata = {
            "name": f"Space Ticket - {trip_data['destination']}",
            "description": f"Valid for travel to {trip_data['destination']} on {trip_data['departure_date']}",
            "image": "https://ipfs.io/ipfs/your_ticket_image_hash",
            "attributes": [
                {"trait_type": "Destination", "value": trip_data['destination']},
                {"trait_type": "Class", "value": trip_data.get('class', 'Economy')},
                {"trait_type": "Departure", "value": trip_data['departure_date']}
            ]
        }
        
        # In production, you'd upload this to IPFS
        token_uri = f"https://your-api.com/metadata/{trip_data['id']}"
        
        # Mint NFT (simplified - in production, handle transaction signing)
        tx_hash = contract.functions.mintTicket(
            user_address,
            token_uri
        ).transact({'from': os.environ.get('ADMIN_ADDRESS')})
        
        return web3.eth.wait_for_transaction_receipt(tx_hash)
    except Exception as e:
        print(f"Error minting ticket: {str(e)}")
        return None
