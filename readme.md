# 📝 Task-Manager

A multi-interface Python Task Manager that allows you to manage your daily objectives seamlessly. This repository features a modern **Web-based GUI** built with Streamlit, a lightweight **Desktop GUI**, and a rapid **Command Line Interface (CLI)** application.  All three applications automatically read and write tasks to a shared local database, allowing you to access and modify your todos from anywhere.


## 🚀 Features

*   **Multi-Interface**: Switch between a web application, a desktop widget, or a classic terminal layout.
*   **Live Timestamp**: Tracks and displays the current date and time on launch.
*   **Add Tasks**: Quick input field to append new items safely.
*   **Edit Functionality**: Modify existing items inline, featuring a helpful **Cancel** button if you change your mind.
*   **Complete & Delete**: Click checkboxes (Web) or type indices (CLI) to safely drop completed tasks without list bugs.
*   **Persistent Storage**: Automatically reads and writes to a text file database.

---

## 🛠️ Project Structure

```text
├── web.py          # Modern Web App Interface (Streamlit)
├── gui.py          # Native Desktop Window App (FreeSimpleGUI)
├── main.py         # Terminal Interactive Tool (CLI)
├── custom.py       # Core module for storage reads & writes (get_todos / write_todos)
├── todos.txt       # Flat text file operating as local database
└── requirement.txt # Lists necessary external project packages
```

---

## 💻 Installation & Setup

Make sure you have Python 3 installed on your system.

1. **Clone the repository:**
   ```bash
   git clone https://github.com/aayush219/Task-Manager.git
   cd Task-Manager
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirement.txt
   ```

---

## 🎯 How to Run

### 1. The Desktop Application (GUI)
Powered by the free-forever, human-friendly [FreeSimpleGUI Library](https://github.com/spyoungtech/FreeSimpleGUI). Open your visual window tool instantly with:
```bash
python gui.py
```

### 2. The Interactive Web Hub
Powered by Streamlit. To host your application locally inside an interactive web dashboard:
```bash
streamlit run web.py
```

### 3. The Quick Console Application (CLI)
For quick, resource-light terminal task configuration:
```bash
python main.py
```
---

## 💡 How to Interact

### Desktop Interface (`gui.py`)
*   **Add**: Write a new objective in the text prompt box and tap **Add**.
*   **Edit**: Highlight an item in your task registry list, make alterations, and click **Edit**.
*   **Complete**: Select an active task item and click **Complete** to safely clear it.

### Web Interface (`web.py`)
*   **Add**: Write your task into the central input element and tap `Enter`.
*   **Edit**: Tap the `Edit` shortcut button next to any item, input the replacement string, and press `Enter`. Tap `Cancel` to drop modifications safely.
*   **Complete**: Tick the checklist box next to any chore to wipe it out.

### Command Line (`main.py`)
*   `add [task item]` — Appends a new item to your file database.
*   `show` — Organizes and displays active chores with numeric indices.
*   `edit [index]` — Modifies an entry based on its given list position.
*   `complete [index]` — Resolves and safely drops a task from your system.
*   `exit` — Shuts down the terminal framework safely.

---

### 🛠️ Built With

*   [Python](https://python.org) - Core logic engine
*   [Streamlit](https://streamlit.io) - Fast web application framework
