def apply_theme(widget,dark_mode=True):
    """Apply the dark or light theme to the given widget"""
    if dark_mode:
        bg_color="#2E2E2E"
        fg_color="#FFFFFFF"
        entry_bg="#3C3F41"
    else :
        bg_color="#FFFFFF"
        fg_color="#000000"
        entry_bg="F0F0F0F"
    try:
        widget.configure(bg=bg_color)
    except:
        pass
    for child in widget.winfo_children():
        try:
            child.configure(bg=bg_color,fg=fg_color)
        except:
            pass
        if child.winfo_class=="Entry":
            child.configure(bg=entry_bg,fg=fg_color)
        elif child.winfo_class=="TFrame":
            apply_theme(child,dark_mode)
        elif child.winfo_children():
            apply_theme(child,dark_mode)
