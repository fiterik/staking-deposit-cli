from typing import Dict, NamedTuple
from eth_utils import decode_hex

DEPOSIT_CLI_VERSION = '3.0.0'


class BaseChainSetting(NamedTuple):
    NETWORK_NAME: str
    GENESIS_FORK_VERSION: bytes
    GENESIS_VALIDATORS_ROOT: bytes

ITXTESTNET = 'itxtestnet'

ItxTestnetSetting = BaseChainSetting(
    NETWORK_NAME=ITXTESTNET, GENESIS_FORK_VERSION=bytes.fromhex('49545800'),
    GENESIS_VALIDATORS_ROOT=bytes.fromhex('f27fbc33ae61765359121f8d798c746be341e67609aaf0699d24554acbee9509'))

ALL_CHAINS: Dict[str, BaseChainSetting] = {
    ITXTESTNET: ItxTestnetSetting,
}


def get_chain_setting(chain_name: str = ITXTESTNET) -> BaseChainSetting:
    return ALL_CHAINS[chain_name]


def get_devnet_chain_setting(network_name: str,
                             genesis_fork_version: str,
                             genesis_validator_root: str) -> BaseChainSetting:
    return BaseChainSetting(
        NETWORK_NAME=network_name,
        GENESIS_FORK_VERSION=decode_hex(genesis_fork_version),
        GENESIS_VALIDATORS_ROOT=decode_hex(genesis_validator_root),
    )
