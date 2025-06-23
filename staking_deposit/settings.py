from typing import Dict, NamedTuple
from eth_utils import decode_hex

DEPOSIT_CLI_VERSION = '3.1'


class BaseChainSetting(NamedTuple):
    NETWORK_NAME: str
    GENESIS_FORK_VERSION: bytes
    GENESIS_VALIDATORS_ROOT: bytes


ITXLOCALNET = 'itxlocalnet' # 532100
ITXDEVNET = 'itxdevnet' # 53210
ITXTESTNET = 'itxtestnet' # 5321
ITXMAINNET = 'itxmainnet' # 1235

# 4954584C -> ITXL | Chain ID 532100
# 49545844 -> ITXD | Chain ID 53210
# 49545854 -> ITXT | Chain ID 5321
# 49545800 -> ITXM | Chain ID 1235

ItxLocalSetting = BaseChainSetting(
    NETWORK_NAME=ITXLOCALNET, GENESIS_FORK_VERSION=bytes.fromhex('4954584C'),
    GENESIS_VALIDATORS_ROOT=bytes.fromhex('0000000000000000000000000000000000000000000000000000000000000000'))

ItxDevnetSetting = BaseChainSetting(
    NETWORK_NAME=ITXDEVNET, GENESIS_FORK_VERSION=bytes.fromhex('49545844'),
    GENESIS_VALIDATORS_ROOT=bytes.fromhex('0000000000000000000000000000000000000000000000000000000000000000'))

ItxTestnetSetting = BaseChainSetting(
    NETWORK_NAME=ITXTESTNET, GENESIS_FORK_VERSION=bytes.fromhex('49545854'),
    GENESIS_VALIDATORS_ROOT=bytes.fromhex('0000000000000000000000000000000000000000000000000000000000000000'))

ItxMainnetSetting = BaseChainSetting(
    NETWORK_NAME=ITXMAINNET, GENESIS_FORK_VERSION=bytes.fromhex('49545800'),
    GENESIS_VALIDATORS_ROOT=bytes.fromhex('0000000000000000000000000000000000000000000000000000000000000000'))

ALL_CHAINS: Dict[str, BaseChainSetting] = {
    ITXLOCALNET: ItxLocalSetting,
    ITXDEVNET: ItxDevnetSetting,
    ITXTESTNET: ItxTestnetSetting,
    ITXMAINNET: ItxMainnetSetting,
}

def get_chain_setting(chain_name: str = ITXLOCALNET) -> BaseChainSetting:
    return ALL_CHAINS[chain_name]


def get_devnet_chain_setting(network_name: str,
                             genesis_fork_version: str,
                             genesis_validator_root: str) -> BaseChainSetting:
    return BaseChainSetting(
        NETWORK_NAME=network_name,
        GENESIS_FORK_VERSION=decode_hex(genesis_fork_version),
        GENESIS_VALIDATORS_ROOT=decode_hex(genesis_validator_root),
    )
