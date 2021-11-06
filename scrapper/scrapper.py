
import os
from GoogleImageScrapper import GoogleImageScraper


data = {
    "Mumbai Indians":"Rohit Sharma, Suryakumar Yadav, Anmolpreet Singh, Chris Lynn, Saurabh Tiwary, Dhawal Kulkarni, Jasprit Bumrah, Rahul Chahar, Trent Boult, Mohsin Khan, Hardik Pandya, Jayant Yadav, Kieron Pollard, Krunal Pandya, Anukul Roy, Ishan Kishan, Quinton de Kock, Aditya Tare, Adam Milne, Nathan Coulter Nile, Piyush Chawla, James Neesham, Yudhvir Charak, Marco Jansen, Arjun Tendulkar",
    "Chennai Super Kings": "MS Dhoni, Suresh Raina, Ambati Rayudu, KM Asif, Deepak Chahar, Dwayne Bravo, Faf du Plessis, Imran Tahir, N Jagadeesan, Karn Sharma, Lungi Ngidi, Mitchell Santner, Ravindra Jadeja, Ruturaj Gaikwad, Shardul Thakur, Sam Curran, Josh Hazlewood, R Sai Kishore, Robin Uthappa, Moeen Ali, Krishnappa Gowtham, Cheteshwar Pujara, M Harisankar Reddy, K Bhagath Varma, C Hari Nishaanth",

    "Royal Challengers Bangalore": "Virat Kohli, AB de Villiers, Devdutt Padikkal, Yuzvendra Chahal, Mohammed Siraj, Kane Richardson, Washington Sundar, Pavan Deshpande, Joshua Philippe, Shahbaz Ahamad, Navdeep Saini, Adam Zampa, Kyle Jamieson, Glenn Maxwell, Rajat Patidar, Sachin Baby, Mohammed Azharuddeen, Dan Christian, KS Bharat, Suyash Prabhudessai, Daniel Sams, Harshal Patel",

    "Delhi Capitals": "Shreyas Iyer, Shikhar Dhawan, Prithvi Shaw, Ajinkya Rahane, Rishabh Pant, Shimron Hetmyer, Marcus Stoinis, Chris Woakes, R Ashwin, Axar Patel, Amit Mishra, Lalit Yadav, Pravin Dubey, Kagiso Rabada, Anrich Nortje, Ishant Sharma, Avesh Khan, Steve Smith, Umesh Yadav, Ripal Patel, Vishnu Vinod, Lukman Meriwala, M Siddarth, Tom Curran, Sam Billings",

    "Punjab Kings": "KL Rahul, Chris Gayle, Mayank Agarwal, Mandeep Singh, Nicholas Pooran, Ishan Porel, Sarfaraz Khan, Murugan Ashwin, Deepak Hooda, Mohammed Shami, Chris Jordan, Ravi Bishnoi, Harpreet Brar, Prabhsimran Singh, Darshan Nalkande, Arshdeep Singh, Dawid Malan, Jhye Richardson, Shahrukh Khan, Riley Meredith, Moises Henriques, Jalaj Saxena, Utkarsh Singh, Fabian Allen, Saurabh Kumar",

    "Kolkata Knight Riders": "Eoin Morgan, Andre Russell, Dinesh Karthik, Kamlesh Nagarkoti, Kuldeep Yadav, Lockie Ferguson, Nitish Rana, Prasidh Krishna, Rinku Singh, Sandeep Warrier, Shivam Mavi, Shubman Gill, Sunil Narine, Pat Cummins, Rahul Tripathi, Varun Chakravarthy, Tim Seifert, Shakib Al Hasan, Sheldon Jackson, Harbhajan Singh, Ben Cutting, Venkatesh Iyer, Pawan Negi, Vaibhav Arora, Karun Nair",

    "Rajasthan Royals": "Sanju Samson , Jos Buttler, Ben Stokes, Yashasvi Jaiswal, Manan Vohra, Anuj Rawat, Riyan Parag, David Miller, Rahul Tewatia, Mahipal Lomror, Shreyas Gopal, Mayank Markande, Jofra Archer, Andrew Tye, Jaydev Unadkat, Kartik Tyagi, Shivam Dube, Chris Morris, Mustafizur Rahman, Chetan Sakariya, KC Cariappa, Liam Livingstone, Kuldip Yadav, Akash Singh",

    "Sun Risers Hyderabad": "David Warner, Jonny Bairstow, Kane Williamson, Manish Pandey, Shreevats Goswami, Wriddhiman Saha, Virat Singh, Priyam Garg, Mohammad Nabi, Vijay Shankar, Kedar Jadhav, Mitchell Marsh, Jason Holder, Abdul Samad, Rashid Khan, Abhishek Sharma, Shahbaz Nadeem, Siddarth Kaul, Mujeeb Ur Rahman, Khaleel Ahmed, T Natarajan, Sandeep Sharma, Basil Thampi, Bhuvneshwar Kumar, Jagadeesha Suchith",

}

data_cleaned = {}
for team, players in data.items():
    data_cleaned[team.strip()] = [p.strip() for p in players.split(',')]


webdriver_path = "./webdriver/chromedriver"
number_of_images = 3
headless = False
#min_resolution = (width,height)
min_resolution=(0,0)
#max_resolution = (width,height)
max_resolution=(1920,1080)


for team, players in data_cleaned.items():
    # make dir if dsnt exists
    directory = './../ipl-imgs/'+team
    if not os.path.exists(directory):
        os.makedirs(directory)
    image_path = directory
    
    for search_key in players:
        search_key = team+" "+search_key+" IPL "
        image_scrapper = GoogleImageScraper(webdriver_path,image_path,search_key,number_of_images,headless,min_resolution,max_resolution)
        image_urls = image_scrapper.find_image_urls()
        image_scrapper.save_images(image_urls)




