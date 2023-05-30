<br />

<img src="https://github.com/zayne-siew/Stretch925/assets/87000020/9a45ff68-f9a0-4dae-ac35-49e1c908a8c9.svg">

<p align="center">
  <img src=https://img.shields.io/badge/python-3.8%20%7C%203.9-blue.svg alt="Python Versions"/>
  <a href=http://hits.dwyl.com/zayne-siew/Stretch925><img src=https://hits.dwyl.com/zayne-siew/Stretch925.svg?style=flat-square&show=unique alt="Hit Count" /></a>
</p>

<h4 align="center">
  <a href="https://youtu.be/Kcc65jPpa4Y">Video</a>
  <span> · </span>
  <a href="https://github.com/zayne-siew/Stretch925/issues">Report a bug</a>
</h4>

---

**Stretch925** is an application that utilizes gamification and computer vision to promote a healthy stretching habit among corporate workers. An accessible, interactive, and smart digital solution, Stretch925 incentivises and rewards corporate workers for taking care of their well-being.

## Features

### Gamification and Rewards
Research showed that stretching at work can help loosen stiff muscles and provide energy to the tired workers.

Through a fun interactive game, Stretch925 seeks to promote a healthy stretching habit. After a random selection of 3 stretches, users can ultise their camera to perform the given stretch repetitions. Points are awarded based on the number of repetitions performed. Users can then use the points to redeem from Stretch925’s amazing catalogue of rewards.

### Accurate Detection of Stretch Repetitions
Stretch925 leverages on [PeekingDuck](https://github.com/aisingapore/PeekingDuck) to obtain pose estimations 
and counts the number of stretch repetitions performed by the user.
Some of these stretches currently supported are:

- **Y-W Stretch** - Extend both arms straight up above your head. Form a Y shape. Next, tuck both arms to your stomach area and squeeze your shoulder blades together. Form a “W” shape.
  <p align="center">
   <img src= https://github.com/zayne-siew/Stretch925/assets/87000020/6971af29-323f-47c9-a990-00079084771c.gif alt="Sample Video 1" width=20% height=auto/>
  </p>
- **Neck Stretch** - Place one hand on the opposite side of your head and tuck the other hand behind your back. Bring the head down towards your shoulder. Hold for 10 seconds.
  <p align="center">
   <img src= https://github.com/zayne-siew/Stretch925/assets/87000020/34fd5a5f-d421-422f-b31e-f80b31a031ef.gif alt="Sample Video 2" width=20% height=auto/>
  </p>
- **Side Stretch** - Extend both arms straight up above your head. Grab your right hand with left hand. Assist with your left hand and stretch to the side.
  <p align="center">
   <img src= https://github.com/zayne-siew/Stretch925/assets/87000020/4eed5f47-7c92-4ea9-bcc5-d92d8244427f.gif alt="Sample Video 3" width=20% height=auto/>
  </p>

### Boosts Productivity
Stretch925 uses the Pomodoro technique to help corporate workers break a long workday into short 25-minute focus periods followed by 5-minute breaks. Doing so enables individuals to maintain focus and accomplish necessary tasks while also providing opportunities for quick energy replenishment during designated breaks.

## Usage

### Installation

1. Refer to the [PeekingDuck installation guide](https://peekingduck.readthedocs.io/en/stable/getting_started/index.html) to install PeekingDuck.

2. [Fork](https://github.com/zayne-siew/Stretch925/fork) or clone this repository to access the source code.

### Physical set-up

4. Prepare the physical environment. Some recommendations for setting up prior to deploying Stretch925 include:

- Place the video-capturing device on a level surface at a suitable distance away from the user(s). Ideally, the video should capture at least the **full top half of the user**.
- Capture the video against a monotone surface such as a wall or a green screen, if possible.
- The body of the user should face the camera directly at all times, if possible. Avoid turning to the side as this will mess with the detection algorithm.

### Deployment

5. To access the isolated **computer vision model**, navigate to the root directory in the terminal and run

````
cd cv
python main.py { arm | neck | side }
````

6. To access the **web application**, navigate to the root directory in the terminal and run

````
cd web-app
npm run dev
````

## Gallery
All of these mockup images can be accessed in the **figma-mockups.zip** file in the repository.

### Sign In
<p align="left">
   <img src= https://github.com/zayne-siew/Stretch925/assets/87000020/faadc74e-00f0-41e7-af42-d72dc0dc7604.png alt="Sign In" width=20% height=auto/>
</p>

### View Stretches
<p align="left">
   <img src= https://github.com/zayne-siew/Stretch925/assets/87000020/90f54ef3-3104-48f1-9e49-e2e9f768a392.png alt="View Stretches" width=20% height=auto/>
</p>

### Home - During Work Session
<p float="left">
  <img src="https://github.com/zayne-siew/Stretch925/assets/87000020/dd448ca6-6aac-4ba4-a684-06d584fb0a5f.png" width=20% height=auto/ />
  <img src="https://github.com/zayne-siew/Stretch925/assets/87000020/8ba5a243-cc14-4674-a1eb-bfcc880f732d.png" width=20% height=auto/ />
  <img src="https://github.com/zayne-siew/Stretch925/assets/87000020/1380303f-d330-49a9-92b3-5c6036afd6b8.png" width=20% height=auto/ />
</p>

### Home - During Break Session
<p float="left">
  <img src="https://github.com/zayne-siew/Stretch925/assets/87000020/a19f5253-71c0-42ea-a00b-96c130648d7c.png" width=20% height=auto/ />
  <img src="https://github.com/zayne-siew/Stretch925/assets/87000020/76c771c5-aa6b-4911-b9c4-5783191bb679.png" width=20% height=auto/ />
  <img src="https://github.com/zayne-siew/Stretch925/assets/87000020/96ce711a-ae65-4f3f-99e1-09a2ddddb2ec.png" width=20% height=auto/ />
  <img src="https://github.com/zayne-siew/Stretch925/assets/87000020/d840d5a7-f176-4a2c-8997-323e7e256e13.png" width=20% height=auto/ />
  <img src="https://github.com/zayne-siew/Stretch925/assets/87000020/748b0fe1-8a7f-4df2-bbee-96b56b2e43df.png" width=20% height=auto/ />
  <img src="https://github.com/zayne-siew/Stretch925/assets/87000020/5befa4fa-9301-423b-bdfc-cabea107b660.png" width=20% height=auto/ />
</p>

### Ranking
<p float="left">
  <img src="https://github.com/zayne-siew/Stretch925/assets/87000020/cc985b6b-9501-47bd-a24e-70b1b40c3f1d.png" width=20% height=auto/ />
  <img src="https://github.com/zayne-siew/Stretch925/assets/87000020/e99b550b-39b5-49f6-ba19-9823b9276da7.png" width=20% height=auto/ />
</p>

### Activity
<p align="left">
   <img src= https://github.com/zayne-siew/Stretch925/assets/87000020/61a9300c-941a-4a5f-b7ea-f1a7bc348352.png alt="Activity" width=20% height=auto/>
</p>

### Profile
<p align="left">
   <img src= https://github.com/zayne-siew/Stretch925/assets/87000020/ffe7ff0a-9867-4b9f-9fc8-0ca08adeda0f.png alt="Profile" width=20% height=auto/>
</p>

## Acknowledgements
This project is an undertaking of the LifeHack 2023 organised by NUS Students' Computing Club, under the Theme: Revolutionizing the Workplace.



