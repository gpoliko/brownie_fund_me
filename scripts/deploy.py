from unittest import mock
from brownie import FundMe, MockV3Aggregator, config, network
from scripts.utils import get_account, deploy_mocks
from web3 import Web3


def deploy_fund_me():
    account = get_account()

    if network.show_active() != "development":
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Contract Deployed to {fund_me.address}")


def main():
    deploy_fund_me()
