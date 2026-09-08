"""Validate observed delivery order, not receipt meaning or host authorization.

Surface, collapse state and semantic segment roles must come from a verified
adapter/UI observation and review. Model self-reports are not observations.
"""
CONTRACT_RESOURCES = frozenset({'SKILL.md', 'PROTOCOL.md', 'release.json'})


def evaluate(events, direct_answer=False):
    if direct_answer:
        # This presentation exception says nothing about action authorization.
        return set()
    errors = set()
    seen = False
    final_receipt = False
    for event in events:
        if event.get('type') == 'tool':
            bootstrap = (event.get('purpose') == 'load_contract' and
                         event.get('resource') in CONTRACT_RESOURCES)
            if not seen and not bootstrap:
                errors.add('TASK_BEFORE_RECEIPT')
            continue
        if event.get('type') != 'message':
            errors.add('UNVERIFIED_SURFACE')
            continue
        surface = event.get('surface')
        if surface not in {'conversation', 'thinking', 'status', 'tool_log'} or not isinstance(event.get('collapsed'), bool):
            errors.add('UNVERIFIED_SURFACE')
        visible = surface == 'conversation' and event.get('collapsed') is False
        local_receipt = False
        for segment in event.get('segments', []):
            role = segment.get('role')
            text = segment.get('text', '')
            valid = isinstance(text, str) and bool(text.strip())
            if role == 'receipt' and visible and valid:
                seen = True
                local_receipt = True
                if event.get('final') is True:
                    final_receipt = True
            elif visible and valid:
                if not seen:
                    errors.add('PREFIX_NOT_RECEIPT')
                if role == 'answer' and (not seen or (event.get('final') is True and not local_receipt)):
                    errors.add('ANSWER_BEFORE_RECEIPT')
    if not seen:
        errors.add('NO_VISIBLE_RECEIPT')
    if not final_receipt:
        errors.add('FINAL_RECEIPT_MISSING')
    return errors
