# **MARVEL TASKS🔥**
------------------------------------------------------
## **Task 1: 3D Printing**

Learnt how to use 3D printer. STL file which is the real pre model file to which the printer creates model. Learnt slicing, giving appropriate adjustments, etc using Ultimaker Cura. Cura - converts the .stl file to printer readable instructions .gcode
When gcode was sent to printer, which printed the object  layer by layer.

## ⚡ Task 2: API

### 🌐 What is an API?
An **API (Application Programming Interface)** is a set of rules and tools that allows different software applications to communicate with each other.  
It defines the methods and data formats that applications can use to **request and exchange information**.  

APIs facilitate the integration of different systems, enabling them to **work together seamlessly**.

## 🌦️ Weather API Integration (Example)

The following code integrates the **OpenWeather API** with jQuery to fetch and display live weather data.

```javascript
$(function () {
  $("#myForm").submit(function (e) {
    e.preventDefault();

    var city = $("#city").val();

    getWeather(city);
  });
});

function getWeather(city) {
  $(".weather-temperature").openWeather({
    key: "ea5ceda552fc62d695e46455e0a5ddbb",
    city: city,
    descriptionTarget: ".weather-description",
    windSpeedTarget: ".weather-wind-speed",
    minTemperatureTarget: ".weather-min-temperature",
    maxTemperatureTarget: ".weather-max-temperature",
    humidityTarget: ".weather-humidity",
    sunriseTarget: ".weather-sunrise",
    sunsetTarget: ".weather-sunset",
    placeTarget: ".weather-place",
    iconTarget: ".weather-icon",
    customIcons: "../src/img/icons/weather/",
    success: function (data) {
      // show weather
      $(".weather-wrapper").show();
      console.log(data);
    },
    error: function (data) {
      console.log(data.error);
      $(".weather-wrapper").remove();
    },
  });
}


![Logo](https://github.com/baswantrayallad/uvce-marvel-tasks/blob/master/assets/TASK%202%20API.png?raw=true)

---

## 🐙 Task 3: Working with GitHub

### 🌐 What is GitHub?
GitHub is a platform that allows developers to **automate software development workflows** directly within a repository.  
It supports **Continuous Integration and Continuous Deployment (CI/CD)** processes, making it easier for teams to collaborate and streamline their pipelines.

---

### 🍴 Forking
- **Forking** means creating a **personal copy** of someone else’s repository.  
- This copy includes the entire version history of files.  
- A fork lets you experiment or modify the project **without affecting the original repo**.

---

### 🔄 Pull Request (PR)
- A **Pull Request** is a **proposed code change** submitted by a developer.  
- It is used for **review and integration** into the main codebase.  
- PRs enable:
  - Peer code reviews 👨‍💻👩‍💻  
  - Discussion before merging  
  - Maintaining code quality ✅  

---

✨ **In short**:  
- Fork → Copy a project  
- Edit → Make changes in your fork  
- PR → Propose your changes to the original project











