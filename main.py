from selenium import webdriver
from PIL import Image
import time
import numpy as np
import sys

websites = {'Social Media':
                            ['facebook.com', 'instagram.com', 'twitter.com', 'whatsapp.com', 'tiktok.com'],
            'General Search':
                            ['google.com', 'youtube.com', 'yahoo.com', 'zoom.us', 'netflix.com'],
            'Shopping':
                            ['amazon.com', 'myshopify.com', 'aliexpress.com', 'ebay.com', 'flipkart.com']}



websites_visited = {'Social Media':
                                    [0,0,0,0,0],
                   'General Search':
                                    [0,0,0,0,0],
                   'Shopping':
                                    [0,0,0,0,0]}

category = list(websites.keys())


def open_pages(str1):
    driver = webdriver.Chrome(executable_path = '/Users/john/Downloads/chromedriver 2')
    url = "https://www." + str1
    driver.get(url)
    driver.save_screenshot('/Users/john/Downloads/pythonProject1/ss/ss.png')
    screenshot = Image.open('/Users/john/Downloads/pythonProject1/ss/ss.png')


    a = [[10,20,30,40],
        [40,60,10000,900]]

    for i in range(np.shape(a)[0]):
        s = screenshot.crop((a[i][0], a[i][1], a[i][2], a[i][3]))
        s = s.convert('RGB')
        s = s.save('/Users/john/Downloads/pythonProject1/ss/' + str(i) + '.jpg')

    time.sleep(1)
    driver.close()


def set_websites_visited(b,c):
    global websites_visited
    websites_visited[category[int(c)]][int(b)-1] = 1
    print("b", websites_visited[category[int(c)]])

def get_websites_visited(c):
    return websites_visited[category[int(c)-1]]

def menu():
    global websites_visited

    all_bool = all(value == 0 for value in websites_visited.values())

    if(all_bool):
        print("Thanks for user study.")
        sys.exit()
    print("Select a Category by index")
    print('------------------------------------')

    for k  in category:
        print(k)
    print('------------------------------------')
    c = input()
    web_cat = websites_visited[category[int(c)-1]]

    boolean = (all(v == 1 for v in web_cat))

    if (boolean):
        print("You have visited all the websites from this category. Please select another category")
        menu()
    else:
        print("Select a website from " + category[int(c)-1] + " category by index")
        print('------------------------------------')
        webs = websites[category[int(c)-1]]
        for w in range(len(webs)):
            if(web_cat[w] == 1):
                print('\u0336'.join(webs[w]) + '\u0336')
            else:
                print(webs[w])
        print('------------------------------------')
        b = input()
        websites_visited[category[int(c)-1]][int(b)-1] = 1
        open_pages(websites[category[int(c)-1]][int(b)-1])
        menu()

menu()
