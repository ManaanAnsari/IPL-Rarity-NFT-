from brownie import network, IPLCollectible, web3
import pytest
from scripts.helpful_scripts import (
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    get_contract,
    get_account,
    get_uris,
)
from scripts.deploy import deploy


def test_can_create_IPLCollectibles():
    # deploy the contract
    # create an NFT
    # get a random token back
    # Arrange
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for local testing")
    # Act
    IPLContract = deploy()
    lottery_fee = IPLContract.lotteryFee()
    print("lottery_fee",lottery_fee)
    lottery_tx = IPLContract.playLottery({"from": get_account(),"value":lottery_fee})
    lottery_tx.wait(1)
    
    requestId = lottery_tx.events["requestedCollectible"]["requestId"]
    random_number = 777
    get_contract("vrf_coordinator").callBackWithRandomness(
        requestId, random_number, IPLContract.address, {"from": get_account()}
    )
    # Assert
    assert IPLContract.tokenCounter() == len(get_uris())
    assert IPLContract.randomlyAssigned(random_number % len(get_uris())) == True

