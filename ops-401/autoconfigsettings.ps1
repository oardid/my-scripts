# Configure Minimum password length (1.1.5 L1)
Set-LocalUser -Name "*" -MinimumPasswordLength 14

# Configure SMB v1 client driver (18.4.3 L1)
Set-SmbClientConfiguration -EnableSMB1Protocol $false
