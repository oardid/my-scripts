# 1.1.5(L1) Set 'Do not allow anonymous enumeration of SAM accounts and shares' policy
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\Lsa" -Name "RestrictAnonymousSAM" -Value 1

# 18.4.3(L1) Set 'Enable insecure guest logons' to Disabled
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters" -Name "EnableInsecureGuestLogons" -Value 0

# Restart the Server service to apply changes
Restart-Service -Name LanmanServer
