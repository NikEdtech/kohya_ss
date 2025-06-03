def msgbox(msg, *args, **kwargs):
    print(f"[INFO] {msg}")

def ynbox(msg, *args, **kwargs):
    print(f"[YNBOX] {msg} (auto-yes)")
    return True

def boolbox(msg, *args, **kwargs):
    print(f"[BOOLBOX] {msg} (auto-yes)")
    return True
