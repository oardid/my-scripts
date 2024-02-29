@echo off 
set /p name=Enter your name:
echo Hello, %name%! Welcome!
set /p source_folder=Enter the source folder path:
set /p dest_folder=Enter the destination folder path:
if not exist %source_folder% (
	echo Error: Source folder doesn't exist.
	goto :eof
)
if not exist %source_destination% (
	echo Error: Destination folder doesn't exist
	goto :eof
)

robocopy %source_folder% %source_destination% /R
:end
