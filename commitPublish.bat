jb build .
git add -A
git commit -m "Publish wiki."
git push origin master
ghp-import -n -p -f _build/html