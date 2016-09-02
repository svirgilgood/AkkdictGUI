#!/usr/bin/env osascript  
on run argv
        activate "Skim"
	set fileName to (item 1 of argv)
	set pageNum to (item 2 of argv) as integer

	tell application "Skim"
		open fileName
		tell document 1
			go to page pageNum
		end tell
		activate
	end tell
end run
