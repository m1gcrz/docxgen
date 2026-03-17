from docxtpl import DocxTemplate
from jinja2 import Environment
import json, re

# Load both files
with open("LLMgen-3.json") as f:
    raw = json.dumps(json.load(f))

with open("valuesph.json") as f:
    values = json.load(f)

# Resolve {{placeholders}} in LLMgen-3.json using values.json
def resolve(text, vals):
    def replacer(match):
        key = match.group(1).strip()
        return str(vals.get(key, match.group(0)))
    return re.sub(r'\{\{(\w+)\}\}', replacer, text)

data = json.loads(resolve(raw, values))

# Render
env = Environment(trim_blocks=True, lstrip_blocks=True, autoescape=False)
doc = DocxTemplate("docxstyling - Copy-5.docx")
doc.render(data, jinja_env=env)
doc.save("res6ph.docx")
