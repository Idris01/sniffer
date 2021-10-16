import sys
from pathlib import Path
import json
from utility.json_sniffer import sniffer


def sniff_schema(path, output="./schema"):
    # open the given file for reading
    # the default output file parent is "./schema"
    with open(path, "r") as file:

        content = file.read()
        content = json.loads(content)

        # convert the content to sniffed data
        # Note: the return type is dict, a datatype that is
        # easily used to represent json
        sniffed_data = sniffer(content)

        # create a schema file name from the input file name
        output_file = output + \
            f"/{path.split('.')[-2].split('/')[-1]}_schema.json"

        # open the file in write "w" mode
        # Note: this overwrites existing file
        with open(output_file, "w") as writer:
            writer.write(json.dumps(sniffed_data, indent=2, sort_keys=False))
            print(f"\n\nSchema file successfully written to {output_file}")


if __name__ == "__main__":
    try:
        # read the path to the json file supplied from the terminal
        # throws an IndexError if no argument is supplied
        path = sys.argv[1]

        # checks if the provided path actually exists
        # throws Assertion Error
        assert(Path(path).exists()), f"{path} does not exist"

        # checks if the given file is a json file
        # throws Assertion Error
        assert(Path(path).name.endswith('.json')
               ), "Only '.json' file extension expected"

        sniff_schema(path)

    except IndexError:
        print("please supply a path to the json file")

    except AssertionError as msg:
        print(msg)
