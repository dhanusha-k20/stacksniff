StackSniff
==========

Status: In Development (pre-release)


ABOUT
-----
StackSniff is a framework-aware path enumeration tool for web application
penetration testing. Instead of brute-forcing a generic wordlist against
every target, StackSniff first fingerprints the backend technology stack
(e.g. Django, Laravel, WordPress) a web application is built on, then checks
only the default paths, files, and endpoints known to be relevant to that
specific stack.


WHY
---
Generic directory brute-forcers like Gobuster and ffuf don't know that a
Laravel app is likely to expose .env or storage/logs/laravel.log, or that a
WordPress site might leak user data through wp-json/wp/v2/users. Pentesters
usually end up manually recalling these framework-specific paths during an
engagement.

StackSniff automates that step: identify the stack, then go straight to the
paths that matter for it, cutting noise and saving time during the recon
phase of a pentest.


HOW IT WORKS (PLANNED)
-----------------------
1. Fingerprinting
   Detects the backend framework/CMS via HTTP response headers, cookies,
   and other signals (e.g. X-Powered-By, laravel_session cookie, Django
   default error pages).

2. Path enumeration
   Loads a curated list of default/sensitive paths specific to the
   detected stack (e.g. .env, artisan, wp-config.php.bak, /admin/) and
   checks which ones are accessible.

3. Reporting
   Returns results with status codes and confidence indicators, flagging
   anything worth manual follow-up.


PLANNED FEATURES
-----------------
- Framework/CMS fingerprinting (Laravel, Django, WordPress, and more over time)
- Curated, stack-specific default path wordlists
- False-positive handling for servers that return soft-404s
- Concurrent/threaded scanning for speed
- CLI with JSON output for chaining into other tools


USE CASE
--------
Built primarily for use in authorized web application penetration testing
engagements, as a faster, more targeted alternative/complement to generic
directory brute-forcing during the reconnaissance phase.


TECH STACK
----------
Python (requests, argparse, concurrent.futures)


DISCLAIMER
----------
StackSniff is intended for authorized security testing only. Only use this
tool against systems you own or have explicit written permission to test.
The author is not responsible for misuse of this tool.


---
This project is a work in progress, built as part of ongoing penetration
testing skill development.
