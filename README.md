# Animal Crossing: New Horizons Critterpedia API

#### A Flask-based app that tells you what critters are available based upon the current timestamp

---

#### Motivations

This app was developed entirely because I was bored during The COVID-19 Lockdown of 2020. 

---

#### How to use

- Install a venv if you want and then get required packages 
    - `pip3 install -r requirements.txt`
- run the app
    - `python3 run.py`

If you use something like AWS Lambda or other systems, you are on your own. Fork the repo and modify to your hearts content or put in a PR if you want to add support for other systems. If I like it, I'll add it. 

---

#### Endpoints

There are three endpoints
- health `/health`
- fish `/fish`
- bugs `/bugs`

If you need me to describe what the health endpoint does, this project isn't for you. 

The fish endpoint will return a jsonified blob of all fish that you can obtain at this moment in time on New Horizons

The bugs endpoint is slightly different than the fish endpoint in that it returns... bugs... What else did you expect? 

That's it. It's over. Go home. 

---

#### TO-DO LIST
- Add all of the fish and bugs to the respective dictionaries (I'm lazy and it's tedious. Sue me.)
- Eat cake. 

---

#### Known Issues
- I'm too lazy to code the southern hemisphere. If you need it, you code it. I'm too lazy to deal with that crap and I'm in the north so it does't impact me. ¯\\\_(ツ)\_/¯
