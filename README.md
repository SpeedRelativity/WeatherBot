# WeatherBot
Using OpenWeatherAPI to create a discord weather bot.

Here's how it works:

1. Get Weather API Key from here: https://openweathermap.org/api -- Basically the service key.
Now that we have permission/the service granted, we need to take that and format it.

2. Weather_app.py does that job. It takes the data and formats it into a dictionary and takes out the necessary parts. I only used the temperature, you are free to use whatever.
3. Next, you setup the discord message system in Bot.py
4. You import the response from weatherapp, and make it so whenever someone puts "!weather" in the chat, it replies with that weatherAPI response that we formatted in weather_app.py

That's pretty much it. The code is not too advanced, a beginner could understand it with a little time.

This is my first project using an API.

I'm sure you can expand this bot further, I only have 1 command, you could use city as a reference variable instead of declaring it like I did.


