$firstname = Read-Host "Enter first name"
$lastname = Read-Host "Enter last name"
$email = Read-Host "Enter email address"
$samAccountName = "$firstname $lastname"
$password = Read-Host "Enter password" -AsSecureString
$company = Read-Host "Enter company"
$department = Read-Host "Enter department"
$jobTitle = Read-Host "Enter job title"
$location = Read-Host "Enter location"
$fullName = "$firstName $lastName"

$domain = "corp.globex.com" 
$userPrincipalName = "$samAccountName@$domain"

New-ADUser -Name $fullName `
    -SamAccountName $samAccountName `
    -EmailAddress $email `
    -UserPrincipalName $userPrincipalName `
    -AccountPassword $password `
    -Enabled $true `
    -Company $company `
    -Department $department `
    -Title $jobTitle `
    -Office $location `
    -ChangePasswordAtLogon $true
