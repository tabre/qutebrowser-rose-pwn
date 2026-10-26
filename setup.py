# vim:fileencoding=utf-8:foldmethod=marker

def setup(c, variant, samecolorrows=False):
    # Palette {{{
    palette = {}
    if variant == "rose-pine":
        palette = {
            "Base": "#1c1c1d",
            "Surface": "#262626",
            "Overlay": "#303030",
            "Muted": "#5f5f87",
            "Subtle": "#8787af",
            "Text": "#d7d7ff",
            "Love": "#ff5f87",
            "Gold": "#ffaf87",
            "Rose": "#ffafaf",
            "Pine": "#5f8787",
            "Foam": "#afd7d7",
            "Iris": "#d7afd7",
            "Leaf": "#95b1ac",
            "HighlightLow": "#21202e",
            "HighlightMed": "#403d52",
            "HighlightHigh": "#524f67",
        }
    elif variant == "rose-pine-moon":
        palette = {
            "Base": "#1c1c1d",
            "Surface": "#262626",
            "Overlay": "#303030",
            "Muted": "#5f5f87",
            "Subtle": "#8787af",
            "Text": "#e0def4",
            "Love": "#ff5f87",
            "Gold": "#ffaf87",
            "Rose": "#c57c7c",
            "Pine": "#5f87af",
            "Foam": "#afd7d7",
            "Iris": "#d7afd7",
            "Leaf": "#95b1ac",
            "HighlightLow": "#2a283e",
            "HighlightMed": "#44415a",
            "HighlightHigh": "#56526e",
        }
    elif variant == "rose-pine-dawn":
        palette = {
            "Base": "#faf4ed",
            "Surface": "#fffaf3",
            "Overlay": "#f2e9e1",
            "Muted": "#9893a5",
            "Subtle": "#797593",
            "Text": "#464261",
            "Love": "#b4637a",
            "Gold": "#ea9d34",
            "Rose": "#d7827e",
            "Pine": "#286983",
            "Foam": "#56949f",
            "Iris": "#907aa9",
            "Leaf": "#6d8f89",
            "HighlightLow": "#f4ede8",	
            "HighlightMed": "#dfdad9",	
            "HighlightHigh": "#cecacd",
        }
    else:
        palette = {
            "Base": "#1c1c1d",	
            "Surface": "#262626",	
            "Overlay": "#303030",	
            "Muted": "#5f5f87",	
            "Subtle": "#8787af",	
            "Text": "#d7d7ff",	
            "Love": "#ff5f87",	
            "Gold": "#ffaf87",	
            "Rose": "#ffafaf",	
            "Pine": "#5f8787",	
            "Foam": "#afd7d7",	
            "Iris": "#d7afd7",	
            "Leaf": "#95b1ac",	
            "HighlightLow": "#21202e",	
            "HighlightMed": "#403d52",	
            "HighlightHigh": "#524f67",
        }
    # }}}

    # Fonts {{{
    ## Font family used by every font group that does not specify its own family
    ## (statusbar, completion, tabs, hints, keyhints, webpages).
    c.fonts.default_family = "JetBrains Mono"
    # }}}

    # Completion {{{
    ## Background color of the completion widget category headers.
    c.colors.completion.category.bg = palette["Base"]
    ## Bottom border color of the completion widget category headers.
    c.colors.completion.category.border.bottom = palette["Surface"]
    ## Top border color of the completion widget category headers.
    c.colors.completion.category.border.top = palette["Overlay"]
    ## Foreground color of completion widget category headers.
    c.colors.completion.category.fg = palette["Muted"]
    ## Background color of the completion widget for even and odd rows.
    c.colors.completion.even.bg = palette["Base"]
    c.colors.completion.odd.bg = palette["Base"]
    ## Text color of the completion widget.
    c.colors.completion.fg = palette["Text"]

    ## Background color of the selected completion item.
    c.colors.completion.item.selected.bg = palette["Overlay"]
    ## Bottom border color of the selected completion item.
    c.colors.completion.item.selected.border.bottom = palette["Surface"]
    ## Top border color of the completion widget category headers.
    c.colors.completion.item.selected.border.top = palette["Surface"]
    ## Foreground color of the selected completion item.
    c.colors.completion.item.selected.fg = palette["Love"]
    ## Foreground color of the selected completion item.
    c.colors.completion.item.selected.match.fg = palette["Rose"]
    ## Foreground color of the matched text in the completion.
    c.colors.completion.match.fg = palette["Text"]

    ## Color of the scrollbar in completion view
    c.colors.completion.scrollbar.bg = palette["Overlay"]
    ## Color of the scrollbar handle in completion view.
    c.colors.completion.scrollbar.fg = palette["Surface"]
    # }}}

    # Statusbar {{{
    ## Background color of the statusbar in different modes.
    c.colors.statusbar.normal.bg = palette["Base"]
    c.colors.statusbar.insert.bg = palette["Base"]
    c.colors.statusbar.command.bg = palette["Base"]
    c.colors.statusbar.caret.bg = palette["Base"]
    c.colors.statusbar.caret.selection.bg = palette["Base"]
    c.colors.statusbar.passthrough.bg = palette["Surface"]
    c.colors.statusbar.private.bg = palette["Love"]

    ## Background color of the progress bar.
    c.colors.statusbar.progress.bg = palette["Foam"]

    ## Foreground color of the statusbar in different modes.
    c.colors.statusbar.normal.fg = palette["Rose"]
    c.colors.statusbar.insert.fg = palette["Pine"]
    c.colors.statusbar.command.fg = palette["Love"]
    c.colors.statusbar.passthrough.fg = palette["Subtle"]
    c.colors.statusbar.caret.fg = palette["Overlay"]
    c.colors.statusbar.caret.selection.fg = palette["Iris"]
    c.colors.statusbar.private.fg = palette["HighlightMed"]

    ## Foreground color of the URL in the statusbar on error.
    c.colors.statusbar.url.error.fg = palette["Gold"]

    ## Default foreground color of the URL in the statusbar.
    c.colors.statusbar.url.fg = palette["Text"]

    ## Foreground color of the URL in the statusbar for hovered links.
    c.colors.statusbar.url.hover.fg = palette["Gold"]

    ## Foreground color of the URL in the statusbar on successful load.
    c.colors.statusbar.url.success.http.fg = palette["Subtle"]

    ## Foreground color of the URL in the statusbar on successful load.
    c.colors.statusbar.url.success.https.fg = palette["Subtle"]

    ## Foreground color of the URL in the statusbar when there's a warning.
    c.colors.statusbar.url.warn.fg = palette["Gold"]

    ## rose-pine-moon overrides: Pine background with dark grey text.
    if variant == "rose-pine-moon":
        c.colors.statusbar.normal.bg = palette["Pine"]
        c.colors.statusbar.insert.bg = palette["Pine"]
        c.colors.statusbar.command.bg = palette["Pine"]
        c.colors.statusbar.caret.bg = palette["Pine"]
        c.colors.statusbar.caret.selection.bg = palette["Pine"]
        c.colors.statusbar.passthrough.bg = palette["Pine"]
        c.colors.statusbar.private.bg = palette["Pine"]

        c.colors.statusbar.normal.fg = palette["Base"]
        c.colors.statusbar.insert.fg = palette["Base"]
        c.colors.statusbar.command.fg = palette["Base"]
        c.colors.statusbar.caret.fg = palette["Base"]
        c.colors.statusbar.caret.selection.fg = palette["Base"]
        c.colors.statusbar.passthrough.fg = palette["Base"]
        c.colors.statusbar.private.fg = palette["Base"]

        ## URL text is dark on the Pine background; errors and warnings stay bright.
        c.colors.statusbar.url.fg = palette["Base"]
        c.colors.statusbar.url.success.http.fg = palette["Base"]
        c.colors.statusbar.url.success.https.fg = palette["Base"]
    # }}}

    # Tabs {{{
    # Background color of unselected tabs.
    c.colors.tabs.bar.bg = palette["Base"]
    c.colors.tabs.even.bg = palette["Base"]
    c.colors.tabs.odd.bg = palette["Base"]

    # Foreground color of unselected tabs.
    c.colors.tabs.even.fg = palette["Subtle"]
    c.colors.tabs.odd.fg = palette["Subtle"]

    # Background color of the selected tab.
    c.colors.tabs.selected.even.bg = palette["Overlay"]
    c.colors.tabs.selected.odd.bg = palette["Overlay"]

    # Foreground color of the selected tab.
    c.colors.tabs.selected.even.fg = palette["Text"]
    c.colors.tabs.selected.odd.fg = palette["Text"]

    # Color for the tab indicator.
    c.colors.tabs.indicator.error = palette["Gold"]
    c.colors.tabs.indicator.start = palette["Pine"]
    c.colors.tabs.indicator.stop = palette["Rose"]
    
    # Pinned tabs
    c.colors.tabs.pinned.even.fg = palette["Subtle"]
    c.colors.tabs.pinned.even.bg = palette["Base"]
    c.colors.tabs.pinned.odd.fg = palette["Subtle"]
    c.colors.tabs.pinned.odd.bg = palette["Base"]
    c.colors.tabs.pinned.selected.even.fg = palette["Text"]
    c.colors.tabs.pinned.selected.even.bg = palette["Overlay"]
    c.colors.tabs.pinned.selected.odd.fg = palette["Text"]
    c.colors.tabs.pinned.selected.odd.bg = palette["Overlay"]
    
    # }}}

    # Background color of webpages {{{
    c.colors.webpage.bg = palette["Base"]
    # }}}
    # Context menu {{{
    c.colors.contextmenu.menu.bg = palette["Surface"]
    c.colors.contextmenu.menu.fg = palette["Text"]

    c.colors.contextmenu.disabled.bg = palette["Muted"]
    c.colors.contextmenu.disabled.fg = palette["Text"]

    c.colors.contextmenu.selected.bg = palette["Rose"]
    c.colors.contextmenu.selected.fg = palette["Base"]
    # }}}

    # Keyhints {{{
    ## Background color of the keyhint widget.
    c.colors.keyhint.bg = palette["Surface"]

    ## Text color for the keyhint widget.
    c.colors.keyhint.fg = palette["Text"]

    ## Highlight color for keys to complete the current keychain.
    c.colors.keyhint.suffix.fg = palette["Rose"]

    ## Background color of follow hint
    c.colors.hints.bg = palette["Surface"]

    ## Text color for follow hint
    c.colors.hints.fg = palette["Text"]

    ## Highlight color for keys to complete the current keychain.
    c.colors.hints.match.fg = palette["Rose"]

    ## Border for follow hint
    c.hints.border = f"1px solid {palette['Overlay']}"



    # }}}

    # Downloads {{{
    c.colors.downloads.bar.bg = palette["Base"]
    c.colors.downloads.error.bg = palette["Base"]
    c.colors.downloads.start.bg = palette["Base"]
    c.colors.downloads.stop.bg = palette["Base"]

    c.colors.downloads.error.fg = palette["Gold"]
    c.colors.downloads.start.fg = palette["Pine"]
    c.colors.downloads.stop.fg = palette["Rose"]
    c.colors.downloads.system.fg = "none"
    c.colors.downloads.system.bg = "none"
    # }}}

    # Prompts {{{
    c.colors.prompts.bg = palette["Surface"]
    c.colors.prompts.border = palette["Subtle"]
    c.colors.prompts.fg = palette["Text"]
    c.colors.prompts.selected.bg = palette["Overlay"]
    c.colors.prompts.selected.fg = palette["Text"]

    # }}}

    # Error, info and warning messages {{{
    c.colors.messages.error.bg = palette["Surface"]
    c.colors.messages.error.border =palette["Surface"]
    c.colors.messages.error.fg = palette["Text"]

    c.colors.messages.info.bg = palette["Surface"]
    c.colors.messages.info.border = palette["Surface"]
    c.colors.messages.info.fg = palette["Gold"]

    c.colors.messages.warning.bg = palette["Surface"]
    c.colors.messages.warning.border = palette["Surface"]
    c.colors.messages.warning.fg = palette["Gold"]




    # }}}
