# TravelPlanner
Django Web Application which uses OpenAI &amp; OpenWeatherMap APIs for Travel Planning 

- User Can Enter a Prompt e.g. `I would like to go bhopal from delhi for 3 days` in any format
- Website will automatically detect the `Source`, `Destination` & `Total No. of Days`.

It will provide following `data` in `Tabular Format`:

- Source Place Weather Info for Current Day
- Destination Place Weather Info for N no. of days
- Recommendations Based on Humidity & Temperature Difference

## Project Information
This project was developed for a `24 hour long Hackathon`, where main `aim` was to `utilise` `OpenWeatherMap API` & build a project by solving real world problem.
Our project was able to qualify 1st round.

## Design
![Design](Design/Design.JPG)

## Technology Used
- Django
- Bootstrap
- OpenAI API
- OpenWeather API
- Javascript
- HTML
- CSS

## Installation
```
cd TravelPlanner
python -m pip install -r requirements.txt
# Update openai_key & openweather_key in TravelPlanner/home/views.py
python manage.py makemigrations
python manage.py migrate
```

## How to Run
```
python manage.py runserver 
```

## Hackathon Teammate
<table>
<tr>

<td align="center">
    <a href="https://github.com/arushi167">
        <kbd><img src="https://avatars3.githubusercontent.com/arushi167?size=400" width="100px;" alt=""/></kbd><br />
        <sub><b>Arushi Jain</b></sub>
    </a><br />
</td>

<td align="center">
    <a href="https://github.com/PushpenderIndia">
        <kbd><img src="https://avatars3.githubusercontent.com/PushpenderIndia?size=400" width="100px;" alt=""/></kbd><br />
        <sub><b>Pushpender Singh</b></sub>
    </a><br />
</td>

<td align="center">
    <a href="https://github.com/Ayushi0405">
        <kbd><img src="https://avatars3.githubusercontent.com/Ayushi0405?size=400" width="100px;" alt=""/></kbd><br />
        <sub><b>Ayushi Gupta</b></sub>
    </a><br />
</td>

<td align="center">
    <a href="https://github.com/Yuvraj0208">
        <kbd><img src="https://avatars3.githubusercontent.com/Yuvraj0208?size=400" width="100px;" alt=""/></kbd><br />
        <sub><b>Yuvraj Singh</b></sub>
    </a><br />
</td>

</tr>
</tr>
</table>



