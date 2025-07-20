import json

try:
    with open("customer_data.json", "r", encoding="utf-8") as f:
        content = f.read()
        print("RAW FILE CONTENT:\n", repr(content))  # Shows hidden characters

        if not content.strip():
            print("Error: File is empty.")
        else:
            data = json.loads(content)
            print("\n✅ JSON PARSED SUCCESSFULLY:")
            print(json.dumps(data, indent=4))
except json.JSONDecodeError as e:
    print("\n❌ JSON Decode Error:", e)
except FileNotFoundError:
    print("\n❌ File not found.")
except Exception as e:
    print("\n❌ Unexpected error:", e)
