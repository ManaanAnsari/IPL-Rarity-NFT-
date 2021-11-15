pragma solidity ^0.8.6;

import '@openzeppelin/contracts/token/ERC20/ERC20.sol';

contract WETH is ERC20 {
  constructor() ERC20('Wrapped ETH', 'WETH') {
    _mint(msg.sender, 1000 * 10 ** 18); 
  }
}