# Sublime Text Plugin: Paste with Replace

A simple Sublime Text plugin that prompts for 2 string values, then pastes
whatever's on the pasteboard with the first string replaced by the second.
It has some smarts: if the found text is in ALL CAPS / all lower / Title Case,
the replacement will be formatted the same way.

The default key bindings are Cmd+Alt+V (Mac) and Ctrl+Alt+V (Windows / Linux).

To test it out, copy this text:

> Foo FOO foo

Hit (Cmd|Ctrl)+Alt+V and enter _"foo"_ for the first string and _"bar"_ for the
second.

You should see this pasted into the editor:

> Bar BAR bar

## TODO

 1. Add a menu item.
 2. Handle camel/underscored/dashed/pascal case translation
    _(e.g., "fooBar" to "foo-bar")_.
 3. Increment numbers in subsequent pastes (so if you replace _1_ with _2_,
    the next call should replace _1_ with _3_, assuming the text to be pasted
    hasn't changed).
 4. Monetization strategy (what they used to call "Profit!").