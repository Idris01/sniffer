# Documentation (Json Sniffer)
The Json Sniffer program is a python program that sniffs and captures the attributes within
the "message" key of a given ```.json``` file.

The captured JSON attributes are schemed out using the following procedures:

- All attributes are padded with "tag" and "description" keys,
- all properties are set "required":false,
- Keys with values "string", "integer", "boolean", "array of strings" and "array in JSON" mapped to "string", "integer" 
  "boolean", "enum" and "array" respectively
- keys with value of "empty array" defaults to "enum"


Inside the ```main.py``` the core schema sniffing is done by a *sniffer* 
function from the ```json_sniffer``` module inside the ```utility``` package.
```from utility.json_sniffer import sniffer```

## The information required to run the program is described as follow

### To make use of the program 
- clone the repo at 
```https://github.com/idris01/sniffer.git```
- switch into the "sniffer" directory
```cd sniffer```

### To run the program on a given "data_1.json"
- Note: use:
  - ```python ``` for windows 
  - ```python3``` or ```py``` for other OS if ```python``` did not work
- copy the full path of the file, for example inside the ```sniffer``` base
  directory, the full path of the "data_1.json" is ```./data/data_1.json```
- Run the Python command
 - ```python main.py "<full_path_to_file>"``` i.e ```python main.py "./data/data_1.json"``` for *data_1.json*
- When the command successfully runs, the output is found in ```./schema/*_schema.json```
  i.e for our sample *data_1.json* the output is located in ```./schema/data_1_schema.json```

### To run the unittest
```python -m unittest  tests.py```