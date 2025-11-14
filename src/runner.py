thonpython
import json
import os
from datetime import datetime
from extractors.index_checker import check_url_index
from extractors.utils_parser import load_urls
from outputs.exporters import export_json, export_csv, export_excel

def main():
    input_file = os.path.join(os.path.dirname(__file__), "..", "data", "input_urls.sample.txt")
    output_json_path = os.path.join(os.path.dirname(__file__), "..", "data", "sample_output.json")
    output_csv_path = os.path.join(os.path.dirname(__file__), "..", "data", "sample_output.csv")
    output_excel_path = os.path.join(os.path.dirname(__file__), "..", "data", "sample_output.xlsx")

    urls = load_urls(input_file)
    results = []

    for url in urls:
        try:
            status = check_url_index(url)
            results.append({
                "url": url,
                "indexed": status["indexed"],
                "region": status["region"],
                "timestamp": datetime.utcnow().isoformat(),
                "responseDetails": status["details"]
            })
        except Exception as e:
            results.append({
                "url": url,
                "indexed": False,
                "region": None,
                "timestamp": datetime.utcnow().isoformat(),
                "responseDetails": f"Error: {str(e)}"
            })

    export_json(results, output_json_path)
    export_csv(results, output_csv_path)
    export_excel(results, output_excel_path)

    print("Processing complete. Outputs generated.")

if __name__ == "__main__":
    main()