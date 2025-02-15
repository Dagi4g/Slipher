<div align="center">

# Slipher – Personalized Learning tracker

**before moving on:** we want to **thank you** for paying a vist to **slifer** repository

**Slipher** is an innovative app designed to help **high school students** improve their learning experience and there exam score.

It uses a **spaced reptation technique** with personalized notification system to help students retain information better and stay engaged with their studies.

---

## 📖 Table of Contents
- [purpose](#-why-slipher)
- [Code Overview](#-code-overview)
- [Progress So Far](#-progress-so-far)
- [Core Focus](#-core-focus)
- [How to Install](#-how-to-install)
- [How You Can Contribute](#-how-you-can-contribute)
- [License](#license)
- [Thank You](#-thank-you)

---

## 🚀 Why Slipher?
The goal of Slipher is to empower students to **learn and remember better** by:
- Sending **personalized notifications** for review.
- reducing time spent on studying with**spaced repetition** for better retention.
- Helping students stay **actively engaged** with their learning material.

---


## 📦 Code Overview
Slipher uses **Python** and **SQLite** for managing study data.
- **Database:** A SQLite database (`slifer.db`) is initialized using an external SQL file.
- **Subject Management:** The `Subject` class allows users to add subjects to the database via terminal input.
- **Topic Management:** The `Topic` class links topics to existing subjects using subject IDs.
- **User Interaction:** The terminal prompts users to enter subjects and topics, storing them in the database.

---

## 📈 Progress So Far
### ✅ Completed:
- **Database Creation:** A structured database to store subjects and topics.
- **Adding Subjects:** Users can add subjects directly from the terminal.

### 🔜 Next Steps:
- **Simplify Adding Topics & Subtopics:** Improving how topics and subtopics are added from the terminal.
- **Notification System:** Personalized reminders based on the user’s progress.
- **Enhanced User Input:** Refining how users add topics and subtopics for a smoother experience.
- **Improved UI:** Transitioning from a terminal-based interface to a more user-friendly design.
---

## 🎯 Core Focus
Slipher currently focuses on **fundamental features** to ensure the app is stable and effective before expanding into more advanced functionalities.

### 🎯 Core Features

- **Spaced Repetition:** Helps students remember more by optimizing review schedules.

- **Database Management:** Stores all subjects and topics in a structured, scalable format.

- **Customizable Ratings:** Allows users to prioritize topics based on their difficulty or importance.

---

## 📥 How to Install
1. **Clone the Repository:**
   ```bash
   git clone <https://github.com/Dagi4g/Slifer-.git>
   cd slipher/App/Backend/Src
   ```


2. **Run the app:**
    ```bash
    python run.py
    ```

---

## 🤝 How You Can Contribute

### **We’d love your help! Here’s how you can contribute:**

1. Fork the repository and create a new branch for your changes.

2. Add your changes and test them thoroughly.

3. Submit a pull request with a detailed explanation of your work.


## Areas You Can Contribute To:

- **Notification System:** Implement a dynamic notification algorithm for spaced repetition.

- **User Interface:** Create an intuitive UI for easier data input and navigation.

- **Feature Expansion:** Introduce analytics, progress tracking, or export options for user data.
- 🖋 **Add your own idea:** *out of the box ideas are welcomed*


### Tech Stack
![Python](https://img.shields.io/badge/Python-FFD43B?style=flat-square&logo=python&logoColor=green)

## License

Slifer's license: [License](./Documentation/LICENSE)
