
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.3;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@chainlink/contracts/src/v0.8/VRFConsumerBase.sol";


contract IPLCollectible is ERC721URIStorage,VRFConsumerBase,Ownable {
    uint256 public tokenCounter;
    bytes32 public keyhash;
    uint256 public fee;
    address public admin;
    mapping(uint256=>bool) public randomlyAssigned;
    uint256 public lotteryFee = 0.025 ether;
    uint256 public royaltyFee_Perc = 5;
    mapping(bytes32 => address) public requestIdToSender;
    event requestedCollectible(bytes32 indexed requestId, address requester);
    event tokenAssigned(uint256 indexed tokenId);

    // mint set amount of ipl tokens

    constructor(address _vrfCoordinator, address _linkToken, bytes32 _keyhash, uint256 _fee,string[] memory _uris) public 
    VRFConsumerBase(_vrfCoordinator, _linkToken)
    ERC721("IPL", "IPL")
    Ownable()

    {
        admin = msg.sender;
        keyhash = _keyhash;
        fee = _fee;
        tokenCounter = 0;

        for( uint i =0; i<_uris.length;i++){
            uint256 newTokenId = tokenCounter;
            _safeMint(address(this), newTokenId);
            _setTokenURI(newTokenId,_uris[i]);  
            tokenCounter = tokenCounter + 1;
        }
    }

    // play lottery 
    function playLottery() public payable returns (bytes32){
        require(msg.value == lotteryFee,"please provide right amt of lottery fee!");
        bytes32 requestId = requestRandomness(keyhash, fee);
        requestIdToSender[requestId] = msg.sender;
        emit requestedCollectible(requestId, msg.sender);
    }

    function fulfillRandomness(bytes32 requestId, uint256 randomNumber) internal override {
        uint256 tokenIdToAssign  = randomNumber % tokenCounter;
        if(randomlyAssigned[tokenIdToAssign]==false){
            // transfer
            _transfer(address(this),requestIdToSender[requestId],tokenIdToAssign);
            randomlyAssigned[tokenIdToAssign]=true;
            emit tokenAssigned(tokenIdToAssign);
        }
    }

    // admin functions
    function withDrawFees(uint256 _amount) public onlyOwner {
        payable(admin).transfer(_amount);
    }

    function changeLotteryFee (uint256 _fee) public onlyOwner{
        lotteryFee = _fee;
    }

    function changeRoyaltyFeePerc(uint256 _fee) public onlyOwner{
        require(_fee<100,"should be less than 100%");
        royaltyFee_Perc = _fee;
    }

}
