
## what it does?
- minting **196 NFT tokens** (no. of players) with contract itself as token owner
- the only way to get these NFTs is by playing lottery, random numbers are generated using **chainlink VRF** and **pinata** is used for metadata storage
- smartcontract takes **5% royalty** every time NFT token is traded
- all NFTs will be listed on **opensea** market place

## Players
```
"Mumbai Indians": "Rohit Sharma, Suryakumar Yadav, Anmolpreet Singh, Chris Lynn, Saurabh Tiwary, Dhawal Kulkarni, Jasprit Bumrah, Rahul Chahar, Trent Boult, Mohsin Khan, Hardik Pandya, Jayant Yadav, Kieron Pollard, Krunal Pandya, Anukul Roy, Ishan Kishan, Quinton de Kock, Aditya Tare, Adam Milne, Nathan Coulter Nile, Piyush Chawla, James Neesham, Yudhvir Charak, Marco Jansen, Arjun Tendulkar",

"Chennai Super Kings": "MS Dhoni, Suresh Raina, Ambati Rayudu, KM Asif, Deepak Chahar, Dwayne Bravo, Faf du Plessis, Imran Tahir, N Jagadeesan, Karn Sharma, Lungi Ngidi, Mitchell Santner, Ravindra Jadeja, Ruturaj Gaikwad, Shardul Thakur, Sam Curran, Josh Hazlewood, R Sai Kishore, Robin Uthappa, Moeen Ali, Krishnappa Gowtham, Cheteshwar Pujara, M Harisankar Reddy, K Bhagath Varma, C Hari Nishaanth",

"Royal Challengers Bangalore": "Virat Kohli, AB de Villiers, Devdutt Padikkal, Yuzvendra Chahal, Mohammed Siraj, Kane Richardson, Washington Sundar, Pavan Deshpande, Joshua Philippe, Shahbaz Ahamad, Navdeep Saini, Adam Zampa, Kyle Jamieson, Glenn Maxwell, Rajat Patidar, Sachin Baby, Mohammed Azharuddeen, Dan Christian, KS Bharat, Suyash Prabhudessai, Daniel Sams, Harshal Patel",

"Delhi Capitals": "Shreyas Iyer, Shikhar Dhawan, Prithvi Shaw, Ajinkya Rahane, Rishabh Pant, Shimron Hetmyer, Marcus Stoinis, Chris Woakes, R Ashwin, Axar Patel, Amit Mishra, Lalit Yadav, Pravin Dubey, Kagiso Rabada, Anrich Nortje, Ishant Sharma, Avesh Khan, Steve Smith, Umesh Yadav, Ripal Patel, Vishnu Vinod, Lukman Meriwala, M Siddarth, Tom Curran, Sam Billings",

"Punjab Kings": "KL Rahul, Chris Gayle, Mayank Agarwal, Mandeep Singh, Nicholas Pooran, Ishan Porel, Sarfaraz Khan, Murugan Ashwin, Deepak Hooda, Mohammed Shami, Chris Jordan, Ravi Bishnoi, Harpreet Brar, Prabhsimran Singh, Darshan Nalkande, Arshdeep Singh, Dawid Malan, Jhye Richardson, Shahrukh Khan, Riley Meredith, Moises Henriques, Jalaj Saxena, Utkarsh Singh, Fabian Allen, Saurabh Kumar",

"Kolkata Knight Riders": "Eoin Morgan, Andre Russell, Dinesh Karthik, Kamlesh Nagarkoti, Kuldeep Yadav, Lockie Ferguson, Nitish Rana, Prasidh Krishna, Rinku Singh, Sandeep Warrier, Shivam Mavi, Shubman Gill, Sunil Narine, Pat Cummins, Rahul Tripathi, Varun Chakravarthy, Tim Seifert, Shakib Al Hasan, Sheldon Jackson, Harbhajan Singh, Ben Cutting, Venkatesh Iyer, Pawan Negi, Vaibhav Arora, Karun Nair",

"Rajasthan Royals": "Sanju Samson , Jos Buttler, Ben Stokes, Yashasvi Jaiswal, Manan Vohra, Anuj Rawat, Riyan Parag, David Miller, Rahul Tewatia, Mahipal Lomror, Shreyas Gopal, Mayank Markande, Jofra Archer, Andrew Tye, Jaydev Unadkat, Kartik Tyagi, Shivam Dube, Chris Morris, Mustafizur Rahman, Chetan Sakariya, KC Cariappa, Liam Livingstone, Kuldip Yadav, Akash Singh",

"Sun Risers Hyderabad": "David Warner, Jonny Bairstow, Kane Williamson, Manish Pandey, Shreevats Goswami, Wriddhiman Saha, Virat Singh, Priyam Garg, Mohammad Nabi, Vijay Shankar, Kedar Jadhav, Mitchell Marsh, Jason Holder, Abdul Samad, Rashid Khan, Abhishek Sharma, Shahbaz Nadeem, Siddarth Kaul, Mujeeb Ur Rahman, Khaleel Ahmed, T Natarajan, Sandeep Sharma, Basil Thampi, Bhuvneshwar Kumar, Jagadeesha Suchith",

```

## how to use?
-   clone this repo
    create `.env` file and fill the following details
    >export PRIVATE_KEY=xxxx
    export WEB3_INFURA_PROJECT_ID=xx
    export ETHERSCAN_TOKEN=xx
    export PINATA_API_SECRET=xx
    export PINATA_API_KEY=xx
    export UPLOAD_IPFS=True

-   ##### if you are planning to use built in image scrapper
    -   `pip install -r scrapper-req`
    -   `cd scrapper` 
    -   run `python scrapper.py`
    -   run `python togif.py`


-   install dependencies `pip install -r requirements.txt`
-   upload all the gifs in `ipl-gifs`  to pinata by running `brownie run scripts/upload_to_pinata.py`
-   now upload all the metadata `brownie run scripts/create_metadata.py`
-   finally deploy `brownie run scripts/deploy.py`

to test on opensea use  `--network rinkeby` network to deploy and also make sure you have link token



## Credits
scrapper is implemented using [this](https://github.com/ohyicong/Google-Image-Scraper) public repo


## Todos
- [ ] write more testcases
- [ ] implement royalty mechanism
- [ ] integrate with rangmanch/marketplace 
