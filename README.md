# Archa interview challenge

Running: `docker compose up -d` then visit `http://localhost:8000`

User accounts:

 1. Username: `alice`, password `alice's password`
 2. Username: `bob`, password `bob's password`

There are 3 endpoints:

 1. /me/ - information about the logged in user
 2. /cards/ - cards belonging to the logged in user
 3. /admin/cards - cards that are administered by the logged in user

The 3rd endpoint can be used to edit the limit of cards, etc.
