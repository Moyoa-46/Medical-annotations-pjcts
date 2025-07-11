import json

def txt_to_label_studio_json(input_txt_path, output_json_path):
    # Read sentences from .txt file
    with open(input_txt_path, 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file if line.strip()]
    
    # Convert to Label Studio format
    labeled_data = [{"text": line} for line in lines]

    # Save to JSON file
    with open(output_json_path, 'w', encoding='utf-8') as outfile:
        json.dump(labeled_data, outfile, indent=2)
    
    print(f"✅ Converted {len(labeled_data)} sentences and saved to {output_json_path}")

# Example usage
txt_to_label_studio_json("Cardiovascular Diseases.txt", "medical_sentences.json")
