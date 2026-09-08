"""Authored event traces; positions/roles are adapter or reviewer annotations."""
import unittest
from delivery_trace import evaluate

def message(role='receipt', surface='conversation', collapsed=False, final=False):
    return {'type':'message','surface':surface,'collapsed':collapsed,'final':final,
            'segments':[{'role':role,'text':'回讲：你要比较两份材料中的遗漏与未决事项。' if role=='receipt' else '开始核对材料。'}]}
TASK={'type':'tool','purpose':'task','resource':'source.md'}
BOOT={'type':'tool','purpose':'load_contract','resource':'SKILL.md'}

class DeliveryTests(unittest.TestCase):
    def check(self,events,direct=False):return evaluate(events,direct_answer=direct)
    def test_visible_before_tool_and_final(self):
        self.assertEqual(self.check([message(),TASK,message(final=True)]),set())
    def test_hidden_reasoning_is_not_receipt(self):
        self.assertIn('NO_VISIBLE_RECEIPT',self.check([message(surface='thinking'),TASK,message('answer',final=True)]))
    def test_collapsed_progress_is_not_receipt(self):
        self.assertIn('NO_VISIBLE_RECEIPT',self.check([message(collapsed=True),TASK,message('answer',final=True)]))
    def test_action_notice_is_not_receipt(self):
        self.assertIn('NO_VISIBLE_RECEIPT',self.check([message('action_notice'),TASK,message('answer',final=True)]))
    def test_final_receipt_cannot_repair_early_tool(self):
        self.assertIn('TASK_BEFORE_RECEIPT',self.check([TASK,message(final=True)]))
    def test_status_channel_does_not_count(self):
        self.assertIn('TASK_BEFORE_RECEIPT',self.check([message(surface='status'),TASK,message(final=True)]))
    def test_final_must_retain_receipt(self):
        self.assertIn('FINAL_RECEIPT_MISSING',self.check([message(),TASK,message('answer',final=True)]))
    def test_bootstrap_only_loads_contract(self):
        self.assertEqual(self.check([BOOT,message(),TASK,message(final=True)]),set())
    def test_bootstrap_cannot_disguise_task_read(self):
        self.assertIn('TASK_BEFORE_RECEIPT',self.check([dict(BOOT,resource='source.md'),message(final=True)]))
    def test_receipt_before_answer_in_same_message(self):
        e=message(final=True);e['segments'].insert(0,{'role':'answer','text':'结论：可以。'})
        self.assertIn('ANSWER_BEFORE_RECEIPT',self.check([e]))
    def test_explicit_direct_answer_exception(self):
        self.assertEqual(self.check([message('answer',final=True)],direct=True),set())
    def test_unknown_surface_is_unverified(self):
        self.assertIn('UNVERIFIED_SURFACE',self.check([message(surface='unknown',final=True)]))
    def test_empty_receipt_is_not_receipt(self):
        e=message(final=True);e['segments'][0]['text']=' '
        self.assertIn('NO_VISIBLE_RECEIPT',self.check([e]))

if __name__=='__main__':unittest.main()
