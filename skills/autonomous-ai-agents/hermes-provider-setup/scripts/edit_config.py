#!/usr/bin/env python3
"""Safe yaml read/modify/write for Hermes config.yaml list edits.

`hermes config set` cannot append to lists (IndexError on missing indices) and
the fallback CLI accepts no args. Use this script for:
  - custom_providers entries
  - fallback_providers chain edits
  - removing empty-string entries left behind by config set

Usage: edit the ACTIONS dict below, then run: python3 scripts/edit_config.py
"""
import yaml
import sys

PATH = '/root/.hermes/config.yaml'

ACTIONS = {
    # Example: append a custom provider with its own key_env
    # 'add_provider': {
    #     'list': 'custom_providers',
    #     'entry': {
    #         'name': 'Sumopod-DeepSeek',
    #         'base_url': 'https://ai.sumopod.com/v1',
    #         'key_env': 'SUMOPOD_DEEPSEEK_V4_API_KEY',
    #         'model': 'deepseek-v4-flash',
    #         'models': ['deepseek-v4-flash'],
    #     },
    # },
    # Example: replace the whole fallback chain (order = priority)
    # 'set_fallback_chain': {
    #     'list': 'fallback_providers',
    #     'replace_with': [
    #         {'provider': 'custom', 'model': 'llama-3.3-70b-versatile', 'base_url': 'https://api.groq.com/openai/v1'},
    #         {'provider': 'gemini', 'model': 'gemini-3.6-flash', 'base_url': 'https://generativelanguage.googleapis.com/v1beta'},
    #     ],
    # },
    # Example: drop entries with empty provider (cleanup after config set '')
    # 'cleanup_empty': {'list': 'fallback_providers', 'drop_empty_field': 'provider'},
}

def main():
    with open(PATH) as f:
        cfg = yaml.safe_load(f)
    for name, act in ACTIONS.items():
        lst = cfg.setdefault(act['list'], [])
        if 'entry' in act:
            if not any(e.get('name') == act['entry'].get('name') for e in lst if isinstance(e, dict)):
                lst.append(act['entry'])
        if 'replace_with' in act:
            cfg[act['list']] = act['replace_with']
        if 'drop_empty_field' in act:
            field = act['drop_empty_field']
            cfg[act['list']] = [e for e in lst if e.get(field)]
    with open(PATH, 'w') as f:
        yaml.safe_dump(cfg, f, sort_keys=False, allow_unicode=True)
    print('config.yaml updated:')
    for k in ACTIONS:
        print(f'  - {k}')
        for e in cfg.get(k, []):
            if isinstance(e, dict):
                print(f'      {e.get("name", e.get("provider"))}: {e.get("model", "")}')

if __name__ == '__main__':
    main()
