# 🍽️ Meal Planner

An automated weekly meal planning tool that integrates with Notion to generate random meal plans and shopping lists.

## 📋 Project Objective

This tool automatically creates weekly meal plans by:

- 🎲 **Randomly selecting** lunch and dinner meals from your Notion database
- 📅 **Generating weekly menus** for all 7 days of the week
- 🛒 **Creating shopping lists** with all required ingredients
- 📝 **Publishing to Notion** as formatted weekly meal plan pages
- 🇪🇸 **Spanish language support** with days of the week in Spanish

## 🏗️ Project Structure

```
meal-planner/
├── main.py              # Main application logic
├── pyproject.toml       # Project dependencies and configuration
├── Taskfile.yml         # Task automation (install, format, run)
├── .env.example         # Environment variables template
├── .python-version      # Python version specification (3.11)
└── README.md           # This file
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

## 📦 Dependencies

### Production
- `notion-client`: Notion API integration
- `python-dotenv`: Environment variable management
- `pyyaml`: YAML output formatting

### Development
- `black`: Code formatting
- `isort`: Import sorting

## 🤝 Contributing

1. **Format your code**: Run `task format` before committing
2. **Test your changes**: Run `task run` to ensure functionality
3. **Follow conventions**: Use Spanish for day names, maintain YAML structure

## 📝 Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `NOTION_TOKEN` | Your Notion integration token | Yes |

## 🔍 Troubleshooting

### Common Issues

1. **Missing Notion Token**: Ensure `.env` file exists with valid `NOTION_TOKEN`
2. **Database Not Found**: Verify database ID and integration permissions
3. **No Recipes Found**: Check database filters and recipe properties
4. **Permission Errors**: Ensure Notion integration has access to your database and parent page

### Getting Help

- Check Notion API documentation for database setup
- Verify your integration has the correct permissions
- Ensure your database structure matches the expected properties

## 📄 License

This project is for personal use. Please respect Notion's API terms of service.

---

*Generated weekly meal plans to make your life easier! 🍽️*
