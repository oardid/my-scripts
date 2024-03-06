@echo off

$Begin = Get-Date -Date '2/29/2024 1:00:00'
$End = Get-Date -Date '2/29/2024 23:00:00'
$24hrevents = Get-EventLog -LogName System -After $Begin -Before $End
$Errors = Get-EventLog -LogName System -EntryType Error
$EventID16 = Get-EventLog -LogName System -InstanceId 16
$Newest20 = Get-EventLog -LogName System -Newest 20
$Events500 = Get-EventLog -LogName System -Newest 500

set /p name=Enter your name:
echo Hello, %name%! Welcome!

Write-Host "List of Variables:"
Write-Host "1. 24hrevents"
Write-Host "2. Errors"
Write-Host "3. EventID16"
Write-Host "4. Newest20"
Write-Host "5. Events500"

$choice = Read-Host "Enter the variable you want to run the command for (e.g., 1 for 24hrevents)"

if'(' "%choice%"=="1" (
    PowerShell -Command "$24hrevents | Format-Table"
) elseif "%choice%"=="2" (
    PowerShell -Command "$Errors | Format-Table"
) elseif "%choice%"=="3" (
    PowerShell -Command "$EventID16 | Format-Table"
) elseif "%choice%"=="4" (
    PowerShell -Command "$Newest20 | Format-Table"
) elseif "%choice%"=="5" (
    PowerShell -Command "$Events500 | Group-Object -Property Source -NoElement | Sort-Object -Property Count -Descending | Format-Table -Wrap | Out-String -Width ([int]::MaxValue)"
) else (
    echo Invalid choice
)
