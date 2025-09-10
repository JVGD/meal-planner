# 🍽️ Meal Planner

An automated weekly meal planning tool that integrates with Notion to get your meal database and generate a random meal plan and its shopping list for the week.

<img width="1322" height="578" alt="image" src="https://github.com/user-attachments/assets/9f0bc6b9-a3fb-4a37-a79d-5e19c61ffbc3" />


## 📋 Project Objective

This tool automatically creates weekly meal plans by:

- 🎲 **Randomly selecting** lunch and dinner meals from your Notion database
- 📅 **Generating weekly menus** for all 7 days of the week
- 🛒 **Creating shopping lists** with all required ingredients
- 📝 **Publishing to Notion** as formatted weekly meal plan pages

## 🏗️ Project Structure

```
meal-planner/
├── main.py              # Main application logic
├── pyproject.toml       # Project dependencies and configuration
├── Taskfile.yml         # Task automation (install, format, run)
├── .env.example         # Environment variables template
├── .python-version      # Python version specification (3.11)
└── README.md            # This file
```

## 🛠️ Prerequisites

- **Python 3.11+**: Required for the application
- **uv**: Modern Python package manager ([installation guide](https://docs.astral.sh/uv/getting-started/installation/))
- **Task**: Task runner ([installation guide](https://taskfile.dev/installation/))
- **Notion Integration**: Access to a Notion workspace with recipe database

## 🚀 Setup

### 1. Clone and Navigate

```bash
git clone <repository-url>
cd meal-planner
```

### 2. Install Dependencies

```bash
# Using Task (recommended)
task install

# Or directly with uv
uv sync --all-groups
```

### 3. Configure Environment

```bash
# Copy the environment template
cp .env.example .env

# Edit .env and add your Notion token
# Get your token from: https://www.notion.so/my-integrations
```

### 4. Set up Notion Database

Your Notion database should have the following properties:

- **Name** (Title): Recipe name
- **Tipo Comida** (Multi-select): Contains "Almuerzo" and/or "Cena"
- **Tipo de Plato** (Select): Should include "Completo" option
- **Ingredientes** (Multi-select): List of ingredients needed

### 5. Update Database and Page IDs

Edit `main.py` and replace the hardcoded IDs with your own:

```python
# Replace with your database ID
database_id="your_database_id_here"

# Replace with your parent page ID
parent={"page_id": "your_parent_page_id_here"}
```

## 🎯 Usage

### Run the Meal Planner

```bash
# Using Task (recommended)
task run

# Or directly with uv
uv run python main.py
```

### Development Tasks

```bash
# Format code (black + isort)
task format

# Install dependencies
task install

# List all available tasks
task --list
```

## 📊 Output Example

The tool generates a weekly meal plan like this:

```yaml
Lunes:
  Almuerzo: Arroz con Pollo
  Cena: Ensalada César
Martes:
  Almuerzo: Pasta Bolognesa
  Cena: Sopa de Verduras
# ... rest of the week
Ingredientes:
  - Pollo
  - Arroz
  - Lechuga
  - Tomate
  # ... all unique ingredients
```

## 🔧 Configuration

### Python Environment

- **Version**: Python 3.11 (specified in `.python-version`)
- **Package Manager**: uv for fast dependency management
- **Virtual Environment**: Automatically managed by uv

### Code Formatting

- **Black**: 120 character line length
- **Isort**: Compatible with Black, imports sorted automatically
- **Configuration**: Defined in `pyproject.toml`

