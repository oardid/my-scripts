@echo off

$CPU = Get-Process | Sort-Object CPU -Descending
echo $CPU

$ID = Get-Process | Sort-Object ID -Descending
echo $ID

$WorkSet = Get-Process | Sort-Object WorkingSet -Descending
echo $WorkSet

$StartWeb = Start-Process "chrome" -ArgumentList "https://owasp.org/www-project-top-ten/"
echo $StartWeb

$Note = for ($i = 1; $i -le 10; $i++) {
    Start-Process "notepad.exe"
}
Get-Process notepad | Stop-Process
