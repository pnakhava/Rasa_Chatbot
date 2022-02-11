## intent:affirm
- yes
- yep
- yeah
- indeed
- that's right
- ok
- great
- right, thank you
- correct
- great choice
- sounds really good
- thanks
- Thanks
- yes. Please

## intent:deny
- no
- no. Thanks
- n
- nope
- never
- nay
- nah
- I don't think so
- no way
- not really
- no. thanks

## intent:goodbye
- bye
- goodbye
- good bye
- stop
- end
- farewell
- Bye bye
- have a good one
- Thanks
- thanks
- no. thanks
- see you later
- seeya
- have a nice day
- Okay. Bon Appetit!

## intent:greet
- hey
- howdy
- hey there
- hello
- hi
- good morning
- good evening
- good afternoon
- dear sir
- hi
- hi
- hola
- Hola
- Hey
- Hi
- Hello!

## intent:restaurant_search
- i'm looking for a place to eat
- I want to grab lunch
- I am searching for a dinner spot
- I am looking for some restaurants in [Delhi](location).
- I am looking for some restaurants in [Bangalore](location)
- show me [chinese](cuisine) restaurants
- show me [chines](cuisine:chinese) restaurants in the [New Delhi](location:Delhi)
- show me a [mexican](cuisine) place in the [centre](location)
- i am looking for an [indian](cuisine) spot called olaolaolaolaolaola
- search for restaurants
- anywhere in the [west](location)
- I am looking for [asian fusion](cuisine) food
- I am looking a restaurant in [294328](location)
- in [Gurgaon](location)
- [South Indian](cuisine)
- [North Indian](cuisine)
- [Italian](cuisine)
- [Chinese](cuisine:chinese)
- [chinese](cuisine)
- [Lithuania](location)
- [bengaluru](location)
- yes. Please send it to [ahbcdj@dkj.com](emailid)
- Oh, sorry, in [Italy](location)
- in [delhi](location)
- I am looking for some restaurants in [Mumbai](location)
- I am looking for [mexican indian fusion](cuisine)
- can you book a table in [rome](location) in a [moderate](price:mid) price range with [british](cuisine) food for [four](people:4) people
- [central](location) [indian](cuisine) restaurant
- please help me to find restaurants in [pune](location)
- Please find me a restaurantin [bangalore](location)
- in [Mumbai](location)
- [Chinese](cuisine:chinese)
- show me restaurants
- [mumbai](location)
- [Italian](cuisine)
- I’ll prefer [thai](cuisine)
- [300-700](budget) range
- please find me [chinese](cuisine) restaurant in [delhi](location)
- can you find me a [chinese](cuisine) restaurant
- [delhi](location)
- please find me a restaurant in [ahmedabad](loscation)
- please show me a few [italian](cuisine) restaurants in [bangalore](location)
- I’m hungry. Looking out for some good restaurants
- Can you suggest some good restaurants in [Allahabad](location)
- Can you suggest some good restaurants in [kolkata](location)
- I’m hungry. Looking out for some good [chinese](cuisine) restaurants in [chandigarh](location)
- Okay. Show me some in [Allahabad](location)
- I’ll prefer [chines](cuisine)
- [>700](budget)
- yes. Please send it to [xyz@sth.edu](emailid)
- [american](cuisine)
- [<300](budget)
- [jddk.2jmd@kdl.co.in](emailid)
- I’m hungry. Looking out for some good chinese restaurants in [chandigarh](location)

## synonym:4
- four

## synonym:2
- two

## synonym:Delhi
- New Delhi
- Dilli

## synonym:Bengaluru
- Bangalore

## synonym:Mumbai
- Bombay

## synonym:Pune
- Poona

## synonym:Gurgaon
- Gurugram

## synonym:Chennai
- Madras

## synonym:Bokaro
- Bokaro Steel City

## synonym:Dehradun
- Dera Doon

## synonym:Coimbatore
- Covai
- Kovai

## synonym:Jamshedpur
- Tatanagar

## synonym:Hubli-Dharwad
- Hubli
- Dharwad

## synonym:Visakhapatnam
- Vizagapatam

## synonym:Vijayawada
- Bezawada

## synonym:Varanasi
- Kashi
- Benares
- Banaras

## synonym:Vadodara
- Baroda

## synonym:Vijayapura
- Bijapur

## synonym:Tirunelveli
- Tinnevelly
- Nellai

## synonym:Tiruchirappalli
- Trichy
- Tiruchi

## synonym:Thrissur
- Trichur
- Thrisshivaperur

## synonym:Thanjavur
- Tanjore

## synonym:Shimla
- Simla

## synonym:Ratlam
- Ratnapuri

## synonym:Rajamahendravaram
- Rajahmundry

## synonym:Prayagraj
- Allahabad
- Ilahabad

## synonym:Puducherry
- Pondicherry

## synonym:Mysore
- Mysuru

## synonym:Kannur
- Cannanore
- Kannanur
- Cananor

## synonym:Kanpur
- Cawnpore

## synonym:Kochi
- Cochin

## synonym:Kozhikode
- Calicut

## synonym:Mangalore
- Mangaluru

## synonym:chinese
- chines
- Chinese
- Chines

## synonym:mid
- moderate

## synonym:vegetarian
- veggie
- vegg

## regex:greet
- hey[^\s]*
- hello[^\s]*

## regex:pincode
- [0-9]{6}

## regex:emailid
- ^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$