"""Used to demonstrate the functionality of the chef_interface.py module"""
from chef_interface.chef_interface import ChefAPI
import json
from tools.tools import Tools


def main():
    """Demonstrates different methods available within the Chef Interface"""
    chef = ChefAPI()
    chef.auth()
    tool_bag = Tools()

    index = 'node'
    query = 'name:node'
    header = {}

    nodes = tool_bag.csv_pull_key('data/example_nodes.csv', 0)

    response = json.loads(chef.chef_search())
    response = json.loads(chef.chef_search(index=index))
    response = json.loads(chef.chef_search(index=index, query=query))
    response = json.loads(chef.chef_search(index=index, query=query, header=header))

    response = chef.chef_get('/nodes/tst2asvcnow')
    response = json.loads(chef.chef_get('/nodes/', 'tst2asvcnow'))
    print(response['chef_environment'])


    with open('chef_search.json', 'w') as file:
        json.dump(response, file, indent=4)


if __name__ == "__main__":
    main()
