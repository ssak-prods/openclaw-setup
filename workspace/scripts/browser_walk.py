#!/usr/bin/env python3
import argparse, json, re, subprocess, time
from pathlib import Path

CONFIG = Path('/home/abbu-rpi5/.openclaw/openclaw.json')
PROFILE = 'private'
TIMEOUT_MS = '70000'


def token():
    return json.loads(CONFIG.read_text())['gateway']['auth']['token']


def run(*args, check=True, capture=True):
    cmd = ['openclaw', 'browser', '--token', token(), '--browser-profile', PROFILE, '--timeout', TIMEOUT_MS, *args]
    res = subprocess.run(cmd, text=True, capture_output=capture)
    if check and res.returncode != 0:
        raise RuntimeError((res.stderr or res.stdout).strip())
    return res.stdout.strip()


def parse_media_path(text: str):
    m = re.search(r'MEDIA:(.+)', text)
    return m.group(1).strip() if m else None


def ensure_started():
    run('start')


def restart_browser():
    run('stop', check=False)
    time.sleep(1.2)
    run('start')
    time.sleep(2.0)


def get_snapshot_json():
    raw = run('snapshot', '--interactive', '--json')
    return json.loads(raw)


def get_screenshot(full_page=False):
    args = ['screenshot']
    if full_page:
        args.append('--full-page')
    last_err = None
    for attempt in range(4):
        try:
            if attempt == 0:
                ensure_started()
                time.sleep(1.0)
            elif attempt == 2:
                restart_browser()
            else:
                time.sleep(2.0)
            return parse_media_path(run(*args))
        except Exception as e:
            last_err = e
            time.sleep(1.5)
    raise RuntimeError(str(last_err))


def open_url(url: str):
    return run('open', url)


def click_ref(ref: str):
    return run('click', ref)


def summarize(snapshot: dict):
    refs = snapshot.get('refs', {})
    items = []
    for ref, meta in refs.items():
        items.append({
            'ref': ref,
            'role': meta.get('role'),
            'name': meta.get('name', ''),
        })
    nav_like = [i for i in items if any(k in (i['name'] or '').lower() for k in ['pricing', 'about', 'feature', 'dashboard', 'login', 'sign in', 'docs', 'blog'])]
    return {
        'url': snapshot.get('url'),
        'interactive_count': len(items),
        'items': items,
        'nav_like': nav_like,
        'snapshot_text': snapshot.get('snapshot', ''),
    }


def main():
    ap = argparse.ArgumentParser(description='OpenClaw browser walkthrough helper')
    ap.add_argument('url', nargs='?')
    ap.add_argument('--click-ref')
    ap.add_argument('--wait-ms', type=int, default=1200)
    ap.add_argument('--full-page', action='store_true')
    args = ap.parse_args()

    ensure_started()
    opened = None
    if args.url:
        opened = open_url(args.url)
        time.sleep(args.wait_ms / 1000)

    if args.click_ref:
        click_ref(args.click_ref)
        time.sleep(args.wait_ms / 1000)

    snap = get_snapshot_json()
    shot = None
    shot_error = None
    try:
        shot = get_screenshot(full_page=args.full_page)
    except Exception as e:
        shot_error = str(e)
    result = {
        'opened': opened,
        'summary': summarize(snap),
        'screenshot': shot,
        'screenshot_error': shot_error,
    }
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
