from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from flask_mail import sendmail
import pandas as pd
import json

ZomatoData = pd.read_csv('zomato.csv', encoding='cp1252')
ZomatoData = ZomatoData.drop_duplicates().reset_index(drop=True)
WeOperate = ['Ahmedabad', 'Bengaluru', 'Chennai', 'Delhi', 'Hyderabad', 'Kolkata', 'Mumbai', 'Pune', 'Agra', 'Ajmer', 'Aligarh', 'Amravati', 'Amritsar', 'Asansol', 'Aurangabad', 'Bareilly', 'Belgaum', 'Bhavnagar', 'Bhiwandi', 'Bhopal', 'Bhubaneswar', 'Bikaner', 'Bilaspur', 'Bokaro Steel City', 'Chandigarh', 'Coimbatore', 'Cuttack', 'Dehradun', 'Dhanbad', 'Bhilai', 'Durgapur', 'Erode', 'Faridabad', 'Firozabad', 'Ghaziabad', 'Gorakhpur', 'Gulbarga', 'Guntur', 'Gwalior', 'Gurugram', 'Guwahati', 'Hamirpur', 'Hubli', 'Dharwad', 'Indore', 'Jabalpur', 'Jaipur', 'Jalandhar', 'Jalgaon', 'Jammu', 'Jamnagar', 'Jamshedpur', 'Jhansi', 'Jodhpur', 'Kakinada', 'Kannur', 'Kanpur', 'Karnal', 'Kochi', 'Kolhapur', 'Kollam', 'Kozhikode', 'Kurnool', 'Ludhiana', 'Lucknow', 'Madurai', 'Malappuram', 'Mathura', 'Mangalore', 'Meerut', 'Moradabad', 'Mysore', 'Nagpur', 'Nanded', 'Nashik', 'Nellore', 'Noida', 'Patna', 'Puducherry', 'Purulia', 'Prayagraj', 'Raipur', 'Rajkot', 'Rajamahendravaram', 'Ranchi', 'Rourkela', 'Ratlam', 'Salem', 'Sangli', 'Shimla', 'Siliguri', 'Solapur', 'Srinagar', 'Surat', 'Thanjavur', 'Thiruvananthapuram', 'Thrissur', 'Tiruchirappalli', 'Tirunelveli', 'Tiruvannamalai', 'Ujjain', 'Vijayapura', 'Vadodara', 'Varanasi', 'Vasai', 'Virar', 'Vijayawada', 'Visakhapatnam', 'Vellore', 'Warangal']

ZomatoData['Budget']= ZomatoData['Average Cost for two'].apply(lambda x:'<300' if (x<300) else '300-700' if (x>299 and x<701) else '>700')

ZomatoData.sort_values(by='Aggregate rating', ascending=False)

def location_check(City):
    res = ''
    if (City in WeOperate):
        pass
    else:
        dispatcher.utter_message('Sorry, we don’t operate in this city. Can you please specify some other location')

def RestaurantSearch(City,Cuisine,Budget):
    TEMP = ZomatoData[(ZomatoData['Cuisines'].apply(lambda x: Cuisine.lower() in x.lower())) & (ZomatoData['City'].apply(lambda x: City.lower() in x.lower())) & (ZomatoData['Budget'].apply(lambda x: Budget in x))]
    return TEMP[['Restaurant Name','Address','Average Cost for two','Aggregate rating']]

class ActionSearchRestaurants(Action):
    def name(self):
        return 'action_search_restaurants'

    def run(self, dispatcher, tracker, domain):
        #config={ "user_key":"f4924dc9ad672ee8c4f8c84743301af5"}
        loc = tracker.get_slot('location')
        loc_res = location_check(City=loc)
        cuisine = tracker.get_slot('cuisine')
        budget = tracker.get_slot('Budget')
        results = RestaurantSearch(City=loc,Cuisine=cuisine,Budget=Budget)
        response=""
        if results.shape[0] == 0:
            response= "no results"
        else:
            i = 1
            for restaurant in RestaurantSearch(loc,cuisine,budget).iloc[:5].iterrows():
                restaurant = restaurant[1]
                response_title = "Showing you top rated restaurants: \n"
                response = response + str(i) + f". {restaurant['Restaurant Name']} in {restaurant['Address']}. And the average price for two people here is: Rs{restaurant['Average Cost for two']} \n\n"
                i+=1
            response = response_title + response
	
        dispatcher.utter_message('Sent. Bon Appetit!')
        #return [SlotSet('location',loc)]

class ActionSendMail(Action):
    def name(self):
        return 'action_send_mail'

    def run(self, dispatcher, tracker, domain):
        MailID = tracker.get_slot('emailid')
        
        i = 1
        for restaurant in RestaurantSearch(loc,cuisine,budget).iloc[:10].iterrows():
            restaurant = restaurant[1]
            response_title = "Showing you top rated restaurants: \n"
            response = response + str(i) + f". {restaurant['Restaurant Name']} in {restaurant['Address']}. And the average price for two people here is: Rs{restaurant['Average Cost for two']} \n\n"
            i+=1
        response = response_title + response

        sendmail(MailID,response)
        dispatcher.utter_message('Sent. Bon Appetit!')
        #return [SlotSet('emailid',MailID)]

