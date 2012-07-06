#!/bin/evn python
import pexpect, struct, fcntl, termios, signal, sys

p = None

def sigwinch_passthrough (sig, data):
        s = struct.pack("HHHH", 0, 0, 0, 0)
        a = struct.unpack('hhhh', fcntl.ioctl(sys.stdout.fileno(), termios.TIOCGWINSZ , s))
        global p
        p.setwinsize(a[0],a[1])

def ssh(ip, port=22, name='gaohao', password='gaohao123'):
  global p
  tokens = ['ssh', '-p', str(port), name + "@" + ip]
  command = " ".join(tokens)
  print >>sys.stderr, command
  p = pexpect.spawn(command)
  expect1 = name + "@" + ip + "'s password:"
  p.expect(expect1)
  print >>sys.stderr, "send password"
  p.sendline(password)
  signal.signal(signal.SIGWINCH, sigwinch_passthrough)
  p.interact()

if __name__ == '__main__':
  ip = sys.argv[1]
  port = int(sys.argv[2])
  user = sys.argv[3]
  password = sys.argv[4]
  ssh(ip, port, user, password)
