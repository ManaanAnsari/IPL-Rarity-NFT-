from brownie import  IPLCollectible, web3
from scripts.helpful_scripts import (
    get_account,
    get_uris,
)
from scripts.deploy import deploy


def test_can_deploy():
    # deploy the contract
    # create an NFT
    # get a random token back
    # Arrange
    # Act
    IPLContract = deploy()
    # Assert
    assert IPLContract.tokenCounter() == len(get_uris())


def test_can_changeLotteryFee():
    if len(IPLCollectible):
        IPLContract = IPLCollectible[-1]
    else:
        IPLContract = deploy()
    
    tx = IPLContract.changeLotteryFee(web3.toWei("0.1","ether"),{"from":get_account()})
    tx.wait(1)
    assert IPLContract.lotteryFee() == web3.toWei("0.1","ether")


def test_can_changeRoyaltyFeePerc():
    if len(IPLCollectible):
        IPLContract = IPLCollectible[-1]
    else:
        IPLContract = deploy()
    
    tx = IPLContract.changeRoyaltyFeePerc(1,{"from":get_account()})
    tx.wait(1)
    assert IPLContract.royaltyFee_Perc() == 1


