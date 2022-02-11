stories:

- story: complete path1
  steps:
  - intent: greet
  - action: utter_greet
  - intent: restaurant_search
  - action: utter_ask_location
  - intent: restaurant_search
  - action: utter_ask_cuisine
  - intent: restaurant_search
  - action: utter_ask_budget
  - intent: restaurant_search
  - action: utter_search_restaurants
  - action: utter_ask_email
  - intent: affirm
  - action: utter_ask_emailid
  - intent: restaurant_search
  - action: utter_send_mail
  - action: utter_goodbye

- story: complete path2
  steps:
  - intent: greet
  - action: utter_greet
  - intent: restaurant_search
  - action: utter_ask_location
  - intent: restaurant_search
  - action: utter_ask_cuisine
  - intent: restaurant_search
  - action: utter_ask_budget
  - intent: restaurant_search
  - action: utter_search_restaurants
  - action: utter_ask_email
  - intent: deny
  - action: utter_goodbye

- story: complete path3
  steps:
  - intent: greet
  - action: utter_greet
  - intent: restaurant_search
  - action: utter_ask_location
  - intent: restaurant_search
  - action: utter_ask_cuisine
  - intent: restaurant_search
  - action: utter_ask_budget
  - intent: restaurant_search
  - action: utter_search_restaurants
  - action: utter_ask_email
  - intent: restaurant_search
  - action: utter_send_mail
  - action: utter_goodbye

- story: location known1
  steps:
  - intent: greet
  - action: utter_greet
  - intent: restaurant_search
  - action: utter_ask_cuisine
  - intent: restaurant_search
  - action: utter_ask_budget
  - intent: restaurant_search
  - action: utter_search_restaurants
  - action: utter_ask_email
  - intent: affirm
  - action: utter_ask_emailid
  - intent: restaurant_search
  - action: utter_send_mail
  - action: utter_goodbye

- story: location known2
  steps:
  - intent: greet
  - action: utter_greet
  - intent: restaurant_search
  - action: utter_ask_cuisine
  - intent: restaurant_search
  - action: utter_ask_budget
  - intent: restaurant_search
  - action: utter_search_restaurants
  - action: utter_ask_email
  - intent: deny
  - action: utter_goodbye

- story: location wrong1
  steps:
  - intent: greet
  - action: utter_greet
  - action: utter_ask_location
  - intent: restaurant_search
  - action: utter_ask_cuisine
  - intent: restaurant_search
  - action: utter_ask_budget
  - intent: restaurant_search
  - action: utter_search_restaurants
  - action: utter_ask_email
  - intent: affirm
  - action: utter_ask_emailid
  - intent: restaurant_search
  - action: utter_send_mail
  - action: utter_goodbye

- story: cuisine known1
  steps:
  - intent: greet
  - action: utter_greet
  - intent: restaurant_search
  - action: utter_ask_location
  - intent: restaurant_search
  - action: utter_ask_budget
  - intent: restaurant_search
  - action: utter_search_restaurants
  - action: utter_ask_email
  - intent: affirm
  - action: utter_ask_emailid
  - intent: restaurant_search
  - action: utter_send_mail
  - action: utter_goodbye

- story: cuisine known2
  steps:
  - intent: greet
  - action: utter_greet
  - intent: restaurant_search
  - action: utter_ask_location
  - intent: restaurant_search
  - action: utter_ask_budget
  - intent: restaurant_search
  - action: utter_search_restaurants
  - action: utter_ask_email
  - intent: deny
  - action: utter_goodbye

- story: budget known1
  steps:
  - intent: greet
  - action: utter_greet
  - intent: restaurant_search
  - action: utter_ask_location
  - intent: restaurant_search
  - action: utter_ask_cuisine
  - intent: restaurant_search
  - action: utter_search_restaurants
  - action: utter_ask_email
  - intent: affirm
  - action: utter_ask_emailid
  - intent: restaurant_search
  - action: utter_send_mail
  - action: utter_goodbye

- story: budget known2
  steps:
  - intent: greet
  - action: utter_greet
  - intent: restaurant_search
  - action: utter_ask_location
  - intent: restaurant_search
  - action: utter_ask_cuisine
  - intent: restaurant_search
  - action: utter_search_restaurants
  - action: utter_ask_email
  - intent: deny
  - action: utter_goodbye

- story: location cuisine known1
  steps:
  - intent: greet
  - action: utter_greet
  - intent: restaurant_search
  - action: utter_ask_budget
  - intent: restaurant_search
  - action: utter_search_restaurants
  - action: utter_ask_email
  - intent: affirm
  - action: utter_ask_emailid
  - intent: restaurant_search
  - action: utter_send_mail
  - action: utter_goodbye

- story: location cuisine known2
  steps:
  - intent: greet
  - action: utter_greet
  - intent: restaurant_search
  - action: utter_ask_budget
  - intent: restaurant_search
  - action: utter_search_restaurants
  - action: utter_ask_email
  - intent: deny
  - action: utter_goodbye

- story: location cuisine budget known1
  steps:
  - intent: greet
  - action: utter_greet
  - intent: restaurant_search
  - action: utter_search_restaurants
  - action: utter_ask_email
  - intent: affirm
  - action: utter_ask_emailid
  - intent: restaurant_search
  - action: utter_send_mail
  - action: utter_goodbye

- story: location cuisine budget known2
  steps:
  - intent: greet
  - action: utter_greet
  - intent: restaurant_search
  - action: utter_search_restaurants
  - action: utter_ask_email
  - intent: deny
  - action: utter_goodbye
