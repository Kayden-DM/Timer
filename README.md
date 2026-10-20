Timer
A GUI countdown timer built with CustomTkinter, with buttons to add or subtract time and start, pause, or reset.

Concepts Used
CustomTkinter Widgets — labels and buttons laid out in CTkFrame rows.

root.after() — schedules tick() every 1000ms for the countdown without freezing the UI.

Global State Flags — running and time_left control start/pause/reset behaviour across functions.

Features
Flexible Time Adjustment — eight add and eight subtract buttons ranging from 1 second to 1 hour.

Start / Pause / Resume — the pause button toggles between pausing and resuming the countdown.

Smart Formatting — displays MM:SS, switching to HH:MM:SS once an hour is reached.

Improvements
Remove Duplicate Time Buttons — the 16 buttons are near-identical lines; build them from a list of (label, seconds) tuples in a loop.

Pause Accuracy — pausing stops the scheduled tick(), so the remaining fraction of a second is lost; track elapsed real time with time.time() for accuracy.

Reset Clears to Zero — reset wipes the timer entirely; a "reset to start value" or confirmation would suit a timer meant to be reused.
