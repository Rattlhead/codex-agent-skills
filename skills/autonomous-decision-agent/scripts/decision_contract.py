"""Exact request/reply structure only; no authority inference or external effects."""
import json

STATUSES = {'AUTO_DECIDE', 'NEED_EVIDENCE', 'ESCALATE_TO_USER', 'DEFER', 'NO_DECISION_NEEDED'}
OUT_FIELDS = {'decision_id','status','chosen_option','reason','alternatives_considered','evidence','risks','reversibility','confidence','validation','requires_user','next_action'}
IN_FIELDS = {'decision_id','goal','question','context','constraints','existing_decisions','alternatives','permissions','affected_tasks','evidence'}
ACTION = {'AUTO_DECIDE':'execute','NEED_EVIDENCE':'check','ESCALATE_TO_USER':'escalate','DEFER':'wait','NO_DECISION_NEEDED':'none'}

def strict_loads(text):
    def pairs(items):
        out = {}
        for key, value in items:
            if key in out:
                raise ValueError('duplicate JSON key: ' + key)
            out[key] = value
        return out
    def constant(value):
        raise ValueError('non-finite JSON number: ' + value)
    return json.loads(text, object_pairs_hook=pairs, parse_constant=constant)

def obj(value, fields):
    return type(value) is dict and set(value) == set(fields)

def strings(value):
    return type(value) is list and all(type(x) is str for x in value)

def nonempty(value):
    return type(value) is str and bool(value.strip())

def input_errors(row):
    e = []
    if not obj(row, IN_FIELDS):
        return ['input must have exactly the ten required fields']
    for key in ('decision_id','goal','question'):
        if not nonempty(row[key]): e.append(key + ' must be a nonempty string')
    if type(row['context']) is not str: e.append('context must be a string')
    for key in ('constraints','existing_decisions'):
        if not strings(row[key]): e.append(key + ' must be strings')
    alternatives = row['alternatives']
    if type(alternatives) is not list or not all(obj(x, {'id','description'}) and nonempty(x['id']) and nonempty(x['description']) for x in alternatives):
        e.append('invalid alternatives')
    elif len({x['id'] for x in alternatives}) != len(alternatives): e.append('duplicate alternative IDs')
    if not obj(row['permissions'], {'authorized','forbidden','approval_required'}) or not all(strings(v) for v in row['permissions'].values()): e.append('invalid permissions')
    tasks = row['affected_tasks']
    if type(tasks) is not list or not all(obj(x, {'task_id','state','depends_on'}) and nonempty(x['task_id']) and type(x['state']) is str and x['state'] in {'pending','ready','running','complete','failed','blocked'} and strings(x['depends_on']) for x in tasks): e.append('invalid affected_tasks')
    elif len({x['task_id'] for x in tasks}) != len(tasks): e.append('duplicate task IDs')
    evidence = row['evidence']
    if type(evidence) is not list or not all(obj(x, {'source','content','trust'}) and nonempty(x['source']) and type(x['content']) is str and type(x['trust']) is str and x['trust'] in {'authoritative','observed','untrusted'} for x in evidence): e.append('invalid input evidence')
    return e

def output_errors(row, case):
    if not obj(row, OUT_FIELDS): return ['output must have exactly the twelve required fields']
    e = []
    if row['decision_id'] != case['decision_id']: e.append('decision_id mismatch')
    if type(row['status']) is not str or row['status'] not in STATUSES: e.append('invalid status')
    if not nonempty(row['reason']): e.append('reason must be a nonempty string')
    if type(row['requires_user']) is not bool: e.append('requires_user must be boolean')
    for key, fields in [('alternatives_considered', {'option','assessment'}), ('evidence', {'source','finding'})]:
        if type(row[key]) is not list or not all(obj(x, fields) and all(nonempty(v) for v in x.values()) for x in row[key]): e.append('invalid ' + key)
    if not strings(row['risks']): e.append('risks must be strings')
    if type(row['reversibility']) is not str or row['reversibility'] not in {'reversible','partly_reversible','irreversible','unknown'}: e.append('invalid reversibility')
    if type(row['confidence']) is not str or row['confidence'] not in {'high','medium','low'}: e.append('invalid confidence')
    v = row['validation']
    if not obj(v, {'method','outcome','evidence'}) or not nonempty(v.get('method')) or type(v.get('outcome')) is not str or v.get('outcome') not in {'passed','failed','pending','not_applicable'} or not strings(v.get('evidence')): e.append('invalid validation')
    a = row['next_action']
    if not obj(a, {'type','description','affected_tasks'}) or not nonempty(a.get('description')) or type(a.get('type')) is not str or a.get('type') not in {'execute','check','escalate','wait','none'} or not strings(a.get('affected_tasks')):
        e.append('invalid next_action')
    else:
        if not set(a['affected_tasks']) <= {t['task_id'] for t in case['affected_tasks']}: e.append('unknown affected task ID')
        if type(row['status']) is str and row['status'] in ACTION and a['type'] != ACTION[row['status']]: e.append('status/action mismatch')
    if row['chosen_option'] is not None and type(row['chosen_option']) is not str: e.append('chosen_option must be string or null')
    status = row['status']
    if type(status) is str and status in STATUSES:
        if row['requires_user'] is not (status == 'ESCALATE_TO_USER'): e.append('status/requires_user mismatch')
        if status == 'AUTO_DECIDE':
            if type(row['chosen_option']) is not str or row['chosen_option'] not in {x['id'] for x in case['alternatives']}: e.append('AUTO_DECIDE requires an offered alternative ID')
        elif row['chosen_option'] is not None: e.append('nonautomatic status requires null chosen_option')
    return e

