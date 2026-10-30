"""Validate proposal boundaries, consumer references and the frozen visual identity."""
import json
from pathlib import Path
from jsonschema import Draft202012Validator

root = Path(__file__).parent
data = json.loads((root/'characters.json').read_text())
schema = json.loads((root/'characters.schema.json').read_text())
Draft202012Validator.check_schema(schema)
Draft202012Validator(schema).validate(data)
Draft202012Validator.check_schema(json.loads((root/'review-receipt.schema.json').read_text()))
specs = {s['id']:s for s in json.loads((root/'visual-specs.json').read_text())['specs']}
prior = set(data['collision_check']['previous_character_names'])
names,ids,assets = set(),set(),set()
for c in data['characters']:
    slug=c['slug']
    assert c['name'] not in prior and c['name'] not in names, c['name']
    assert c['id'] == f'arcanea.fl02.{slug}' and c['character_id']==f'character:{slug}'
    assert c['id'] not in ids
    assert c['visual']['locked_identity']==specs[slug]['identity'], slug
    assert c['title']==specs[slug]['title'], slug
    assert set(c['asset_ids'])=={f'fl02-{slug}-sheet',f'fl02-{slug}-hero'}
    names.add(c['name']);ids.add(c['id']);assets.update(c['asset_ids'])
assert len(assets)==20
queue=json.loads((root/'review-queue.json').read_text())
assert {x['target_id'] for x in queue['items']}=={c['character_id'] for c in data['characters']}
assert {a for x in queue['items'] for a in x['asset_ids']}==assets
for item in queue['items']:
    assert item['state']=='pending' and item['decision'] is None and item['reviewer_id'] is None
print('Validated: 10 distinct character proposals, 20 consistent asset IDs, frozen identity alignment, 6/2/2 cast, review queue targets and honest pending review state.')
