---
name: vps-security-hardening
description: "Harden a Linux VPS: fail2ban, UFW, intrusion watchdog."
version: 1.0.0
platforms: [linux]
---

# VPS Security Hardening & Watchdog

Harden a Linux VPS (SSH brute-force protection) and run a silent watchdog that alerts the owner only on NEW suspicious activity. Built and verified on an Ubuntu VPS exposed to active SSH brute-force attacks.

## When to use
- User asks to protect a server from hackers / "tahan dari serangan" / security check
- Setting up or recreating the security watchdog cron job
- Need to reinstall/regenerate the watchdog script referenced by cron

## Steps

### 1. Fail2ban (block brute-force SSH)
```bash
apt-get install -y fail2ban
cat > /etc/fail2ban/jail.local << 'EOF'
[sshd]
enabled = true
port = 22
filter = sshd
logpath = /var/log/auth.log
maxretry = 10
bantime = 300
findtime = 600
EOF
systemctl enable --now fail2ban
systemctl restart fail2ban && fail2ban-client status sshd
```
- User's preferred tuning: **maxretry 10** (not 4), **bantime 300s / 5 min** (not 1 hour). Ask if unsure; these were explicitly requested.
- After restart, `fail2ban-client status` may briefly error "Failed to access socket" — that's normal, retry after ~3s.

### 2. UFW firewall (default deny, open only what's needed)
```bash
ufw default deny incoming
ufw allow 22/tcp && ufw allow 80/tcp && ufw allow 443/tcp
echo "y" | ufw enable && ufw status
```
- Open 80/443 only if a web service runs; 22 is mandatory for SSH.

### 3. Watchdog script (silent unless NEW threats)
Deploy `scripts/security_watch.sh` (in this skill) to `~/.hermes/scripts/security_watch.sh`, `chmod +x`.
It monitors: fail2ban banned IPs, failed SSH logins, failed sudo, high load (miner sign), crypto-miner processes, new user accounts, disk >90%.

**Dedup design (critical, anti-spam):** script is silent when safe; when alerts exist it hashes them (md5sum) and only emits if DIFFERENT from the last emission (state file `~/.hermes/scripts/.security_watch_last`). Identical recurring alerts (e.g. ongoing brute force) fire ONCE, not every tick. State resets when things go quiet, so a returning threat alerts again.

### 4. Cron job (watchdog delivery)
```bash
hermes cronjob create --name security-watch --schedule '*/15 * * * *' --no-agent --script security_watch.sh
```
- `no_agent=true`: empty stdout = silent (nothing sent); non-empty stdout = delivered verbatim to origin chat.
- Script path must be relative to `~/.hermes/scripts/` (just the filename).

## Pitfalls
- Do NOT change the SSH password or root login policy unless the user explicitly asks — user may have strong preferences (this user: "password jangan diapa-apakan").
- Fail2ban bans are per-IP and short (5 min) with these settings — repeated attackers get re-banned each window; that's expected, not a failure.
- The watchdog must be idempotent and stable: no timestamps in output (or every tick looks "changed").
- `write_file` refuses `/etc/` paths — use `cat > file << EOF` via terminal for system configs.

## Verification
- `fail2ban-client status sshd` shows a jail; real banned IPs prove it works (first run on this box caught a live brute-force IP within minutes).
- Run the watchdog twice: first run emits alerts, second run is silent (dedup proof).
- Watch for the `/etc/fail2ban/jail.local` maxretry/bantime to match user preference after any reinstall.

## Support files
- `scripts/security_watch.sh` — the validated watchdog (deploy to `~/.hermes/scripts/`).
