import json

sample_data2 = """
{
  "nodeIdStr": "sip-cube-lab",
  "subscriptionIdStr": "102",
  "encodingPath": "Cisco-IOS-XE-interfaces-oper:interfaces/interface/statistics",
  "collectionId": "2",
  "collectionStartTime": "1632732373927",
  "msgTimestamp": "1632732373927",
  "dataGpbkv": [
    {
      "timestamp": "1632732373927",
      "fields": [
        {
          "name": "keys",
          "fields": [
            {
              "name": "name",
              "stringValue": "GigabitEthernet1"
            }
          ]
        },
        {
          "name": "content",
          "fields": [
            {
              "name": "discontinuity-time",
              "stringValue": "2021-09-10T10:25:47+00:00"
            },
            {
              "name": "in-octets",
              "uint64Value": "25226083"
            },
            {
              "name": "in-unicast-pkts",
              "uint64Value": "324486"
            },
            {
              "name": "in-broadcast-pkts",
              "uint64Value": "0"
            },
            {
              "name": "in-multicast-pkts",
              "uint64Value": "0"
            },
            {
              "name": "in-discards",
              "uint32Value": 0
            },
            {
              "name": "in-errors",
              "uint32Value": 0
            },
            {
              "name": "in-unknown-protos",
              "uint32Value": 0
            },
            {
              "name": "out-octets",
              "uint32Value": 25151469
            },
            {
              "name": "out-unicast-pkts",
              "uint64Value": "324497"
            },
            {
              "name": "out-broadcast-pkts",
              "uint64Value": "0"
            },
            {
              "name": "out-multicast-pkts",
              "uint64Value": "0"
            },
            {
              "name": "out-discards",
              "uint64Value": "0"
            },
            {
              "name": "out-errors",
              "uint64Value": "0"
            },
            {
              "name": "rx-pps",
              "uint64Value": "0"
            },
            {
              "name": "rx-kbps",
              "uint64Value": "0"
            },
            {
              "name": "tx-pps",
              "uint64Value": "0"
            },
            {
              "name": "tx-kbps",
              "uint64Value": "0"
            },
            {
              "name": "num-flaps",
              "uint64Value": "0"
            },
            {
              "name": "in-crc-errors",
              "uint64Value": "0"
            },
            {
              "name": "in-discards-64",
              "uint64Value": "0"
            },
            {
              "name": "in-errors-64",
              "uint64Value": "0"
            },
            {
              "name": "in-unknown-protos-64",
              "uint64Value": "0"
            },
            {
              "name": "out-octets-64",
              "uint64Value": "25151469"
            }
          ]
        }
      ]
    }
  ]
}


"""

sample_data = """
{
  "nodeIdStr": "sip-cube-lab",
  "subscriptionIdStr": "101",
  "encodingPath": "Cisco-IOS-XE-process-cpu-oper:cpu-usage/cpu-utilization",
  "collectionId": "1",
  "collectionStartTime": "1632730563338",
  "msgTimestamp": "1632730563338",
  "dataGpbkv": [
    {
      "timestamp": "1632730563338",
      "fields": [
        {
          "name": "keys"
        },
        {
          "name": "content",
          "fields": [
            {
              "name": "five-seconds",
              "uint32Value": 1
            },
            {
              "name": "cpu-usage-processes"
            }
          ]
        }
      ]
    }
  ]
}

"""


json_data = json.loads(sample_data2)


def get_field_value(inner_field):
    value = ""
    values = list(inner_field.values())
    if len(values) > 1:
        value = list(inner_field.values())[1]
    return value


new_json = {}


def get_all_fields_for_name(get_field_value, new_json, field, name):
    if field["name"] == name:
        for inner_field in field["fields"]:
            value = get_field_value(inner_field)
            if value != "":
                new_json[inner_field["name"]] = value


for field in json_data["dataGpbkv"][0]["fields"]:
    print(f"Keys, {field.keys()}")
    get_all_fields_for_name(get_field_value, new_json, field, "keys")
    get_all_fields_for_name(get_field_value, new_json, field, "content")


new_list = list(json_data.keys())[:6]

for item in new_list:
    new_json[item] = json_data[item]


print(f"New_json: {json.dumps(new_json, indent=4)}")
