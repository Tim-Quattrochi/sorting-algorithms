### Basic sorting algorithms 🧮

#### Table of Contents

- [Basic sorting algorithms](#basic-sorting-algorithms)
  - [Creating a virtual environment](#creating-a-virtual-environment)
  - [Activating the virtual environment](#activating-the-virtual-environment)
  - [Installing dependencies](#installing-dependencies)
  - [Generating requirements.txt](#generating-requirementstxt)
  - [Running the tests](#running-the-tests)

### Creating a virtual environment

---

I recommend using venv to run the code. To create a virtual environment, run the following command in the terminal:

for windows:

```bash
python -m venv venv
```

for macOS and Linux:

```bash
python3 -m venv venv
```

### Activating the virtual environment

---

To activate the virtual environment, run the following command in the terminal:

for windows:

```bash
venv\Scripts\activate
```

for macOS and Linux: 🖥️

```bash
source venv/bin/activate
```

### Installing dependencies

```bash
pip install -r requirements.txt
```

### Generating requirements.txt

---

_This is more of a reference for myself._

```bash
pip freeze > requirements.txt
```

### Running the tests 🧪

---

To run the tests, run the following command in the terminal:

```bash
pytest
```
