#!/usr/bin/python3

import sys
import pexpect
import subprocess

c = pexpect.spawn('./bin/opi -n html2text', logfile=sys.stdout.buffer, echo=False)

c.expect(r'([0-9]+)\. html2text', timeout=10)
c.expect('Pick a number')
c.expect(r'([0-9]+)\. [^ ]*(openSUSE-Tumbleweed-Oss|Main Repository)', timeout=10)
c.expect('Installing from existing repo', timeout=10)
c.expect('Continue?', timeout=20)
c.interact()
c.wait()
c.close()
print()
assert c.exitstatus == 0, f'Exit code: {c.exitstatus}'
subprocess.check_call(['rpm', '-qi', 'html2text'])


c = pexpect.spawn('./bin/opi -n zfs', logfile=sys.stdout.buffer, echo=False)

c.expect(r'([0-9]+)\. zfs', timeout=10)
c.expect('Pick a number')
c.expect(r'([0-9]+)\. [^ ]*(filesystems)', timeout=10)
c.expect('Adding repo \'filesystems\'', timeout=10)
c.expect('Continue?', timeout=20)
c.interact()
c.wait()
c.close()
print()
assert c.exitstatus == 0, f'Exit code: {c.exitstatus}'
subprocess.check_call(['rpm', '-qi', 'zfs'])
