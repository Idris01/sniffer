from unittest import TestCase
from utility.json_sniffer import sniffer


class SnifferTest(TestCase):
    def setUp(self) -> None:
        # source is setup to serve as testing data
        self.source = {"message": {"battle": {"id": "KLMNOPQR"}, "age": 30,
                                   "participantIds": ["ABCDEF", "ABCDEFGHI"],
                                   "publicFeeds": False,
                                   "name": "Idris", "acl": [], }}

    def tests_source_data_is_dict(self):
        # note: dict is json representation
        data_type = type(self.source)
        self.assertEqual(data_type, dict)

    def tests_sniffer_returns_dict(self):
        result = sniffer(self.source)
        self.assertEqual(type(result), dict)

    def tests_age_type_int(self):
        result = sniffer(self.source)
        age = result["age"]
        self.assertEqual(age["type"], "integer")

    def tests_participant_id_type_enum(self):
        result = sniffer(self.source)
        participant_id = result["participantIds"]
        self.assertEqual(participant_id["type"], "enum")

    def tests_battle_type_array(self):
        result = sniffer(self.source)
        battle = result["battle"]
        self.assertEqual(battle["type"], "array")

    def tests_publicFeeds_type_boolean(self):
        result = sniffer(self.source)
        public_feeds = result["publicFeeds"]
        self.assertEqual(public_feeds["type"], "boolean")

    def tests_name_type_string(self):
        result = sniffer(self.source)
        name = result["name"]
        self.assertEqual(name["type"], "string")

    def tests_empty_array_type_enum(self):
        result = sniffer(self.source)
        acl = result["acl"]   # Note that "acl" has an empty array, []
        self.assertEqual(acl["type"], "enum")
