<br />

<img src="https://github.com/zayne-siew/Stretch925/assets/87000020/601a20a2-e419-4033-9c6c-236fdd1348f7.svg">

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

**Stretch925** is an application that rewards fatigued corporate workers for taking their much-needed breaks and promotes a healthy stretching habit through gamification. It is available both on web and mobile.
All users must perform a one-time Singpass login to sign up for Stretch925.

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
   <img src= https://github.com/zayne-siew/Stretch925/assets/87000020/066eab37-ccbc-4968-82b4-0c5974eaf8be.gif alt="Sample Video 1" width=20% height=auto/>
  </p>
- **Neck Stretch** - Place one hand on the opposite side of your head and tuck the other hand behind your back. Bring the head down towards your shoulder. Hold for 10 seconds.
  <p align="center">
   <img src= https://github.com/zayne-siew/Stretch925/assets/87000020/4c0fca7b-ef4f-4ae9-8a36-7678cdd33263.gif alt="Sample Video 2" width=20% height=auto/>
  </p>
- **Side Stretch** - Extend both arms straight up above your head. Grab your right hand with left hand. Assist with your left hand and stretch to the side.
  <p align="center">
   <img src= https://github.com/zayne-siew/Stretch925/assets/87000020/53a08eea-f096-4452-9617-33bf8e289737.gif alt="Sample Video 3" width=20% height=auto/>
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

5. Navigate to the root directory in the terminal and run

````
python main.py { arm | neck | side }
````

## Gallery
### Sign In
<p align="left">
   <img src= https://github.com/zayne-siew/Stretch925/assets/87000020/64f8ebb4-f0d8-40a2-bc2f-0330a1910a7b.png alt="Sign In" width=20% height=auto/>
</p>

### View Stretches
<p align="left">
   <img src= https://github.com/zayne-siew/Stretch925/assets/87000020/f93dd013-d083-4abb-b850-3b17c8bd712a.png alt="View Stretches" width=20% height=auto/>
</p>

### Home - During Work Session
<p float="left">
  <img src="https://github.com/zayne-siew/Stretch925/assets/87000020/e6995f1f-6cfe-4184-aa6f-fa0ac315c0f1.png" width=20% height=auto/ />
  <img src="https://github.com/zayne-siew/Stretch925/assets/87000020/0bd6f123-96a6-47ef-9a18-fa26b8b392a5.png" width=20% height=auto/ />
  <img src="https://github.com/zayne-siew/Stretch925/assets/87000020/a1dd22f3-8647-4deb-bcee-bb8156cfc018.png" width=20% height=auto/ />
</p>

### Home - During Break Session
<p float="left">
  <img src="https://github.com/zayne-siew/Stretch925/assets/87000020/3f33bc76-3483-4eb8-a1d5-3f95eac0b83d.png" width=20% height=auto/ />
  <img src="https://github.com/zayne-siew/Stretch925/assets/87000020/0ec790b1-59df-4805-b041-202de23141b7.png" width=20% height=auto/ />
  <img src="https://github.com/zayne-siew/Stretch925/assets/87000020/6f5d249f-a174-456d-b60c-90686b1daf85.png" width=20% height=auto/ />
  <img src="https://github.com/zayne-siew/Stretch925/assets/87000020/14dfa9a5-73c7-4803-bf9a-39a58d22a01d.png" width=20% height=auto/ />
  <img src="https://github.com/zayne-siew/Stretch925/assets/87000020/068b6b39-3130-4891-918b-b4fcdfbbd419.png" width=20% height=auto/ />
  <img src="https://github.com/zayne-siew/Stretch925/assets/87000020/f33f18e2-4680-4d41-9c67-0a3c9c99b11a.png" width=20% height=auto/ />
</p>

### Ranking
<p float="left">
  <img src="https://github.com/zayne-siew/Stretch925/assets/87000020/3ba58262-cdb3-4bec-b579-8ca94156b3a0.png" width=20% height=auto/ />
  <img src="https://github.com/zayne-siew/Stretch925/assets/87000020/c0ba4f41-6643-4410-994e-8da4bbb5490a.png" width=20% height=auto/ />
</p>

### Activity
<p align="left">
   <img src= https://github.com/zayne-siew/Stretch925/assets/87000020/46ba2d14-9594-49c2-b1c2-27adfe6b9e12.png alt="Activity" width=20% height=auto/>
</p>

### Profile
<p align="left">
   <img src= https://github.com/zayne-siew/Stretch925/assets/87000020/08063d78-5345-4e3b-9a2d-d7947e7135ae.png alt="Profile" width=20% height=auto/>
</p>

## Acknowledgements
This project is an undertaking of the LifeHack 2023 organised by NUS Students' Computing Club, under the Theme: Revolutionizing the Workplace.
