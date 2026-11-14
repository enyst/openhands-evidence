#!/usr/bin/env python3
"""Print `usage_id: prompt_tokens/completion_tokens` per source.

usage: summ.py LABEL --ws CAPTURE.jsonl | --rest (JSON on stdin) | --disk BASE_STATE
"""
import json, sys

def fmt(stats):
    if not stats:
        return "(none)"
    m = stats.get("usage_to_metrics", {})
    return " ".join(
        f"{k}={(v.get('accumulated_token_usage') or {}).get('prompt_tokens')}/"
        f"{(v.get('accumulated_token_usage') or {}).get('completion_tokens')}"
        for k, v in sorted(m.items())
    ) or "(empty)"

label, mode = sys.argv[1], sys.argv[2]
if mode == "--ws":
    frames = [json.loads(l) for l in open(sys.argv[3])]
    stats = [f["frame"]["value"] for f in frames
             if f.get("direction") == "received" and f["frame"].get("key") == "stats"]
    full = [f["frame"]["value"].get("stats") for f in frames
            if f.get("direction") == "received" and f["frame"].get("key") == "full_state"]
    print(f"{label:34s} socket full_state on connect: {fmt(full[0]) if full else '(none)'}")
    print(f"{label:34s} socket stats events: {len(stats)}"
          + (f"; last: {fmt(stats[-1])}" if stats else ""))
elif mode == "--rest":
    print(f"{label:34s} REST GET stats:    {fmt(json.load(sys.stdin).get('stats'))}")
else:
    print(f"{label:34s} base_state.json:   {fmt(json.load(open(sys.argv[3])).get('stats'))}")
