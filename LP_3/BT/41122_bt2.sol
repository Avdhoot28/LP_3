// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

contract Bank {
    mapping(address => uint256) public balances;

    function hello() public view returns (address) {
        return msg.sender;
    }

    function deposit(uint256 amount1) public payable {
        balances[msg.sender] += amount1;
    }

    function withdraw(uint256 _amount) public {
        require(balances[msg.sender] >= _amount, "Not enough ether");
        balances[msg.sender] -= _amount;
        (bool sent, ) = msg.sender.call{value: _amount}("Sent");
        require(sent, "failed to send ETH");
    }

    function getBal() public view returns (uint256) {
        return balances[msg.sender];
    }
}
