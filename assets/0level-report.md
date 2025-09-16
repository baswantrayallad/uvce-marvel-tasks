# **MARVEL TASKS🔥**
------------------------------------------------------
## **Task 1: 3D Printing**

Learnt how to use 3D printer. STL file which is the real pre model file to which the printer creates model. Learnt slicing, giving appropriate adjustments, etc using Ultimaker Cura. Cura - converts the .stl file to printer readable instructions .gcode
When gcode was sent to printer, which printed the object  layer by layer.

##  Task 2: API

###  What is an API?
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
```
---

 ![Logo](https://github.com/baswantrayallad/uvce-marvel-tasks/blob/master/assets/TASK%202%20API.png?raw=true)

---

##  Task 3: Working with GitHub

###  What is GitHub?
GitHub is a platform that allows developers to **automate software development workflows** directly within a repository.  
It supports **Continuous Integration and Continuous Deployment (CI/CD)**, making it easier for teams to collaborate and streamline their development pipelines.

---

### Forking
- **Forking** means creating a **personal copy** of someone else’s repository.  
- This copy contains all the files and complete version history.  
- A fork allows you to **experiment or modify** without affecting the original project.  

---

### Pull Request (PR)
- A **Pull Request (PR)** is a way to **propose code changes** to a project.  
- Developers submit a PR for **review and integration** into the main codebase.  
- PRs are essential for:
  - Peer code reviews   
  - Team collaboration 
  - Maintaining project quality  

---

 **In summary:**  
- **Fork** → Copy the repository  
- **Edit/Commit** → Make your changes  
- **Pull Request** → Suggest changes to be merged into the original project

 ![Logo](https://github.com/baswantrayallad/uvce-marvel-tasks/blob/master/assets/TASK%203%20Working%20with%20github%201.png?raw=true)

  ![Logo](https://github.com/baswantrayallad/uvce-marvel-tasks/blob/master/assets/TASK%203%20Working%20with%20github%202.png?raw=true)

 ![Logo](https://github.com/baswantrayallad/uvce-marvel-tasks/blob/master/assets/TASK%203%20Working%20with%20github%203.png?raw=true)

 ---

 # Task 4: Get familiar with the command line on ubuntu:

* Create a folder named test.
* cd into that folder.
* Create a blank file without using any text editor.
* List the files in that folder.
* Create 2600 folders in this folder where each folder is named M90.
```shell
for i in {1..2600}; do
    mkdir "M$i"
