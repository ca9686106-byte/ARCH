// live preview weather dashboard functionality

const apiKey = 'YOUR_API_KEY'; // replace with your actual API key
const weatherOutput = document.getElementById('weatherOutput');
const cityInput = document.getElementById('cityInput');
const submitButton = document.getElementById('submitButton');

submitButton.addEventListener('click', () => {
    const city = cityInput.value;
    fetchWeather(city);
});

function fetchWeather(city) {
    fetch(`https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`)
        .then(response => response.json())
        .then(data => showWeather(data))
        .catch(error => console.error('Error fetching weather data:', error));
}

function showWeather(data) {
    if (data.cod !== 200) {
        weatherOutput.innerHTML = `<p>Error: ${data.message}</p>`;
        return;
    }
    const weatherInfo = `<h2>${data.name}</h2>
                        <p>Temperature: ${data.main.temp} °C</p>
                        <p>Weather: ${data.weather[0].description}</p>`;
    weatherOutput.innerHTML = weatherInfo;
}
