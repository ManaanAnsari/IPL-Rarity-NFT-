from scripts.helpful_scripts import (
    get_account,
    get_uris,
    OPENSEA_URL,
    get_contract,
    fund_with_link,
)
from brownie import IPLCollectible, network, config, web3


def deploy():
    account = get_account()
    uris = get_uris()
    if not uris:
        print('uris empty')
        return
    # We want to be able to use the deployed contracts if we are on a testnet
    # Otherwise, we want to deploy some mocks and use those
    # Rinkeby
    iplContract = IPLCollectible.deploy(
        get_contract("vrf_coordinator"),
        get_contract("link_token"),
        config["networks"][network.show_active()]["keyhash"],
        config["networks"][network.show_active()]["fee"],
        uris,
        {"from": account},
    )
    fund_with_link(iplContract.address)
    print("Deployed!")
    return iplContract


def main():
    deploy()