done
```
* Concatenate two text files containing any random text and display them on the terminal.
```shell
echo "Random Text File 1" > file1.txt
echo "Random Text File 2" > file2.txt
cat file1.txt file2.txt
```

![Logo](https://github.com/baswantrayallad/uvce-marvel-tasks/blob/master/assets/TASK%204%20Working%20with%20ubuntu%201.png?raw=true)

![Logo](https://github.com/baswantrayallad/uvce-marvel-tasks/blob/master/assets/TASK%204%20Working%20with%20ubuntu%202.png?raw=true)



## Task 5: Build Your Own Brain - Linear Regression from Scratch


In this task, we dive into the **core of machine learning** by implementing **Linear Regression from scratch** and comparing it with **scikit-learn’s implementation**.  
We will use the **California Housing dataset** to test the model on real-world data.

1. **Linear Regression Fundamentals**  
   - Understood how a straight line can be used to model the relationship between features and target values.  
   - Learned the role of weights and bias in fitting the model.  

2. **Gradient Descent Optimization**  
   - Realized how gradient descent updates weights step by step to minimize error.  
   - Saw the importance of choosing the right learning rate to ensure convergence.  

3. **Feature Scaling Importance**  
   - Learned that without normalization/standardization, gradient descent becomes slow or unstable.  

4. **Model Evaluation Metrics**  
   - Understood how to measure model performance using **MSE, MAE, and R² Score**.  
   - Learned how each metric provides a different perspective on accuracy.  

5. **Scratch vs Scikit-learn**  
   - Implementing from scratch gave me a clear view of the math behind the model.  
   - Using scikit-learn showed the power and convenience of built-in libraries.  
   - I understood the trade-off between **learning by building from scratch** vs **efficiency in real-world projects**.  

 ![Logo](https://github.com/baswantrayallad/uvce-marvel-tasks/blob/master/assets/TASK%205%20Linear%20Regression%201.png?raw=true)
 

## Task 6: The Matrix Puzzle — Decode with NumPy & Reveal the Image

In this task, I worked with **NumPy** and **Matplotlib** to solve a visual puzzle.  
The goal was to decode a scrambled matrix and reconstruct the hidden image using array operations.

---

### Objectives
- Manipulate and decode a scrambled NumPy matrix.  
- Apply **reshaping, slicing, flipping, and transposing** operations.  
- Visualize the hidden image using `matplotlib.pyplot.imshow()`.  

---

### Expected Outcomes
- Confidence with **NumPy operations** like reshaping, slicing, flipping, transposing.  
- Ability to **visualize 2D arrays** as images.  
- Improved **debugging & puzzle-solving skills** through experimentation.


 ![Logo](https://github.com/baswantrayallad/uvce-marvel-tasks/blob/master/assets/TASK%206%20Matrix%20Puzzle%201.png?raw=true)

![Logo](https://github.com/baswantrayallad/uvce-marvel-tasks/blob/master/assets/TASK%206%20Martix%20Puzzle%202.png?raw=true)


## **Task 7: Creating Portfolio webpage**
I have created  a basic portfolio webpage using HTML + CSS (Tailwind) + JavaScript (React/Next.js).

 ![Logo](https://github.com/baswantrayallad/uvce-marvel-tasks/blob/master/assets/TASK%207%20portfolio.png?raw=true)

[link](https://github.com/baswantrayallad/portfolio-website)

---------------------

## **Task 8: Writting Resource Article**

I have writen an article on process-multithreading

[link](https://github.com/baswantrayallad/uvce-marvel-tasks/blob/master/TASK%208%20%20Resource%20Article/process-vs-thread/process-multithreading.md)

## **Task 9: TinkedCad**
Tinkercad Circuits is a free, browser-based electronic circuit simulator that allows users to design, test, and program electronic circuits online without needing physical hardware.
It supports popular microcontrollers like the Arduino Uno, Micro, H-brigde, potentiometer, BreadBoard etc.

![Logo](https://github.com/baswantrayallad/uvce-marvel-tasks/blob/master/assets/TASK%209%20Thinkercad.png?raw=true)

## **Task 10: Speed Control of DC Motor**

The task of **speed control of a DC motor using Arduino UNO and L298N motor driver** was successfully completed. The experiment provided practical exposure to motor driver interfacing, PWM control, and real-time hardware validation.

![Logo](https://github.com/baswantrayallad/uvce-marvel-tasks/blob/master/assets/TASK%2010%20%20Speed%20Control%20of%20DC%20Motor.png?raw=true)




### Task 11: LED Toggle Using ESP32  

For this task, I worked with the **ESP32 microcontroller** and learned how to create a web server to control an LED through its GPIO pins. I Installed and configured **Arduino IDE** with ESP32 board support. Connected the ESP32 board and verified communication with the IDE. Wrote and uploaded a program that created a simple web server. Served an HTML page with **ON/OFF buttons**. Accessed the ESP32’s **IP address** via a browser. Controlled an LED connected to ESP32 GPIO pins based on user input.  

![ESP32 toggling LED's](https://github.com/baswantrayallad/uvce-marvel-tasks/blob/master/assets/TASK%2011%20ESP32%20GIF.mp4?raw=true)

---

## **Task 12: Soldering Prerequisites**

As part of this task, I familiarized myself with the soldering equipment available in the lab, including the soldering iron, solder wire, flux, and soldering wick. The coordinator demonstrated the safe handling of these tools and explained their purpose.

![Logo](https://github.com/baswantrayallad/uvce-marvel-tasks/blob/master/assets/TASK%2012%201.png?raw=true)

I then performed a basic soldering exercise on a perf board (green PCB) by soldering a single LED. This gave me hands-on practice in heating the joint, applying solder.,,
![Logo](https://github.com/baswantrayallad/uvce-marvel-tasks/blob/master/assets/TASK%2012%202.png?raw=true)

## Task 14: Karnaugh Maps and Deriving the Logic Circuit  

In this task, I learned how to use **Karnaugh Maps (K-Maps)** to simplify Boolean expressions and design a simple burglar alarm circuit.  
The burglar alarm should work based on the whether the **door is locked or open**, whether the **key is pressed or not pressed**.  By using these conditions on a **4-variable K-Map**, I identified the simplified Boolean expression for the output. This logic was then used to design a circuit using **logic gates**. 

### Image:
![Logo](https://github.com/baswantrayallad/uvce-marvel-tasks/blob/master/assets/TASK%2014%20Kmap.png?raw=true)  


## **Task 15: Participation**

### **MARVELops: DOCKER 101 WORKSHOP CONDUCTED BY MARVEL**

![Logo](https://github.com/baswantrayallad/uvce-marvel-tasks/blob/master/assets/TASK%2015%20Active%20Participation.png?raw=true)


---------------

## **Task 18: Sad Servers**

One of my Fav. task - we are time-bound of 20 mins, we needed to find the Murderer name, there were 20 total hints but i viewed only 3, and i was able to do it in 12 mins, used a bunch of linux kernal commands "grep", "tail" and grep -A5 for first lines and grep - C5 for first and last 5 lines. and the murderer name echoin "mysolution" file and displayed the md5sum encryption which matched the expected outcome.


### **Snippets:**
![Logo](https://github.com/Shrihari6/Marvel-Level0/blob/DA_chatbot/Photos/Task%2018(1).png?raw=true)
![Logo](https://github.com/Shrihari6/Marvel-Level0/blob/DA_chatbot/Photos/Task%2018(2).png?raw=true)
![Logo](https://github.com/Shrihari6/Marvel-Level0/blob/DA_chatbot/Photos/Task%2018(3).png?raw=true)
![Logo](https://github.com/Shrihari6/Marvel-Level0/blob/DA_chatbot/Photos/Task%2018(4).png?raw=true)
![Logo](https://github.com/Shrihari6/Marvel-Level0/blob/DA_chatbot/Photos/Task%2018(6).png?raw=true)
![Logo](https://github.com/Shrihari6/Marvel-Level0/blob/DA_chatbot/Photos/Task%2018(7).png?raw=true)

------------------




## **Task 19: Making of a WebApp - Notes-made-easy**
i have used JavaScript for working of taking input note, adding and deletion.
Html5 for frontend
Css for styling and cascading the webapp

![Logo](https://github.com/baswantrayallad/uvce-marvel-tasks/blob/master/assets/Task%2019%20Web%20app.png?raw=true)

[Website Link](marvel-task-19-zeta.vercel.app)

[Github Repo](https://github.com/baswantrayallad/marvel-task-19)













  

 










































