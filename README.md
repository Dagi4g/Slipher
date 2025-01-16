<div align="center">
# Slipher – Personalized Learning tracker
**before moving on:** we want to **thank you** for checking slifer repository

**Slipher** is a learning tracker designed to help students(**high school**) do better in there exams.

It uses a spaced reptation technique with personalized notification system to help students retain information better and stay engaged with their studies.

---

## 📖 Table of Contents
- [purpse](#-why-slipher)
- [Code Overview](#-code-overview)
- [Progress So Far](#-progress-so-far)
- [Core Focus](#-core-focus)
- [How to Install](#-how-to-install)
- [How You Can Contribute](#-how-you-can-contribute)
- [License](#-license)
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

---

## 🎯 Core Focus
Slipher currently focuses on **fundamental features** to ensure the app is stable and effective before expanding into more advanced functionalities.

---

## 📥 How to Install
1. **Clone the Repository:**
   ```bash
   git clone <https://github.com/Dagi4g/Slifer-.git>
   cd slipher

2. **Run the app:**
    ```bash
    python slifer.py
