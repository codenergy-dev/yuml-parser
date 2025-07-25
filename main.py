import json
from yuml_parser.parse_yuml import parse_yuml

if __name__ == "__main__":
  import sys
  if len(sys.argv) != 2:
    print("Usage: python main.py <pipelines.yuml>")
    sys.exit(1)

  yuml_path = sys.argv[1]
  pipelines = parse_yuml(yuml_path)
  pipelines_json = [pipeline.__dict__ for pipeline in pipelines]

  print(json.dumps(pipelines_json, indent=2, ensure_ascii=False))