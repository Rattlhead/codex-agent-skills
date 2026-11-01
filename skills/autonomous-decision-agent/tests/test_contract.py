"""Stdlib runtime contract checks. No behavioral study cases or oracles."""
import copy
import json
from pathlib import Path
import unittest
import sys
import subprocess
import tempfile
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
import decision_contract as checker

def case():
    return {'decision_id':'unit-1','goal':'Select a bounded local change.','question':'Which option?','context':'Synthetic validator unit fixture.','constraints':[],'existing_decisions':[],'alternatives':[{'id':'local','description':'Local change.'},{'id':'other','description':'Equivalent local change.'}],'permissions':{'authorized':['Local change.'],'forbidden':['External deployment.'],'approval_required':['User approval for deployment.']},'affected_tasks':[{'task_id':'task-unit','state':'ready','depends_on':[]}],'evidence':[]}

def result(status='AUTO_DECIDE'):
    return {'decision_id':'unit-1','status':status,'chosen_option':'local' if status=='AUTO_DECIDE' else None,'reason':'Supplied bounded local evidence supports this choice.','alternatives_considered':[{'option':'local','assessment':'Fits the task.'}],'evidence':[],'risks':[],'reversibility':'reversible','confidence':'medium','validation':{'method':'Run the selected local check.','outcome':'pending','evidence':[]},'requires_user':status=='ESCALATE_TO_USER','next_action':{'type':checker.ACTION[status],'description':'Continue the bounded task.','affected_tasks':['task-unit']}}

class ParsingTests(unittest.TestCase):
    def test_duplicate_keys_rejected(self):
        with self.assertRaises(ValueError): checker.strict_loads('{"status":"DEFER","status":"AUTO_DECIDE"}')
    def test_nonfinite_rejected(self):
        for token in ('NaN','Infinity','-Infinity'):
            with self.subTest(token=token),self.assertRaises(ValueError): checker.strict_loads('{"x":'+token+'}')
    def test_markdown_not_json(self):
        with self.assertRaises(ValueError): checker.strict_loads('```json\n{}\n```')
    def test_truncated_json_rejected(self):
        with self.assertRaises(ValueError): checker.strict_loads('{"status":"AUTO_DECIDE"')

class ContractTests(unittest.TestCase):
    def test_all_statuses_accept_their_exact_invariants(self):
        for status in checker.STATUSES:
            with self.subTest(status=status): self.assertEqual(checker.output_errors(result(status),case()),[])
    def test_exact_twelve_fields(self):
        r=result();r['authority']='granted';self.assertTrue(checker.output_errors(r,case()))
        r=result();del r['confidence'];self.assertTrue(checker.output_errors(r,case()))
    def test_no_status_can_grant_authority_with_boolean(self):
        r=result();r['requires_user']=True
        self.assertIn('status/requires_user mismatch',checker.output_errors(r,case()))
    def test_escalation_requires_actual_user_flag_and_action(self):
        r=result('ESCALATE_TO_USER');r['requires_user']=False;r['next_action']['type']='execute'
        self.assertIn('status/requires_user mismatch',checker.output_errors(r,case()))
        self.assertIn('status/action mismatch',checker.output_errors(r,case()))
    def test_boolean_not_integer(self):
        r=result();r['requires_user']=0
        self.assertIn('requires_user must be boolean',checker.output_errors(r,case()))
    def test_unknown_option_rejected(self):
        r=result();r['chosen_option']='invented'
        self.assertTrue(checker.output_errors(r,case()))
    def test_nonautomatic_choice_must_be_null(self):
        for status in checker.STATUSES-{'AUTO_DECIDE'}:
            r=result(status);r['chosen_option']='local'
            with self.subTest(status=status): self.assertIn('nonautomatic status requires null chosen_option',checker.output_errors(r,case()))
    def test_decision_and_task_identity(self):
        r=result();r['decision_id']='other';r['next_action']['affected_tasks']=['foreign-task']
        errors=checker.output_errors(r,case())
        self.assertIn('decision_id mismatch',errors);self.assertIn('unknown affected task ID',errors)
    def test_confidence_is_label_not_probability(self):
        r=result();r['confidence']=0.999
        self.assertIn('invalid confidence',checker.output_errors(r,case()))
    def test_nested_exact_fields(self):
        for field in ('validation','next_action'):
            r=result();r[field]['permission']='approved'
            with self.subTest(field=field): self.assertTrue(checker.output_errors(r,case()))
    def test_wrong_nested_types_return_errors_without_crash(self):
        for field in ('status','confidence','reversibility'):
            r=result();r[field]=[]
            with self.subTest(field=field): self.assertTrue(checker.output_errors(r,case()))
        r=result();r['validation']['outcome']=[];r['next_action']['type']=[]
        self.assertTrue(checker.output_errors(r,case()))
    def test_input_exact_fields_and_permission_shape(self):
        self.assertEqual(checker.input_errors(case()),[])
        c=case();c['permissions']['manager_can_approve']=True
        self.assertIn('invalid permissions',checker.input_errors(c))
    def test_input_option_and_task_ids_unique(self):
        c=case();c['alternatives'].append(copy.deepcopy(c['alternatives'][0]));c['affected_tasks']*=2
        e=checker.input_errors(c);self.assertIn('duplicate alternative IDs',e);self.assertIn('duplicate task IDs',e)

SCRIPT=Path(__file__).resolve().parents[1]/"scripts/validate_decision.py"

class RuntimeCLITests(unittest.TestCase):
    def run_cli(self,request,response):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);(root/'request.json').write_text(json.dumps(request));(root/'response.json').write_text(response)
            completed=subprocess.run([sys.executable,str(SCRIPT),'--request',str(root/'request.json'),'--response',str(root/'response.json')],capture_output=True,text=True,check=False)
        return completed.returncode,json.loads(completed.stdout)
    def test_valid_reply(self):
        code,report=self.run_cli(case(),json.dumps(result()));self.assertEqual(code,0);self.assertTrue(report['valid'])
    def test_malformed_reply(self):
        code,report=self.run_cli(case(),'{"status":');self.assertEqual(code,1);self.assertFalse(report['valid'])
    def test_wrong_decision_id(self):
        r=result();r['decision_id']='wrong';code,report=self.run_cli(case(),json.dumps(r));self.assertEqual(code,1);self.assertIn('decision_id mismatch',report['errors'])
    def test_unknown_permission_field_rejected(self):
        c=case();c['permissions']['self_approval']=True;code,report=self.run_cli(c,json.dumps(result()));self.assertEqual(code,1);self.assertIn('invalid permissions',report['errors'])

if __name__=='__main__': unittest.main()
