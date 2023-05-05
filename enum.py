# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""

class Chains:
    ETHEREUM = 'ETHEREUM'
    AVAX = 'AVAX'
    BSC = 'BSC'
    POLYGON = 'POLYGON'
    BOBA = 'BOBA'
    
CHAINS_NAME = [
    {
        "name": "Ethereum",
        "symbol":  "ETHEREUM",
        "image_url": "https://static.katanainu.com/chain/ethereum.svg"
    },
    {
        "name": "Avalanche",
        "symbol":  "AVAX",
        "image_url": "https://static.katanainu.com/chain/avax.svg"
    },
    {
        "name": "Boba Network",
        "symbol":  "BOBA",
        "image_url": "https://static.katanainu.com/chain/boba.svg"
    },
    {
        "name": "Binance Smart Chain",
        "symbol":  "BSC",
        "image_url": "https://static.katanainu.com/chain/bsc.svg"
    },
]

ListChainsSupport = [Chains.ETHEREUM, Chains.AVAX, Chains.BOBA, Chains.BSC]

NFT_AMOUNT_PUBLIC_MINT = 50