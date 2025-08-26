import os
from notion_client import Client
from dotenv import load_dotenv
import random
import yaml

semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]


def main():
    # Connecting to Notion
    notion = Client(auth=os.environ["NOTION_TOKEN"])

    # Querying cenas
    query_cena = notion.databases.query(
        database_id="25b301d42b9a8065901bcf9ae8e09950",
        filter={
            "and": [
                {
                    "property": "Tipo Comida",
                    "multi_select": {
                        "contains": "Cena"
                    }
                },
                {
                    "property": "Tipo de Plato",
                    "select": {
                        "equals": "Completo"
                    }
                }
            ]
        }
    )
    cenas_db = query_cena["results"]

    # Almuerzos
    query_almuerzo = notion.databases.query(
        database_id="25b301d42b9a8065901bcf9ae8e09950",
        filter={
            "and": [
                {
                    "property": "Tipo Comida",
                    "multi_select": {
                        "contains": "Almuerzo"
                    }
                },
                {
                    "property": "Tipo de Plato",
                    "select": {
                        "equals": "Completo"
                    }
                }
            ]
        }
    )
    almuerzos_db = query_almuerzo["results"]


    # Random per week
    cenas = random.sample(cenas_db, k=len(semana))
    almuerzos = random.sample(almuerzos_db, k=len(semana))

    # Populating output
    comida_semanal = {}
    for dia, cena, almuerzo in zip(semana, cenas, almuerzos):

        plato_cena = cena['properties']['Name']['title'][0]['plain_text']
        plato_almuerzo = almuerzo['properties']['Name']['title'][0]['plain_text']

        plan_diario = {"Almuerzo": plato_almuerzo, "Cena": plato_cena}
        comida_semanal[dia] = plan_diario

    yaml_output = yaml.dump(comida_semanal, indent=4, allow_unicode=True, sort_keys=False)
    print(yaml_output)



if __name__ == "__main__":
    load_dotenv()
    main()